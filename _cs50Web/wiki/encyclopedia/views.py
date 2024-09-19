from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from . import util
import random
from markdown2 import Markdown
markdowner = Markdown()
from django.utils.safestring import mark_safe



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def search(request):
    search = request.GET['q'].lower()
    #entries = util.list_entries()
    pages = set([page.lower() for page in util.list_entries()]) # maybe should do a dict with key value pairs to store both
    # or associate a name with a value using attributes?
    if search in pages:
        return render(request, "encyclopedia/entry.html", {
            "entry_name" : search, #need to think a bit here,
            "page_content" : util.get_entry(search)
        })
    else:
        # here we need to implement a string search
        list_of_matches = []
        for string in pages:
             if search in string:
                list_of_matches.append(string)

        return render(request, "encyclopedia/search_page.html", {
             "entries": list_of_matches
        })
#

def entry(request, entry):
    look_up_entry = entry.lower()
    page_content = util.get_entry(look_up_entry)
    if page_content == None:
            return HttpResponse("No such page 404")
    return render(request, "encyclopedia/entry.html", {
        "entry_name" : entry,
        "page_content" : markdowner.convert(page_content)
    })

def new_page(request):
    if request.method == 'GET':
        return render(request, "encyclopedia/new_page.html")
    else:
        title = request.POST['title']
        textarea = request.POST['textarea']
        entries = set([page.lower() for page in util.list_entries()])
        if title is None:
            return HttpResponse("Cant create with no name")
        if title in entries:
            return HttpResponse("Name is taken")
        util.save_entry(title, textarea)
        return redirect(reverse(index)+title)

def edit_page(request, entry):
    if request.method == 'GET':
        return render(request, "encyclopedia/edit_page.html", {
            "page_title": entry,
            "text_area": util.get_entry(entry)
        })
    else:
        textarea = request.POST['text-area']
        util.save_entry(entry, textarea)
        return redirect(reverse(index)+entry)

def random_page(request):
    list_of_entries = util.list_entries()
    random_entry = random.choice(list_of_entries)
    return redirect(reverse(index)+random_entry)