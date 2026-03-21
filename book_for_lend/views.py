
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView 
from .serializers import BookForLendSerializer
from .service import getAllLendBookWithCache,getSingleBookWithCache
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from .pagination import BookForLendPagination  
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter  
from rest_framework.response import Response


class AllBookForLendView(ListCreateAPIView):
    def get_queryset(self):
        return getAllLendBookWithCache()
    
    serializer_class = BookForLendSerializer 
    def get_permissions(self):
        if self.request.method  in ['POST','PUT','GET']:
            return [AllowAny()]
        return [IsAuthenticated()]
    pagination_class = BookForLendPagination 
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_fields = ["book_name","author_name"]
    search_fields  = ["book_name","author_name"]

    def perform_create(self, serializer):
        return serializer.save(lender=self.request.user)

class SingleBookLendView(RetrieveUpdateDestroyAPIView):
    

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        elif self.request.method in ['PUT','PATCH','POST','DELETE']:
            return [IsAuthenticated()]
        
    lookup_field = 'slug'
    serializer_class = BookForLendSerializer
        

    def get_object(self):
        slug  = self.kwargs['slug']
        return getSingleBookWithCache(slug)
    
    def perform_update(self, serializer):
        if serializer.instance.lender != self.request.user:
            return Response({'error': 'You are not the lender of this book.'}, status=403)
        serializer.save(lender=self.request.user)

    def perform_destroy(self, instance):
        if instance.lender != self.request.user:
            return Response({'error': 'You are not the lender of this book.'}, status=403)
        instance.delete()

    
        

        
    

    

    



        
        
        