from django.db import models

# Create your models here.


class Category(models.Model):

    category_name = models.CharField('Category name',max_length=50, null=False, blank=False)

    def __str__(self) -> str:
        return self.category_name
    
    class Meta:
        verbose_name_plural='Categories'

class Product(models.Model):
    product_name = models.CharField('Product name',max_length=250, null=False, blank=False)
    product_value=models.DecimalField(max_digits=10 , decimal_places=2,null = False, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='category', null=True,blank=True)
    ingredients = models.CharField('Ingredients',max_length=250, null=False, blank=False)
    active = models.BooleanField(null=True, default=True)
    imagen = models.ImageField(upload_to = "product" , null= True)

    def __str__(self) -> str:
        return self.product_name
    
    class Meta:
        verbose_name_plural='Products'