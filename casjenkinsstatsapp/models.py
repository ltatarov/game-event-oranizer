from django.db import models

# Create your models here.


class Table(models.Model):
    max_guests = models.IntegerField()
    guests = models.ManyToManyField('Guest')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __unicode__(self):
        return self.name


class Guest(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name