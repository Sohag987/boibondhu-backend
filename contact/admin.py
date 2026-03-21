from django.contrib import admin
from .models import Contact

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','created_at','is_read']
    list_filter = ['is_read','created_at']
    search_fields = ['name','email','subject']
