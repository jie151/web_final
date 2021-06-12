from django.contrib import admin
from .models import Picture, Home
# Register your models here.

class PictureAdmin(admin.ModelAdmin):
    list_display = ("title", "p_url")

class HomeAdmin(admin.ModelAdmin):
    list_display = ("title", "descript")

#Register model

admin.site.register(Picture, PictureAdmin)
admin.site.register(Home, HomeAdmin)

