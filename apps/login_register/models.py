from __future__ import unicode_literals
from django.db import models

import re
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def login(self, post_obj):
        username = post_obj['username']
        pw = post_obj['pw'].encode()

        validation_obj = {
            'errors': []
        }

        try:
            user = User.objects.get(username=username)
        except:
            msg = "Username address doesn't exist. Please register."
            validation_obj['errors'].append(msg)
            return validation_obj
        if bcrypt.hashpw(pw, user.password.encode()) == user.password.encode():
            return {'user': user.full_name}
        else:
            msg = "Invalid password"
            validation_obj['errors'].append(msg)
            return validation_obj

    def register(self, post_obj):
        full_name = post_obj['full_name']
        username = post_obj['username']
        hire_date = post_obj['hire_date']
        pw = post_obj['pw']
        confirm_pw = post_obj['confirm_pw']

        validation_obj = {
            'errors': []
        }

        if not full_name or not username:
            msg = "You must input a name and username"
            validation_obj['errors'].append(msg)
        try:
            User.objects.get(username=username)
            msg = "Username already exists"
            validation_obj['errors'].append(msg)
        except:
            pass
        if len(full_name) < 3 or len(username) < 3:
            msg = "Name and Username must be at least 3 characters"
            validation_obj['errors'].append(msg)
        if len(pw) < 8:
            msg = "Password must be at least 8 characters"
            validation_obj['errors'].append(msg)
        if pw != confirm_pw:
            msg = "Passwords must match"
            validation_obj['errors'].append(msg)

        if validation_obj['errors']:
            return validation_obj
        else:
            return {'user': full_name}


class User(models.Model):
    full_name = models.CharField(max_length=65)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=65)
    hire_date = models.DateTimeField(default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
