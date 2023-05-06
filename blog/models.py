from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
