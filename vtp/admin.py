from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Network)
admin.site.register(DataType)
admin.site.register(ReqData)
