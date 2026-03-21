from rest_framework.pagination import PageNumberPagination 

class BookForSellPaginator(PageNumberPagination):
    page_size = 12
    page_query_param = 'size'
    max_page_size = 50 
    