from django.contrib import admin

# Register your models here.
from vtp.models import Datatype, Network, Permode

admin.site.register(Network)
admin.site.register(Datatype)
admin.site.register(Permode)