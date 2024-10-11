# admin_app/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Admin

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'
        read_only_fields = ('user',)

    def create(self, validated_data):
        # Create User instance
        user_data = {
            'username': validated_data['a_email'],  # Using email as username
            'email': validated_data['a_email'],
            'password': 'your_default_password'  # Use a secure way to handle passwords
        }
        user = User(**user_data)
        user.set_password(user_data['password'])  # Hash the password
        user.save()

        # Create Admin instance
        admin = Admin.objects.create(user=user, **validated_data)
        return admin
