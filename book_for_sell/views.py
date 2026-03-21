from .service import getAllSellBook,getSingleSellBook 
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView 

from .serializers import BookForSellserializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.filters import SearchFilter 
from django_filters.rest_framework import DjangoFilterBackend 
from .pagination import BookForSellPaginator 
from rest_framework.response import Response



class AllBookSellView(ListCreateAPIView):
    def get_permissions(self):
        if self.request.method  == 'GET':
             return  [AllowAny()]
        
        return  [IsAuthenticated()]
    
    def get_queryset(self):
        return getAllSellBook()
    filter_backends = [SearchFilter,DjangoFilterBackend]
    filterset_fields = ["book_name","author_name"]
    search_fields = ["book_name","author_name"]
    serializer_class = BookForSellserializer 
    pagination_class = BookForSellPaginator


    def perform_create(self, serializer):
      if serializer.instance.seller != self.request.user:
          return Response({'error': 'You are not the seller of this book.'}, status=403)
      serializer.save(seller=self.request.user)


class SingleBookSellView(RetrieveUpdateDestroyAPIView):
     def get_permissions(self):
        if self.request.method  == 'GET':
             return  [AllowAny()]
        
        return  [IsAuthenticated()]
     serializer_class = BookForSellserializer 
     lookup_field = 'slug'
     def get_object(self):
         slug = self.kwargs['slug']
          
         return getSingleSellBook(slug)
     
     def perform_update(self, serializer):
         if serializer.instance.seller != self.request.user:
             return Response({'error': 'You are not the seller of this book.'}, status=403)
         serializer.save(seller=self.request.user)
     def perform_destroy(self, instance):
         if instance.seller != self.request.user:
             return Response({'error': 'You are not the seller of this book.'}, status=403)
         instance.delete()
     
     
    


   
   