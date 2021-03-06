from django.db import models

class Editor(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')
    body = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)

def __str__(self):
    return self.title


class Comment(models.Model):
    editor_id = models.ForeignKey(Editor, on_delete=models.CASCADE, related_name="comments")
    comment_text = models.CharField(max_length=50)

    def __str__(self):
        return self.comment_text
# Create your models here.

