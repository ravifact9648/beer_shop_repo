from django.contrib import admin

# Register your models here.
from app.models import Beer

class BeerAdmin(admin.ModelAdmin):
    list_display=['name','taste','color','price']

admin.site.register(Beer,BeerAdmin)
