from .models import BookForSell 
from rest_framework import serializers
from user.serializers import UserSerializer

class BookForSellserializer(serializers.ModelSerializer):
    
    seller = UserSerializer(read_only=True)

    class Meta:
        model = BookForSell
        fields = '__all__'
        read_only_fields = ['seller','slug']
