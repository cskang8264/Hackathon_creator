from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth
from Project import settings

class Place(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user', default=10)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')
    body = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)

    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_post', blank=True)
    favorite = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='favorite_post', blank=True)


def __str__(self):
    return self.title


def get_absolute_url(self):
    return reverse('place:detail', args=[self.id])
class Comment(models.Model):
    place_id = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="comments")
    comment_text = models.CharField(max_length=50)

    def __str__(self):
        return self.comment_text
# Create your models here.

