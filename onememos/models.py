from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,
    PermissionsMixin)
 

# Create your models here.

class OneMemo(models.Model):
    content = models.CharField(max_length=100)
    writer = models.CharField(max_length=100,)
    update_Date = models.DateTimeField(auto_now=True, null=True)
    write_date = models.DateTimeField(auto_now_add=True)
    
    

 
class UserManager(BaseUserManager):
    def create_user(self, email, nickname, password=None):
        if not email:
            raise ValueError('Users must have an email address')
 
        user = self.model(
            email=UserManager.normalize_email(email),
            nickname=nickname,
        )
 
        user.set_password(password)
        user.save(using=self._db)
        return user
 
    def create_superuser(self, email, nickname, password):
        u = self.create_user(email=email,
                             nickname=nickname,
                             password=password,
                             )
        u.is_admin = True
        u.save(using=self._db)
        return u
 
 
class Users(AbstractBaseUser,  PermissionsMixin):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    nickname = models.CharField(
        max_length=10, 
        blank=False, 
        unique=True, 
        default='')
 
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
 
    objects = UserManager()
 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin    
    

# class Users(AbstractUser):
#     pass

