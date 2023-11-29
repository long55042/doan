from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.title}"
# Create your models here.
class avatar(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True)
    # avatar = models.URLField()
    email_page = models.EmailField(max_length=75, null=True) 
    phone = models.CharField(max_length=10, blank=True)
    author = models.TextField(null= True)
    def __str__(self):
        return self.title
    