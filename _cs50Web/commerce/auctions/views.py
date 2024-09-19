from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Listing, Bid, Comment, Category, Connection
from .forms import CreateListingForm, MakeBid #MakeComment #AddToWatchlist
from django.contrib.auth.decorators import login_required

class SimpleObject:
    pass


def index(request):
    index_listing = Listing.objects.filter(closed=False)
    list_of_listings = list()

    for listing in index_listing:
        listing_w_categ = SimpleObject()
        listing_w_categ.listing = listing
        listing_w_categ.categories = listing.category.all()
        list_of_listings.append(listing_w_categ)
    # So our listing objects will have two attributes in one part is index listing and the other is a list of categories
    return render(request, "auctions/index.html", {
        'listings': list_of_listings,
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def create_listing(request):
    if request.method == 'GET':
        form = CreateListingForm()
        return render(request, "auctions/create_listing.html", {
            'form':form
        })
    else:
        if request.POST.get('action') == "add_category":
            category = Category() #(id=listing_id).watchlist.add(request.user)
            category.category = request.POST.get('category')
            category.save()
            return HttpResponseRedirect(reverse("create_listing"))
        
        form = CreateListingForm(request.POST)
        form.creator = request.user
        
        
        if form.is_valid():
            listing = form.save(commit=False)  # Create a model instance but do not save to DB yet
            listing.creator = request.user  # Set the creator to the current logged-in user
            listing.save()  # Save the instance to the database

            categories = form.cleaned_data['category']
            for category in categories:
                Connection.objects.create(listing=listing, category=category)
                print("Selected categories:", category)
            return HttpResponseRedirect(reverse("index"))  # Redirect to a success page or another relevant URL

@login_required
def listing(request, listing_id): # why is listing an unexpected key word??? why should i put listing here?
    if request.method == 'GET':
        listing_info = Listing.objects.get(id=listing_id)
        # so I want to make sure that if listing is closed, the user should be informed.
        current_bid = Bid.objects.filter(listing=listing_id).last()
        comments = Comment.objects.filter(listing=listing_id)
        make_bid = MakeBid()
        winner = False

        if listing_info.creator == request.user:
            listing_admin = True
        else:
            listing_admin = False

        if current_bid == None:
            current_bid = Bid()
            current_bid.bid = listing_info.starting_price
        else:
            if listing_info.closed == True:
                this_user = request.user.id
                if this_user == current_bid.user.id:
                    winner = True
        
        categories = listing_info.category.all()

        return render(request, "auctions/listing.html", {
            "listing": listing_info,
            "current_bid": current_bid.bid,
            "make_bid": make_bid,
            "comments": comments,
            "listing_admin": listing_admin,
            "winner": winner,
            "categories": categories
        })

    else:
        if request.POST.get('action') == "make_bid":
            this_listing = Listing.objects.get(id=listing_id)
            if this_listing.closed == True:
                return HttpResponse("sorry, cant bet on closed")
            make_bid = MakeBid(request.POST)
            if make_bid.is_valid():
                user_bid = make_bid.save(commit=False)
                past_bid = Bid.objects.filter(listing=listing_id).last()
                if past_bid == None:
                    if user_bid.bid >= this_listing.starting_price:
                        user_bid.user = request.user
                        user_bid.listing =  this_listing
                        user_bid.save()
                        return HttpResponseRedirect(reverse("listing", kwargs={'listing_id': listing_id}))
                elif int(user_bid.bid) > int(past_bid.bid):
                    user_bid.user = request.user
                    user_bid.listing = this_listing
                    user_bid.save()
                    return HttpResponseRedirect(reverse("listing", kwargs={'listing_id': listing_id}))
                else:
                    return HttpResponse("the bid is too small")
                
        elif request.POST.get('action') == "add_to_watch":
            Listing.objects.get(id=listing_id).watchlist.add(request.user)
            return HttpResponseRedirect(reverse("listing", kwargs={'listing_id': listing_id}))
        
        elif request.POST.get('action') == "close":
            this_listing = Listing.objects.get(id=listing_id)
            if this_listing.creator == request.user:
                this_listing.closed = True
                this_listing.save()
                return HttpResponseRedirect(reverse("listing", kwargs={'listing_id': listing_id}))

        else:
            comment = Comment()
            comment.comment = request.POST.get('comment')
            comment.user = request.user
            comment.listing = Listing.objects.get(id=listing_id)
            comment.save()
            return HttpResponseRedirect(reverse("listing", kwargs={'listing_id': listing_id}))

@login_required
def watchlist(request):
    # There is a many to many field, called "watching" that connects user to listing
    # how to get all listings for a user?
    this_user = request.user.id
    wathing_listing = User.objects.get(id = this_user).watching.all()
    return render(request, "auctions/watchlist.html", {
        'listings': wathing_listing
    })

def categories(request):
    categories = Category.objects.all()
    return render(request, "auctions/category_page.html", {
        'categories': categories
    })

def category(request, category):
    this_category = Category.objects.get(category=category)
    listings = this_category.lising_with_cat.all()
    list_of_listings = list()
    for listing in listings:
        listing_w_categ = SimpleObject()
        listing_w_categ.listing = listing
        listing_w_categ.categories = listing.category.all()
        list_of_listings.append(listing_w_categ)

    return render(request, "auctions/selected_category.html", {
        "category": this_category,
        'listings': list_of_listings
    })