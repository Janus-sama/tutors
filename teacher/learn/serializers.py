from .models import User, Profile
from rest_framework import serializers
from teacher.settings import AUTH_USER_MODEL
from django_countries.serializers import CountryFieldMixin

class ProfileSerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'first_name',
            'last_name',
            'gender',
            'date_of_birth',
            'nationality',
            'profile_picture',)


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True)
    username = AUTH_USER_MODEL

    class Meta:
        model = User
        fields = ('url', 'username', 'profile', 'created', )
        read_only_field = 'username',

    def create(self, validated_data):

        profile_data = validated_data.pop('profile')
        # create profile
        profile = Profile.objects.create(
            user=User,
            first_name=profile_data['first_name'],
            last_name=profile_data['last_name'],
            gender=profile_data['gender'],
            date_of_birth=profile_data['date_of_birth'],
            nationality=profile_data['nationality'],
            profile_picture=profile_data['profile_picture'],
        )

        return User

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        # * AccountProfile Info
        profile.first_name = profile_data.get(
            'first_name', profile.first_name)
        profile.last_name = profile_data.get(
            'last_name', profile.last_name)
        profile.gender = profile_data.get(
            'gender', profile.gender)
        profile.date_of_birth = profile_data.get(
            'date_of_birth', profile.date_of_birth)
        profile.nationality = profile_data.get(
           'nationality', profile.nationality)
        profile.profile_picture = profile_data.get(
            'profile_picture', profile.profile_picture)
        profile.save()
        
        return instance
