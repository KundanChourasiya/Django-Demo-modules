from django.contrib import admin
from .models import Publisher,Author,Student,Book

class AdminPublisher(admin.ModelAdmin):
    list_display = ['pname','ploc','email']

class AdminAuthor(admin.ModelAdmin):
    list_display = ['aname','aloc','aincome']

class AdminStudent(admin.ModelAdmin):
    list_display = ['sname','sage','sfee']

class AdminBook(admin.ModelAdmin):
    list_display = ['bname','bcost']

admin.site.register(Publisher,AdminPublisher)
admin.site.register(Author,AdminAuthor)
admin.site.register(Student,AdminStudent)
admin.site.register(Book,AdminBook)