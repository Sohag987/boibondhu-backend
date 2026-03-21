from .models import BookForFund 

def get_all_books():
    return BookForFund.objects.all()

def get_one_book(slug):
    return BookForFund.objects.get(slug=slug)