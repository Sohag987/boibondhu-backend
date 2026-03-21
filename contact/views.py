from rest_framework.views import APIView 
from .models import Contact
from .serializers import ContactSerializer
from rest_framework import status 
from django.core.mail import send_mail 
from django.conf import settings 
from rest_framework.response import Response




class ContactView(APIView):
    def post(self,request):
        serializer = ContactSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()

            send_mail(

                

                subject="We receieved your Opinion-BoiBondhu",
                message=f'''

Hi {serializer.data["name"]},

Thank you for your feedback.We will reach you soon.


         

''',
from_email=settings.DEFAULT_FROM_EMAIL,
recipient_list=[serializer.data["email"]],
fail_silently=True

            
            )
            return Response({'msg':"Feedback sent successfully"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
