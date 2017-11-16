from django.db import models
from django.conf import settings
"""Account models."""
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Custom user model"""
    USER_TYPES_CHOICES = (
        ('S', 'STUDENT'),
        ('T', 'TEACHER'),
        ('A', 'ADMINISTRATOR'),
    )
    PAYMENT_STATUS_CHOICES = (
        ('NPR', 'NO PAYMENT REQUIRED'),
        ('OK', 'PAYMENT OK'),
        ('PND', 'PENDING'),
        ('CLD', 'CANCELED'),
    )
    GENDER_CHOICES = (
        ('M', 'MALE'),
        ('F', 'FEMALE'),
    )
    user_type = models.CharField(max_length=1, choices=USER_TYPES_CHOICES)
    avatar = models.ImageField(upload_to='user_avatar', null=True,
                               blank=True,
                               default='{}'.format(settings.USER_AVATAR_DIR))
    social_number = models.CharField(max_length=20, blank=False)
    address = models.CharField(max_length=255, blank=True)
    payment_status = models.CharField(
        max_length=3,
        choices=PAYMENT_STATUS_CHOICES,
        default='NPR'
    )
    phone_number = models.CharField(max_length=20, blank=False)
    gender = models.CharField(
        max_length=1,
        blank=False,
        choices=GENDER_CHOICES
    )
