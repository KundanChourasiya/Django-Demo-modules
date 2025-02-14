from django.contrib import admin
from .models import ProductData

class AdminProductData(admin.ModelAdmin):
    list_display = ['productname','productcost','productcolor','productdesc']

admin.site.register(ProductData,AdminProductData)
