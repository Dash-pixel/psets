from django import forms

from .models import User, Listing, Bid, Comment

class CreateListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        exclude = ['creator', 'watchlist', 'closed']

class MakeBid(forms.ModelForm):
    class Meta:
        model = Bid
        exclude = ['listing', 'user']

"""class MakeComment(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['listing', 'user']
"""
"""class AddToWatchlist(forms.ModelForm):
     class Meta:
         model = User
         fields = ['watching']"""