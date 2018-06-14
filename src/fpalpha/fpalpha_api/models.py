from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """Helps Django work with our custom user model"""
    def create_user(self, email, name, password=None):   #Create user object
        if not email:
            raise ValueError('Users must have an email address')
        email=self.normalize_emanil(email)
        user=self.model(email=email, name=name)
        user.set_password(password) #set_password: encripts the password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user=self.create_user(email,name,password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Represent User Profile inside our system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']

    def get_full_name(self):
        return self.name
    def get_short_name(self):
        return self.name

    def __str__(self):
        """Django uses this when it needs to convert the object to string"""
        return self.email
