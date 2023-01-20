from django.db import models
from django.conf import settings
# Create your models here.
class TODO(models.Model):
    ticket= models.CharField(max_length=64, null=False)
    seriale = models.TextField(null=False)
    imei = models.TextField(null=False)
    stato = models.TextField(max_length=200, null=False, default="")
    tipo_guasto = models.TextField(max_length=200, null=False, default="")

    def __str__(self):
        return self.ticket