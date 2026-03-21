from .models import BookForLend



def getAllLendbook():
    return BookForLend.objects.all()

def get_one_lendbook(slug):
    return BookForLend.objects.get(slug=slug)