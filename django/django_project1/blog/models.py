from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

#class in django means one table in database
class Post(models.Model):
    #create attributes in database like title
    title=models.CharField(max_length=100)
    content= models.TextField()
    data_posted=models.DateTimeField(default=timezone.now) #here we use default because of timezone are different for that we imported timezone from django.utilis
    author= models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title