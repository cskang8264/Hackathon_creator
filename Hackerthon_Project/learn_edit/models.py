from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=40, null=False)
    content = models.TextField(null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.title



class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="contents")
    content = models.CharField(" ", max_length=100)

    def __str__(self):
        return self.content

class Hastag(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name