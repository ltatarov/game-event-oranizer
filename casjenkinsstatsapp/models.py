from django.db import models

# Create your models here.


class Table(models.Model):
    max_guests = models.IntegerField()
    guests = models.ManyToManyField('Guest', through='Membership')
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __unicode__(self):
        return self.name


class Guest(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Membership(models.Model):
    table = models.ForeignKey(Table)
    guest = models.ForeignKey(Guest)