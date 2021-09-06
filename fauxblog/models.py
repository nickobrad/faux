from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.postgres import search
import datetime as dt

# Create your models here.
class Location(models.Model): 
    location = models.CharField(max_length = 30, blank = False, null = False)

    def __str__(self):
        return self.location

    def save_location(self):
        return self.save()

    def delete_location(self):
        return self.delete()

    def update_location(self):
        return self.save()

class Category(models.Model):
    category = models.CharField(max_length = 30, blank = False, null = False)

    def __str__(self):
        return self.category

    def save_category(self):
        return self.save()

    def delete_category(self):
        return self.delete()

    def update_category(self):
        return self.save()

class ImagePost(models.Model):
    image_name = models.CharField(max_length = 30, blank = False)
    image_description = models.TextField(blank = False, null = False)
    image_location = models.ForeignKey(Location, on_delete = models.CASCADE)
    image_category = models.ForeignKey(Category, on_delete = models.CASCADE)
    date_publshed = models.DateTimeField(auto_now_add = True)
    posted_by = models.ForeignKey(User, on_delete = models.CASCADE,)
    image = models.ImageField(upload_to = 'images/') 

    def get_absolute_url(self):
        return reverse('postdetails', args=(str(self.pk)))

    def save_image(self):
        return self.save()

    def delete_image(self):
        return self.delete()

    @classmethod
    def get_image_by_id(cls, id):
        picture = cls.objects.filter(id = id).first()
        return picture

    @classmethod
    def search_by_category(cls,search_term):
        pictures = cls.objects.filter(image_category__category__icontains = search_term)
        return pictures

    @classmethod
    def filter_by_location(cls, location):
        pictures = cls.objects.filter(image_location_id = location).all()
        return pictures

