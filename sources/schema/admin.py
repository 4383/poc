from django.contrib import admin
from schema.models import Global
from schema.models import UserDefined
from schema.models import Entry
from schema.models import Zone
from schema.models import Schema
from schema.models import Warehouse

# Register your models here.
admin.site.register(Global)
admin.site.register(UserDefined)
admin.site.register(Entry)
admin.site.register(Zone)
admin.site.register(Schema)
admin.site.register(Warehouse)
