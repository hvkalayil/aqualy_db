from django.db import models

def nameFile(instance, filename):
    return '/'.join(['images', str(instance.name), filename])

# Create your models here.
class User(models.Model):
    uid = models.CharField(max_length=256)
    def __str__(self):
        return self.uid

class Product(models.Model):
    PRODUCT_TYPES = (
        ('F' , 'Fish'),
        ('A' , 'Accessory'),
    )
    name = models.CharField(max_length=256)
    price = models.IntegerField()
    productType = models.CharField(choices=PRODUCT_TYPES,max_length=1)
    isAllowed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Shop(models.Model):
    name = models.CharField(max_length=256)
    revenue = models.FloatField()

    def __str__(self):
        return self.name

class Listing(models.Model):
    product_id = models.ForeignKey(Product,on_delete=models.DO_NOTHING)
    shop_id = models.ForeignKey(Shop,on_delete=models.DO_NOTHING)
    color = models.CharField(max_length=256)
    size = models.CharField(max_length=256)
    discount = models.IntegerField()
    accessories = models.ForeignKey(Product,on_delete=models.DO_NOTHING,related_name='accessory')

    def __str__(self):
        return self.product_id + ' sold by ' + self.shop_id

class Rating(models.Model):
    listing_id = models.ForeignKey(Listing,on_delete=models.DO_NOTHING)
    review = models.CharField(max_length=512)
    stars = models.IntegerField()

    def __str__(self):
        return self.stars

class Cart(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    listing_id = models.ForeignKey(Listing,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.user_id



