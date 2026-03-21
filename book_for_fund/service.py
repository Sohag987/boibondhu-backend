from django.core.cache import cache 
from  .selector import get_all_books ,get_one_book 

cache_key_1 = "book_list"


def get_book_with_cache():
    books = cache.get(cache_key_1)

    if not books:
        books = get_all_books()
        cache.set(cache_key_1,books,timeout=60*5)
    
    return books 

def get_one_books_with_cache(book_slug):
    cache_key_2 = f"book:{book_slug}"
    particular_book = cache.get(cache_key_2)
    

    if not particular_book:
        particular_book = get_one_book(book_slug)
        cache.set(cache_key_2,particular_book,timeout=60*5)
        # print("DB query executed")

    return particular_book 