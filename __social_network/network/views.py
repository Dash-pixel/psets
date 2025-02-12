from django.contrib.auth import authenticate
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from .models import User, Post, FollowerInfluencer, Likes, Comment
import json
from .serializers import UserSerializer
############################################################
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from django.contrib.auth import authenticate
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .middleware.jwtcookie_auth import CookieJWTAuthentication

class Register(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save() # this thing resturns the user
            refresh = RefreshToken.for_user(user)

            response = Response({"id": user.id}, status=status.HTTP_201_CREATED)
            response.set_cookie(
                key='access',
                value=str(refresh.access_token),
                httponly=True,
                secure=True,  # set to true in production (use https)
                samesite='strict',  # prevent csrf
                max_age=7 * 24 * 60 * 60,  # expire after 7 days
            )
            response.set_cookie(
                key='refresh',
                value=str(refresh),
                httponly=True,
                secure=True,  # set to true in production (use https)
                samesite='strict',  # prevent csrf
                max_age=7 * 24 * 60 * 60,  # expire after 7 days
            )
            return response
class Login(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )
        
        response = Response({"id": user.id}, status=status.HTTP_200_OK)

        if user:
            refresh = RefreshToken.for_user(user)
            response.set_cookie(
                key='access',
                value=str(refresh.access_token),
                httponly=True,
                secure=True,  # set to true in production (use https)
                samesite='strict',  # prevent csrf
                max_age=7 * 24 * 60 * 60,  # expire after 7 days
            )
            response.set_cookie(
                key='refresh',
                value=str(refresh),
                httponly=True,
                secure=True,  # set to true in production (use https)
                samesite='strict',  # prevent csrf
                max_age=7 * 24 * 60 * 60,  # expire after 7 days
            )
            print(refresh.access_token)
            return response
        else:
            return response({'error': 'invalid credentials'}, status=status.http_401_unauthorized)
@api_view(['POST'])
@authentication_classes([CookieJWTAuthentication])
@permission_classes([IsAuthenticated])
def new_post(request):
    form = json.loads(request.body) # {'name': 'lk', 'text': 'lk'}
    print(form)
    post = Post(
        title = form['name'],
        content = form['text'],
        user = request.user
    )
    post.save()
    return JsonResponse({"all is" :'fine'})

def get_posts_response(queryset):
    posts = list(queryset[:10].values('id', 'title', 'content', 'created_at', 'user_id', 'user__username', 'like_count'))
    return JsonResponse(posts, safe=False)

def user_posts(request, user):
    if request.GET.get('from'):
        queryset = Post.objects.filter(user__id=user, id__lt = request.GET.get('from'))
    else:
        queryset = Post.objects.filter(user__id=user)
    return get_posts_response(queryset)

def all_posts(request):
    if request.GET.get('from'):
        queryset = Post.objects.filter(id__lt = request.GET.get('from'))
    else:
        queryset = Post.objects.all()
    return get_posts_response(queryset)

@api_view(['GET'])
@authentication_classes([CookieJWTAuthentication])
@permission_classes([IsAuthenticated])
def following_posts(request):
    if request.GET.get('from'):
        queryset = Post.objects.filter(user__influencer_relations__follower=request.user, id__lt = request.GET.get('from'))
    else:
        queryset = Post.objects.filter(user__influencer_relations__follower=request.user)
    return get_posts_response(queryset)


def user_profile(request, user): # need to add followed for the request user
    user_obj = User.objects.get(id=user)
    follower_count = FollowerInfluencer.objects.filter(influencer=user_obj).count()
    following_count = FollowerInfluencer.objects.filter(follower=user_obj).count()

    user_dict = {
        'followers': follower_count,
        'username': user_obj.username,
        'following': following_count,
        'id': user_obj.id,
        'followed': True
        }
    return JsonResponse(user_dict, safe=False)

@api_view(['POST'])
@authentication_classes([CookieJWTAuthentication])
@permission_classes([IsAuthenticated])
def toggle_like(request, post_id):
    post= Post.objects.get(id=post_id)
    
    try:
        like = Likes.objects.get(user=request.user, post=post)
        like.delete()
        liked = False

    except Likes.DoesNotExist:
        like = Likes(
            user = request.user,
            post = post
        )
        like.save()
        liked = True
        
    to_upd = Post.objects.get(id=post.id)
    to_upd.like_count = to_upd.like_count + 1 if liked else to_upd.like_count - 1 
    to_upd.save()
    # maybe we can count the entries each time by select count? Create better datastruct?
    # + race condition   
    return JsonResponse({'count':to_upd.like_count, 'liked':liked})

@api_view(['POST'])
@authentication_classes([CookieJWTAuthentication])
@permission_classes([IsAuthenticated])
def toggle_follow(request, user_id):
    influencer = User.objects.get(id=user_id)
    if influencer == request.user:
        return HttpResponse('CANT FOLLOW YOURSELF')
    try:
        follow = FollowerInfluencer.objects.get(follower=request.user, influencer=influencer)
        follow.delete()

    except FollowerInfluencer.DoesNotExist:
        follow = FollowerInfluencer(
            influencer = influencer,
            follower = request.user
        )
        follow.save()
    
    follower_count=FollowerInfluencer.objects.filter(influencer=influencer).count()
    return JsonResponse({'followers':follower_count})


class Comments(APIView):
    def get(self, request, post_id):
        total_comments = Comment.objects.filter(post__id=post_id).count()
        offset_index = max(total_comments - 5, 0)
        comments = list(Comment.objects.filter(post__id=post_id).order_by('id')[offset_index:].values())        
        
        return JsonResponse(comments, safe=False)
    
    def post(self, request, post_id):
        # Enforce authentication and permissions for POST requests
        self.authentication_classes = [CookieJWTAuthentication]
        self.permission_classes = [IsAuthenticated]
        
        comment = Comment(
            user = request.user,
            post = Post.objects.get(id=post_id),
            comment = json.loads(request.body) # here is the misstake
        )
        comment.save()
        return HttpResponse()


@api_view(['POST'])
@authentication_classes([CookieJWTAuthentication])
@permission_classes([IsAuthenticated])
def edit(request, post_id):
    post = Post.objects.get(id = post_id)
    if request.user == post.user:
        post.content = 'Edited post: ' + json.loads(request.body)
        post.save()
        return HttpResponse('fine')
    else:
        return HttpResponse('edit mistake, possibly not logged in')
        #post.content =  only in that case update but also write editлдed at the beggining 