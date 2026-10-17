from rest_framework import viewsets

from autotrack.models import (
    Usuario,
    Vehiculo,
    TipoMantenimiento,
    Taller,
    Mantenimiento,
    Refaccion,
    MantenimientoRefaccion,
    Recordatorio
)

from .serializers import (
    UsuarioSerializer,
    VehiculoSerializer,
    TipoMantenimientoSerializer,
    TallerSerializer,
    MantenimientoSerializer,
    RefaccionSerializer,
    MantenimientoRefaccionSerializer,
    RecordatorioSerializer
)


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer


class TipoMantenimientoViewSet(viewsets.ModelViewSet):
    queryset = TipoMantenimiento.objects.all()
    serializer_class = TipoMantenimientoSerializer


class TallerViewSet(viewsets.ModelViewSet):
    queryset = Taller.objects.all()
    serializer_class = TallerSerializer


class MantenimientoViewSet(viewsets.ModelViewSet):
    queryset = Mantenimiento.objects.all()
    serializer_class = MantenimientoSerializer


class RefaccionViewSet(viewsets.ModelViewSet):
    queryset = Refaccion.objects.all()
    serializer_class = RefaccionSerializer


class MantenimientoRefaccionViewSet(viewsets.ModelViewSet):
    queryset = MantenimientoRefaccion.objects.all()
    serializer_class = MantenimientoRefaccionSerializer


class RecordatorioViewSet(viewsets.ModelViewSet):
    queryset = Recordatorio.objects.all()
    serializer_class = RecordatorioSerializer