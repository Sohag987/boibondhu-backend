from rest_framework import serializers
from .models import MyCustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = MyCustomUser
        fields = ['id', 'first_name', 'last_name', 'email',
                  'password', 'phone', 'address', 'picture']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return MyCustomUser.objects.create_user(**validated_data)
