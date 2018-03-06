from django.db import models
from django.utils import timezone

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=30)
    dob = models.DateField("Date of Birth")

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=1000, blank= True )
    pub_time = models.DateTimeField("publish time", default= timezone.now())
    edited_time = models.DateTimeField("Edit time", blank= True, default= timezone.now())
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    def __str__(self):
        return self.title