from django.contrib import admin

# Register your models here.
from vtp.models import Datatype, Network, Dataplan,  Permode

admin.site.register(Network)
admin.site.register(Datatype)
admin.site.register(Dataplan)
admin.site.register(Permode)