from rest_framework import serializers 
from .models import BookForFund 
from user.serializers import UserSerializer

class BoookForFundSerializer(serializers.ModelSerializer):
    
    donor = UserSerializer(read_only=True)
    class Meta:
        model = BookForFund
        fields = '__all__'
        read_only_fields = ['slug','donor']