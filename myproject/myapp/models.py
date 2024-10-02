from django.db import models

# Create your models here.
class MyModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    password = models.CharField()

    def __str__(self):
        return self.name
