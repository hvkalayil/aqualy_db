from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','uid','profileImage']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name','price','productType','isAllowed']

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['id','name','revenue']

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['id','product_id','shop_id','color','size','discount','accessories']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id','listing_id','review','stars']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id','user_id','listing_id']
