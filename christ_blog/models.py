from django.db import models

# Create your models here.

class Versicles(models.Model):
    book = models.CharField(max_length=200)
    cap_number = models.IntegerField()
    ver_number = models.IntegerField()
    versicle = models.TextField()
    teaching = models.TextField()

    def __str__(self):
        return self.book

