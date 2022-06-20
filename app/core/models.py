"""
Models for db
"""

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin)
import psycopg2


# Create your models here.
class UserManager(BaseUserManager):
    """To manage user in the db"""
    def create_user(self, email, password=None, **extra_fields):
        """Create save and return new user"""
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user 


class User(AbstractBaseUser,PermissionsMixin):
    """users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()


    USERNAME_FIELD = 'email'