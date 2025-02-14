from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("new_page/", views.new_page, name="new_page"),
    path("edit_page/<str:entry>/", views.edit_page, name="edit_page"),
    path('random', views.random_page, name="random"),
    path("<str:entry>", views.entry, name="entry"),
    path("<str:entry>/", views.entry, name="entry")
]
