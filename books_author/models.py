from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.FloatField()
    publish_date = models.DateField()

    def __str__(self):
        return self.title
