from .selector import getAllLendbook,get_one_lendbook 
from django.core.cache import cache

ALL_BOOK_LEND_CACHE_KEY = "all_for_lend"


def getAllLendBookWithCache():
    books_for_lends = cache.get(ALL_BOOK_LEND_CACHE_KEY)

    if not books_for_lends:
        books_for_lends = getAllLendbook() 
        cache.set(ALL_BOOK_LEND_CACHE_KEY,books_for_lends,timeout=60*5)

    return books_for_lends 

def getSingleBookWithCache(slug):
    SINGLE_BOOK_LEND_KEY = f"single{slug}"

    single_book_for_lend = cache.get(SINGLE_BOOK_LEND_KEY)

    if not single_book_for_lend:
        single_book_for_lend = get_one_lendbook(slug)
        cache.set(SINGLE_BOOK_LEND_KEY,single_book_for_lend,timeout=60*5)

    return single_book_for_lend 

    
