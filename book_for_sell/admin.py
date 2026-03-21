from django.contrib import admin
from .models import BookForSell

# Register your models here.

@admin.register(BookForSell)
class Book_for_sell_admin(admin.ModelAdmin):
    list_display=["book_name","author_name","seller","price","slug"]