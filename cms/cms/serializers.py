from django.contrib.auth.models import User, Group
from rest_framework import serializers
from . import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.News
        fields = ('id', 'title', 'content')


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Car
        fields = ('id', 'name', 'model', 'price', 'photo')


class GeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.General
        fields = ('id', 'name', 'title', 'firstContent', 'secondContent', 'footerDescription', 'facebookLink', 'instagramLink', 'snapchatLink', 'twitterLink')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact
        fields = ('id', 'citiesAv', 'phone', 'mail', 'address', 'openHr')


class UserLoginSerializer(serializers.ModelSerializer):
    class UserLogin:
        model = models.UserLogin
        fields = 'username'
