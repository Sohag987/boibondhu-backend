from rest_framework import serializers
from .models import BookForLend 
from user.serializers import UserSerializer 

class BookForLendSerializer(serializers.ModelSerializer):
    lender = UserSerializer(read_only=True)

    class Meta:
      model = BookForLend
      fields = '__all__'
      read_only_fields = ['slug','lender']




