from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return self.name


class Blogs(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    author = models.CharField(max_length=15)
    image = models.ImageField(upload_to='blog', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Services(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()

    def __str__(self):
        return self.title




