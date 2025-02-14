from django.contrib import admin
from .models import Student,Course

class AdminStudent(admin.ModelAdmin):
    list_display = ['sno','sname','slo']

class AdminCourse(admin.ModelAdmin):
    list_display = ['cno','cname','cfee']

admin.site.register(Student,AdminStudent)
admin.site.register(Course,AdminCourse)
