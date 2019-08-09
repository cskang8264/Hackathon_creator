from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth
from Project import settings

class Place(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user', default=1)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')
    body = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    time = models.CharField(max_length=20)

    # lon = models.DecimalField(max_digits=8, decimal_places=3)
    # lat = models.DecimalField(max_digits=8, decimal_places=3)

    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='likes')
    
    @property
    def total_likes(self):
        return self.likes.count()
    # like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_post', blank=True)
    # favorite = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='favorite_post', blank=True)
   
    # def __init__(request, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    def __str__(self):
        return self.title

# def get_absolute_url(sel):
#     return reverse('place_datail', args=[self.id])

class Comment(models.Model):
    place_id = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="comments")
    comment_text = models.CharField(max_length=50)

    def __str__(self):
        return self.comment_text
# Create your models here.
