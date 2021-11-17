from django.contrib import admin
from .models import Student, User, Profile, Video
# Register your models here.
admin.site.register(Video)
admin.site.register(Profile)
admin.site.register(Student)
admin.site.register(User)