from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    author  = models.CharField(max_length=255)
    inventory = models.IntegerField(default=10)
    class Meta:
        indexes = [models.Index(fields=['price']),]

