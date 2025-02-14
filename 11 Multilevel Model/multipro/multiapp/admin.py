from django.contrib import admin
from .models import Student,Emp,Customer

class AdminStudent(admin.ModelAdmin):
    list_display = ['sname', 'sfee','email']

class AdminEmp(admin.ModelAdmin):
    list_display = ['ename','esal']

class AdminCustomer(admin.ModelAdmin):
    list_display = ['cname','csale']

admin.site.register(Student,AdminStudent)
admin.site.register(Emp,AdminEmp)
admin.site.register(Customer,AdminCustomer)