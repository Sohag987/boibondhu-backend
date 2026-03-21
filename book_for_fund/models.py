from django.db import models
from autoslug import AutoSlugField 
from user.models import MyCustomUser 

# Create your models here.
class BookForFund(models.Model):
    donor = models.ForeignKey(MyCustomUser,related_name="donor_name",on_delete=models.CASCADE)
    book_name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    donation = models.FloatField(default=20)
    picture1 = models.ImageField(upload_to='images/',default=None,null=True,blank=True)
    picture2 = models.ImageField(upload_to='images/',default=None,null=True,blank=True)
    slug = AutoSlugField(unique=True,max_length=100,populate_from ="book_name")

    class Meta:
        verbose_name_plural = "BookForFund"
        ordering = ["book_name","author_name"]

    def __str__(self):
        return self.book_name
    



