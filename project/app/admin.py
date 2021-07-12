from django.contrib import admin
from .models import Profile



@admin.register(Profile)
class InfoAdmin(admin.ModelAdmin):
    list_display = ['user','address','phoneNo','level','registeredAt']
