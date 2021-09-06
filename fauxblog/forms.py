from django import forms
from django.forms.widgets import Widget
from .models import ImagePost
import datetime as dt

class ImageForm(forms.ModelForm):

    class Meta:
        model = ImagePost
        fields = ('image_name', 'image_location', 'image_description', 'image_category','posted_by', 'image')

        widgets = {
            'image_name': forms.TextInput(attrs = {'class': 'form-control form-floating mb-3', 'Placeholder': 'Image Title'}),
            'image_location': forms.Select(attrs = {'class': 'form-control', 'label': 'Location Taken', 'Placeholder': 'Image Title'}),
            'image_description': forms.Textarea(attrs = {'class': 'form-control','Label': '', 'Placeholder': 'Image Description'}),
            'posted_by': forms.TextInput(attrs = {'class': 'form-control','id': 'user', 'value': '', 'type': 'hidden'}),
            'image_category': forms.Select(attrs = {'class': 'form-control', 'Placeholder': 'Image Category'}),
            'image': forms.FileInput(attrs = {'class': 'form-control', 'type': 'file'})
        }

class ImageUpdateForm(forms.ModelForm):

    class Meta: 
        model = ImagePost
        fields = ('image_name', 'image_location', 'image_description', 'image_category')

        widgets = {
            'image_name': forms.TextInput(attrs = {'class': 'form-control form-floating mb-3'}),
            'image_location': forms.TextInput(attrs = {'class': 'form-control'}),
            'image_description': forms.Textarea(attrs = {'class': 'form-control'}),
            'image_category': forms.Select(attrs = {'class': 'form-control'}),
        }
        