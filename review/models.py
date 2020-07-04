from django.db import models
from django.utils.text import slugify
from embed_video.fields import EmbedVideoField
from filer.fields.file import FilerFileField
from filer.fields.image import FilerImageField
from django.urls import reverse
from django.contrib.auth.models import User
# from filer.fields.image import FilerImageField

# Create your models here.
ONE = 1
TWO = 2
THREE = 3
FOUR = 4
FIVE = 5
SIX= 6
SEVEN=7
EIGHT=8
NINE=9
TEN=10
STATUS_CHOICES = (
    (ONE, 'One'),
    (TWO, 'Two'),
    (THREE, 'Three'),
    (FOUR, 'Four'),
    (FIVE, 'Five'), 
    (SIX, 'Six'),
    (SEVEN, 'Seven'),
    (EIGHT, 'Eight'),
    (NINE, 'Nine'),
    (TEN, 'Ten'),
)
RESTAURANT=1
REVIEW=2
VLOG=3
BLOG=4
VIDEO=5
RECIPE=6
MODEL_CHOICES=(
    (RESTAURANT,"Restaurant"),
    (REVIEW,"Review"),
    (VLOG,"Vlog"),
    (BLOG,"Blog"),
    (VIDEO,"Video"),
    (RECIPE,"Recipe"),

)
class Restaurant(models.Model):
    dishes=models.ForeignKey("Dish", on_delete=models.CASCADE,blank=True,null=True)
    menu = models.ImageField( upload_to="restaurant")
    image=models.ImageField(upload_to="rstaurantimage")
    name=models.CharField(max_length=100)
    about=models.TextField( max_length=1000)
    slug=models.SlugField(blank=True, null=False)
    created = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(choices=STATUS_CHOICES, unique=True)
    pinned=models.BooleanField(default=False)
    desc=models.CharField(max_length=90)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Restaurant, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    


class Dish(models.Model):
    owner=models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    image=models.ImageField(upload_to="dish")
    review=models.TextField()
    name=models.CharField( max_length=100)
    slug=models.SlugField(blank=True, null=False)
    created = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(choices=STATUS_CHOICES, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Dish, self).save(*args, **kwargs)

    def __str__(self):
            return self.name
        
class Review(models.Model):
    images=models.ForeignKey("ReviewImage",on_delete=models.CASCADE,blank=True,null=True)
    reviewtext=models.TextField()
    image=models.ImageField( upload_to="mainreview")
    name=models.CharField( max_length=100)
    slug=models.SlugField(blank=True, null=False)
    created = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(choices=STATUS_CHOICES, unique=True)
    desc=models.CharField(max_length=90)
    pinned=models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Review, self).save(*args, **kwargs)

    def __str__(self):
            return self.name

class ReviewImage(models.Model):
    belong=models.ForeignKey(Review, on_delete=models.CASCADE)
    image=models.ImageField(upload_to="image-review")

class Video(models.Model):
    video = EmbedVideoField(blank=True)
    name =models.CharField( max_length=100)
    image=models.ImageField(upload_to="video-image")
    slug=models.SlugField(blank=True, null=False)
    created = models.DateTimeField(auto_now_add=True)
    desc=models.CharField(max_length=90)
    pinned=models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Video, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Vlog(models.Model):
    title=models.CharField(max_length=100)
    text=models.TextField()
    image=models.ImageField( upload_to="vlog-media")
    video = EmbedVideoField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(blank=True, null=False)
    desc=models.CharField(max_length=90)
    pinned=models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Vlog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Blog(models.Model):
    title=models.CharField(max_length=100)
    text=models.TextField()
    image=models.ImageField( upload_to="vlog-media")
    created = models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(blank=True, null=False)
    desc=models.CharField(max_length=90)
    pinned=models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
'''
class Test(models.Model):
    image=FilerImageField(blank=True,null=True,on_delete=models.CASCADE)
'''
class Recipe(models.Model):
    title=models.CharField(max_length=100)
    text=models.TextField()
    image=models.ImageField( upload_to="recipe-media")
    created = models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(blank=True, null=False)
    desc=models.CharField(max_length=90)
    video = EmbedVideoField(blank=True)
    pinned=models.BooleanField(default=False)
    rating = models.IntegerField(choices=STATUS_CHOICES, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Recipe, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("food:home", kwargs={"pk": self.pk})
    

class Model(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    title=models.CharField(max_length=100)
    text=models.TextField()
    image=models.ImageField( upload_to="model-media")
    created = models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(blank=True, null=False)
    desc=models.CharField(max_length=90)
    video = EmbedVideoField(blank=True)
    pinned=models.BooleanField(default=False)
    rating = models.IntegerField(choices=STATUS_CHOICES, unique=True)
    category = models.IntegerField(choices=MODEL_CHOICES, unique=True)
    images=FilerImageField(blank=True,null=True,on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Model, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("food:home", kwargs={"pk": self.pk})
