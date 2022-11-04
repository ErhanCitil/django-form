from django.db import models

# Create your models here.
class Contactdata(models.Model):
    naam = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    onderwerp = models.CharField(max_length=255)
    bericht = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'contactdata'