from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Category(models.Model):
    category = models.CharField(max_length=75, unique=True)
    def __str__(self):
        return self.category

class Listing(models.Model):
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=300, null=True)
    imageUrl = models.CharField(max_length=500, null=True)
    starting_price = models.IntegerField()
    category = models.ManyToManyField(Category, through='Connection', related_name = "lising_with_cat", blank=True)
    #not user input
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "user_listings", blank=True)
    watchlist = models.ManyToManyField(User, related_name = "watching", blank=True)
    closed = models.BooleanField(default=False)

class Connection(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name = "bids")
    bid = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "user_bid")

class Comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name = "comments")
    comment = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "user_comment")

