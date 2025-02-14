from django.contrib import admin
from .models import Student,StudentProxy

class AdminStudent(admin.ModelAdmin):
    list_display = ['sno','sname','sloc']

class AdminStudentProxy(admin.ModelAdmin):
    list_display = ['sno','sname','sloc']

admin.site.register(Student,AdminStudent)
admin.site.register(StudentProxy,AdminStudentProxy)
