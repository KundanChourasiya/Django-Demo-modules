from django.contrib import admin
from genericviews.models import person

class AdminPerson(admin.ModelAdmin):
    list_display = ['name','desc']

admin.sites.register(person,AdminPerson)

