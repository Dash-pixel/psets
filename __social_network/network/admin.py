from django.contrib import admin
from .models import User, Post, FollowerInfluencer, Comment, Likes

admin.site.register(User)
admin.site.register(FollowerInfluencer)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Likes)