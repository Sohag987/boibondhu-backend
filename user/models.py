from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



class MyCustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        if not email:
            raise ValueError('Email must be provided')
        email = self.normalize_email(email)
        user  = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user
    
    
    def create_superuser(self, email, first_name, last_name, password=None, **extra_fields):
        extra_fields['is_staff']     = True
        extra_fields['is_superuser'] = True
        return self.create_user(email, first_name, last_name, password, **extra_fields)


class MyCustomUser(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    email      = models.EmailField(unique=True)
    phone      = models.CharField(max_length=15, default=None, null=True)
    address    = models.CharField(max_length=200, default=None, null=True, blank=True)
    picture    = models.ImageField(upload_to='images/', default=None, null=True, blank=True)

    is_active    = models.BooleanField(default=True)
    is_staff     = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = MyCustomUserManager()


    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    class Meta:
        verbose_name_plural = "USER"
        ordering = ["first_name", "last_name"]

    def __str__(self):
        return self.first_name

