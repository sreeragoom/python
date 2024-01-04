from django.db import models


# Create your models here.
class Players(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    position = models.CharField(max_length=50)
    desc = models.TextField()
    market_value = models.IntegerField()
    img=models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name
