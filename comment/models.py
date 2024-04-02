from django.db import models
from car.models import Car
from django.contrib.auth.models import User
# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.car.model}"