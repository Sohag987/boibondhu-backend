from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .service import get_book_with_cache,get_one_books_with_cache
from .serializers import BoookForFundSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated 
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter 
from .pagination import BookForLendPagination 



class BookForFundListView(ListCreateAPIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]
    def get_queryset(self):
        return get_book_with_cache() 
    
    serializer_class = BoookForFundSerializer 
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields = ["book_name","author_name"]
    filterset_fields = ["book_name","author_name"]
    pagination_class = BookForLendPagination 

    def perform_create(self, serializer):
      serializer.save(donor=self.request.user)



class SingleBookForFund(RetrieveUpdateDestroyAPIView):
     def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]
     lookup_field = 'slug'
     serializer_class = BoookForFundSerializer
     def get_object(self):
         slug = self.kwargs['slug']
         return get_one_books_with_cache(slug)
     
     def perform_update(self, serializer):
         if serializer.instance.donor != self.request.user:
             return Response({'error': 'You are not the donor of this book.'}, status=403)
         serializer.save(donor=self.request.user)

     def perform_destroy(self, instance):
         if instance.donor != self.request.user:
             return Response({'error': 'You are not the donor of this book.'}, status=403)
         instance.delete()
         
    

