from django.db import models
from tinymce.models import HTMLField
from user.models import MyCustomUser 
from autoslug import AutoSlugField 

# Create your models here.

class BookForSell(models.Model):
    seller = models.ForeignKey(MyCustomUser,related_name="seller_name",on_delete=models.CASCADE)
    book_name = models.CharField(max_length=40)
    author_name = models.CharField(max_length=50)
    description = HTMLField()
    price = models.FloatField(default=0.00)
    picture1 = models.ImageField(upload_to='images/',default=None ,null=True,blank=True)
    picture2 = models.ImageField(upload_to='images/',default=None,null=True,blank=True)
    picture3 = models.ImageField(upload_to='images/',default=None,null=True,blank=True)
    slug = AutoSlugField(populate_from="book_name",unique=True)

    class Meta:
        verbose_name_plural = "BookForSell"
        ordering = ['book_name','author_name']

    def __str__(self):
        return self.book_name





