from django.contrib import admin


# Register your models here.
from .models import items,Cart
admin.site.register(items)
admin.site.register(Cart)



