from django.db import models
class Movie(models.Model):
    name=models.CharField(max_length=150)
    desc=models.TextField()
    year=models.IntegerField()
    image=models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name