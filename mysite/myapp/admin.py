from django.contrib import admin
from .models import *
# Register your models here.
class invitmadmin(admin.ModelAdmin):
    list_display = ['id', 'inv', 'item']
admin.site.register(item)
admin.site.register(invoice)
admin.site.register(invitem, invitmadmin)