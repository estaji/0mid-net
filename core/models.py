from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Create and save a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Menu(models.Model):
    """Model for main menu items"""
    title = models.CharField(max_length=50, verbose_name='Title')
    url = models.URLField(
        max_length=100,
        default='https://#',
        verbose_name='URL',
        blank=True,
    )
    order = models.IntegerField(unique=True, verbose_name='Order Number')

    DROPDOWN = 'DD'
    NORMAL = "N"
    DISABLED = 'DI'
    TYPE_CHOICES = [
        (DROPDOWN, 'Has submenu'),
        (NORMAL, "Don't have submenu"),
        (DISABLED, 'Is deactivate'),
    ]
    icon_type = models.CharField(
        max_length=2,
        choices=TYPE_CHOICES,
        default=NORMAL,
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']


class SubMenu(models.Model):
    """Model for sub menu items"""
    title = models.CharField(max_length=50, verbose_name='Title')
    url = models.URLField(
        max_length=100,
        default='https://#',
        verbose_name='URL',
        blank=True,
    )
    parent = models.ForeignKey(Menu, on_delete=models.CASCADE)
    order = models.IntegerField(unique=True, verbose_name='Order Number')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']
