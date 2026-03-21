from .selector import getAllBook,getSingleBook 
from django.core.cache import cache 

ALL_SELL_BOOK_KEY = "sell_book_key"


def getAllSellBook():

    books = cache.get(ALL_SELL_BOOK_KEY)

    if not books:
        books = getAllBook()
        cache.set(ALL_SELL_BOOK_KEY,books,timeout=60*5)

    return books 

def getSingleSellBook(slug):
    SINGLE_SELL_BOOK_KEY = f"Single_sell_{slug}"

    book = cache.get(SINGLE_SELL_BOOK_KEY)
    
    if not book:
        book = getSingleBook(slug)
        cache.set(SINGLE_SELL_BOOK_KEY,book,timeout=60*5)

    return book 
        

    