from django.contrib import admin
from .models import *

admin.site.register(Usuario)
admin.site.register(Vehiculo)
admin.site.register(TipoMantenimiento)
admin.site.register(Taller)
admin.site.register(Mantenimiento)
admin.site.register(Refaccion)
admin.site.register(MantenimientoRefaccion)
admin.site.register(Recordatorio)