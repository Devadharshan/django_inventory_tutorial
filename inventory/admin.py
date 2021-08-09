from django.contrib import admin

# Register your models here.

from .models import Item

# not required just to make the admin page look customized 
class ItemAdmin(admin.ModelAdmin):
    list_display = ['title','amount']

#admin.site.register(Item) initial without customization

admin.site.register(Item,ItemAdmin)


