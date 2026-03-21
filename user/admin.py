from django.contrib import admin
from .models import MyCustomUser

# Register your models here.
@admin.register(MyCustomUser)
class MyCustomUserAdmin(admin.ModelAdmin):
    list_display=["first_name","last_name","email","phone"]
    





