from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from .validators import validate_file_extension
from vote.models import VoteModel
from django.utils.html import escape, mark_safe
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
# Create your models here

class User(AbstractUser):
    created = models.DateTimeField('created', auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

class Profile(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHERS = 'O'
    PREFER_TO_NOT_SAY = 'P'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHERS, 'Others'),
        (PREFER_TO_NOT_SAY, 'Prefer to not say')
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null = False)
    first_name = models.CharField(max_length=50, unique=False)
    last_name = models.CharField(max_length=50, unique=False)
    gender = models.CharField(
        max_length=2,
        choices=GENDER_CHOICES,
        default=None,
        null=True,
    )
    date_of_birth = models.DateField(verbose_name='date of birth', null = True)
    nationality = CountryField()
    profile_picture = models.ImageField(
        upload_to='pfp/%Y/%m/%d/', blank=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        '''
        to set table name in database
        '''
        db_table = "profile"

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
post_save.connect(create_profile, sender=User)


def delete_user(sender, instance=None, **kwargs):
    try:
        instance.user
    except User.DoesNotExist:
        pass
    else:
        instance.user.delete()
post_delete.connect(delete_user, sender=Profile)

class Video(VoteModel, models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User,
                              related_name='videos',
                              on_delete=models.CASCADE)
    submitted = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    video_section = models.ForeignKey('categories.Category', on_delete=models.CASCADE)
    video_file = models.FileField(
        upload_to='uploads/%Y/%m/%d/',
        validators=[validate_file_extension, ],
    )


class Student(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    interest = models.ForeignKey(
        'categories.Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
