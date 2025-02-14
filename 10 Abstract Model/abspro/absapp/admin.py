from django.contrib import admin
from .models import CommonInfo,Student,Emp,Customer

class AdminStudent(admin.ModelAdmin):
    list_display = ['name','loc','fee']

class AdminEmp(admin.ModelAdmin):
    list_display = ['name', 'loc', 'sal']

class AdminCustomer(admin.ModelAdmin):
    list_display = ['name', 'loc', 'saleamt']

admin.site.register(Student,AdminStudent)
admin.site.register(Emp,AdminEmp)
admin.site.register(Customer,AdminCustomer)