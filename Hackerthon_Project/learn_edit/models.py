from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField('제목:',max_length=40, null=False)
    content = models.TextField('내용:', null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    link = models.CharField('링크주소:', max_length=100, null=False)

    def __str__(self):
        return self.title



class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="contents")
    content = models.CharField(" ", max_length=100)

    def __str__(self):
        return self.content

