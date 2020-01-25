from django.db import models


# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.CharField(max_length=2400, blank=True, null=True)


class Car(models.Model):
    name = models.CharField(max_length=400, blank=True, null=True)
    model = models.CharField(max_length=400, blank=True, null=True)
    price = models.CharField(max_length=42, blank=True, null=True)
    photo = models.FileField(blank=True, null=True)


class General(models.Model):
    name = models.CharField(max_length=400, blank=True, null=True)
    title = models.CharField(max_length=400, blank=True, null=True)
    firstContent = models.CharField(max_length=2400, blank=True, null=True)
    secondContent = models.CharField(max_length=2400, blank=True, null=True)
    footerDescription = models.CharField(max_length=400, blank=True, null=True)
    facebookLink = models.CharField(max_length=50, blank=True, null=True)
    instagramLink = models.CharField(max_length=50, blank=True, null=True)
    snapchatLink = models.CharField(max_length=50, blank=True, null=True)
    twitterLink = models.CharField(max_length=50, blank=True, null=True)


class Contact(models.Model):
    citiesAv = models.CharField(max_length=400, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    mail = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    openHr = models.CharField(max_length=40, blank=True, null=True)


class UserLogin(models.Model):
    username = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=40, blank=True, null=True)