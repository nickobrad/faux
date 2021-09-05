from django.contrib import admin
from .models import Category, ImagePost, Location

# Register your models here.

admin.site.register(ImagePost)
admin.site.register(Category)
admin.site.register(Location)

