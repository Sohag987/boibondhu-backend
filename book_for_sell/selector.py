from .models import BookForSell 


def getAllBook():
    return BookForSell.objects.all()

def getSingleBook(slug):
    return BookForSell.objects.get(slug=slug)

