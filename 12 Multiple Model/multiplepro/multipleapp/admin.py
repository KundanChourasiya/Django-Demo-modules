from django.contrib import admin
from .models import Emp,Customer,Student

class AdminEmp(admin.ModelAdmin):
    list_display = ['eid','eno','ename','esal']

class AdminCustomer(admin.ModelAdmin):
    list_display = ['cid','cno', 'cname','csale']

class AdminStudent(admin.ModelAdmin):
    list_display = ['sno','sname','sfee']

admin.site.register(Emp,AdminEmp)
admin.site.register(Customer,AdminCustomer)
admin.site.register(Student,AdminStudent)
