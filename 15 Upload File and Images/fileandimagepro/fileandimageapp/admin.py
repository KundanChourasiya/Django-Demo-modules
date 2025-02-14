from django.contrib import admin
from .models import Student

class AdminStudent(admin.ModelAdmin):
    list_display = ['sno','sname','sloc','image','profile']

admin.site.register(Student,AdminStudent)