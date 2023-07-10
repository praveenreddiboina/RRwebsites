from django.db import models
# from django.db import models
# from .category import Category
class Category(models.Model):
    name= models.CharField(max_length=50)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name
class Products(models.Model):
    name = models.CharField(max_length=60)
    price= models.IntegerField(default=0)
    category= models.ForeignKey(Category,on_delete=models.CASCADE,default=1 )
    description= models.CharField(max_length=250, default='', blank=True, null= True)
    image= models.ImageField(upload_to='pics')

    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter(id__in=ids)
    @staticmethod
    def get_all_products():
        return Products.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Products.objects.filter(category=category_id)
        else:
            return Products.get_all_products()
# Create your models here.
# class products(models.Model):
#     name = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='pics')
#     description = models.TextField()
#     price = models.IntegerField()

