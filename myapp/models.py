from django.db import models

from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill

from django.utils.text import slugify
from django.urls import reverse

from django.utils.text import slugify

class Category(models.Model):

    title = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.title

class Tag(models.Model):

    title = models.CharField(max_length=255, default='')
    slug = models.SlugField(blank=True, default='')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Tag, self).save()

class Flower(models.Model):
    title = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    image = models.ImageField(default='', blank=True, upload_to='images')
    image_thumbnail = ImageSpecField(source='image',
        processors=[ResizeToFill(100, 100)],
        format='JPEG',
        options={'quality': 60})
    slug = models.SlugField(blank=True, default='')

    category = models.ForeignKey(Category, null=True, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag)

    def __str__(self):			     
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Flower, self).save()

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.slug)])
