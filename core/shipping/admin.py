from django.contrib import admin
from shipping.models import Client,Product,Driver,Container,Custom


# Register your models here.
admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Driver)
admin.site.register(Container)
admin.site.register(Custom)