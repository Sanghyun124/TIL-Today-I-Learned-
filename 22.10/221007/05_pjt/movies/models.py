from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=20)
    audience=models.IntegerField()
    release_date=models.DateField()
    genre=models.CharField(max_length=30)
    score=models.FloatField()
    poster_url=models.TextField()
    description=models.TextField()
    author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
