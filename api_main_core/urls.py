from rest_framework.routers import DefaultRouter
from .views import (
    UsuarioViewSet,
    VehiculoViewSet,
    TipoMantenimientoViewSet,
    TallerViewSet,
    MantenimientoViewSet,
    RefaccionViewSet,
    MantenimientoRefaccionViewSet,
    RecordatorioViewSet
)

router = DefaultRouter()

router.register('usuarios', UsuarioViewSet)
router.register('vehiculos', VehiculoViewSet)
router.register('tipos-mantenimiento', TipoMantenimientoViewSet)
router.register('talleres', TallerViewSet)
router.register('mantenimientos', MantenimientoViewSet)
router.register('refacciones', RefaccionViewSet)
router.register('mantenimiento-refacciones', MantenimientoRefaccionViewSet)
router.register('recordatorios', RecordatorioViewSet)

urlpatterns = router.urls