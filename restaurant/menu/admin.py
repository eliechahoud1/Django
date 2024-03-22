from django.contrib import admin

from .models import categories,items

admin.site.register(categories)
admin.site.register(items)