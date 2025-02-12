
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from . import views

urlpatterns = [
    path('user_posts/<str:user>', views.user_posts, name='user_posts'),
    path('all_posts', views.all_posts, name='all_posts'),
    path('user_profile/<str:user>', views.user_profile, name='user_profile'),
    path('like/<str:post_id>', views.toggle_like, name='like'), #nouns are bad urls. should avoid nouns in naming
    path('subscribe/<str:user_id>', views.toggle_follow, name='follow'),
    path('following_posts', views.following_posts, name='following_posts'),
    path('comments/<str:post_id>', views.Comments.as_view(), name='comments'),
    path('edit/<str:post_id>', views.edit, name='comments'),
    path('new_post', views.new_post, name='new_post'),
    path('register', views.Register.as_view(), name='register'),
    path('login', views.Login.as_view(), name='register'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    #two user_posts/profile... dont map on navigation, so needs rethinking

]

"""
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),"""