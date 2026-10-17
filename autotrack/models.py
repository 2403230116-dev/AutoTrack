from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=128)

    def __str__(self):
        return self.nombre  
    
class Vehiculo(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año = models.IntegerField()
    color = models.CharField(max_length=30)
    kilometraje = models.IntegerField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.marca} {self.modelo}"
    
class TipoMantenimiento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    
class Taller(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre
    
class Mantenimiento(models.Model):
    fecha = models.DateField()
    kilometraje = models.IntegerField()
    descripcion = models.TextField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoMantenimiento, on_delete=models.CASCADE)
    taller = models.ForeignKey(Taller, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.vehiculo} - {self.fecha}"
    
class Refaccion(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    
class MantenimientoRefaccion(models.Model):
    mantenimiento = models.ForeignKey(Mantenimiento, on_delete=models.CASCADE)
    refaccion = models.ForeignKey(Refaccion, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.mantenimiento} - {self.refaccion}"
    
class Recordatorio(models.Model):
    servicio = models.CharField(max_length=100)
    fecha_proxima = models.DateField()
    kilometraje_proximo = models.IntegerField()
    estado = models.CharField(max_length=30)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)

    def __str__(self):
        return self.servicio