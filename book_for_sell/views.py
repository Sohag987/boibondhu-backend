from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from book_for_sell.serializers import BookForSellserializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.filters import SearchFilter
from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import BookForSellPaginator
from .models import BookForSell
from django.core.cache import cache 




class AllBookSellView(ListCreateAPIView):
    serializer_class   = BookForSellserializer
    pagination_class   = BookForSellPaginator
    filter_backends    = [SearchFilter, DjangoFilterBackend]
    filterset_fields   = ['book_name', 'author_name']
    search_fields      = ['book_name', 'author_name']
    def get_queryset(self):
        cached_key = 'all_books_sell'
        queryset = cache.get('all_books_sell')
        if not queryset:
            queryset = BookForSell.objects.all()
            cache.set('all_books_sell', queryset, timeout=60*15)  # Cache for 15 minutes
        return queryset

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]

    

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)


class SingleBookSellView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookForSellserializer
    lookup_field     = 'slug'
    single_cache_key = 'book_sell_{}'  # 

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        cache_key = self.single_cache_key.format(slug)
        book = cache.get(cache_key)
        if not book:
            book = BookForSell.objects.filter(slug=slug).first()
            if book:
                cache.set(cache_key, book, timeout=60*15)  # Cache for 15 minutes
        return BookForSell.objects.filter(slug=slug)

    def perform_update(self, serializer):
        if serializer.instance.seller != self.request.user:
            raise PermissionDenied('You can only update your own books')
        serializer.save()

    def perform_destroy(self, instance):
        if instance.seller != self.request.user:
            raise PermissionDenied('You can only delete your own books')
        instance.delete()