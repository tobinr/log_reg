from __future__ import unicode_literals
from django.db import models
import re


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = ("Invalid email address")
        if len(postData['fname']) < 2:
            errors['first_name'] = ("First name must be at least 2 characters")
        if len(postData['lname']) < 2:
            errors['last_name'] = ("Last name must be at least 2 characters")
        if len(postData['pw']) < 8:
            errors['password'] = ("Password must be at least 8 characters")
        if postData['pw'] != postData['pwconf']:
            errors['password_conf'] = ("Your password and confirm password do not match")
        return errors
    

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()