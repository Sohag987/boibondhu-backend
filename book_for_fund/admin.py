from django.contrib import admin
from .models import BookForFund 

# Register your models here.
@admin.register(BookForFund)
class BookForFundAdmin(admin.ModelAdmin):
    list_display = ["book_name","author_name","donor","donation","slug"]

