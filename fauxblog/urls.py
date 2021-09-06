"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views
from .views import DeletePost, HomeView, PostDetailView, AddPost, UpdatePost, DeletePost, post_by_location, search_results

urlpatterns = [
    path('blog', HomeView.as_view(), name = 'home'),
    path('blog/<int:pk>', PostDetailView.as_view(), name = 'postdetails'),
    path('blog/add', AddPost.as_view(), name = 'addpost'),
    path('blog/update/<int:pk>', UpdatePost.as_view(), name = 'updatepost'),
    path('blog/delete/<int:pk>', DeletePost.as_view(), name = 'deletepost'),
    path('blog/location/<str:locale>', post_by_location, name = 'post_location'),
    url(r'^blog/search/', search_results, name = 'search_results'),
]
