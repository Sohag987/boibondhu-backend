from django.contrib import admin
from .models import BookForLend 

# Register your models here.

@admin.register(BookForLend)
class BookForLendAdmin(admin.ModelAdmin):
    list_display=["book_name","author_name","lender","duration","slug"]



