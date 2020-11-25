from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Shop)
admin.site.register(Listing)
admin.site.register(Rating)
admin.site.register(Cart)
