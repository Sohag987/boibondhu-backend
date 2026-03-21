from django.db import models
from autoslug import AutoSlugField 
from user.models import MyCustomUser
# Create your models here.

class BookForLend(models.Model):
    lender = models.ForeignKey(MyCustomUser,related_name="lender_name",on_delete=models.CASCADE)
    book_name = models.CharField(max_length=50)
    author_name = models.CharField(max_length=50)
    duration = models.IntegerField(default=30)
    picture1 = models.ImageField(upload_to='images/',default=None,null=True,blank=True)
    picture2 = models.ImageField(upload_to='images/',default=None,null=True,blank=True)
    slug = AutoSlugField(populate_from ='book_name',unique =True,max_length=200)


    class Meta:
        verbose_name_plural = "BookForLend"
        ordering = ["book_name","author_name"]

    def __str__(self):
        return self.book_name
    
    
