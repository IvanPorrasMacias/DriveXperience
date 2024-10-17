from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    teléfono = models.CharField(max_length=20)
    RFC = models.CharField(max_length=13)
    usuario = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=20)

    def save(self, *args, **kwargs):
        self.usuario = (self.nombre[:3] + self.apellidos[:3] + self.teléfono[-3:]).lower()
        super(Usuario, self).save(*args, **kwargs)

    def __str__(self):
        return self.usuario

class Vehículo(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    año = models.CharField(max_length=4)
    especificaciones = models.CharField(max_length=200)
    precioLista = models.DecimalField(max_digits=10, decimal_places=2)
    enganche = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 

    def save(self, *args, **kwargs):
        self.enganche = (self.precioLista*30)/100
        super(Vehículo, self).save(*args, **kwargs)

    def __str__(self):
        return self.marca + ' - ' + self.modelo


class Plan(models.Model):
    mensualidades = models.IntegerField()
    interes = models.DecimalField(max_digits=5,decimal_places=2,default=5.00)
    comisionApertura = models.DecimalField(max_digits=10,decimal_places=2,default=5000.00)
    seguro = models.DecimalField(max_digits=10,decimal_places=2,default=12000.00)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    vehículo = models.ForeignKey(Vehículo, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        interesMensual = (self.vehículo.precioLista / self.mensualidades) * self.interes
        interesTotal = interesMensual * self.mensualidades
        self.costoTotal = self.vehículo.precioLista + interesTotal
        super(Plan, self).save(*args, **kwargs)

class Promociones(models.Model):
    descuento = models.IntegerField()
    vehículo = models.ForeignKey(Vehículo, on_delete=models.CASCADE)