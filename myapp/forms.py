from django import forms
from django.forms import ModelForm
from .models import Flower

class MyForm(ModelForm):
    class Meta:
        model = Flower
        fields = ['title',
                  'description',
                  'image',
                  'slug',
                  'category',
                  'tags']
