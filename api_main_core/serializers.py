from rest_framework import serializers
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


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'


class TipoMantenimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMantenimiento
        fields = '__all__'


class TallerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taller
        fields = '__all__'


class MantenimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mantenimiento
        fields = '__all__'


class RefaccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refaccion
        fields = '__all__'


class MantenimientoRefaccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MantenimientoRefaccion
        fields = '__all__'


class RecordatorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recordatorio
        fields = '__all__'