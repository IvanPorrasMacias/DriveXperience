import requests
from django.db import models
from django.contrib import messages
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    direccion = models.CharField(max_length=100)
    teléfono = models.CharField(max_length=20)
    RFC = models.CharField(max_length=13)

    def save(self, *args, **kwargs):
        self.username = (self.first_name[:3] + self.last_name[:3] + self.teléfono[-3:]).lower()
        super(Usuario, self).save(*args, **kwargs)

    def __str__(self):
        return self.username
    pass

class Vehículo(models.Model):
    marca = models.CharField(max_length=30, null=False)
    modelo = models.CharField(max_length=30, null=False)
    año = models.CharField(max_length=4, null=False)
    transmision = models.CharField(max_length=1, null=True, blank=True)
    tipoCombustible = models.CharField(max_length=11, null=True, blank=True)
    traccion = models.CharField(max_length=3, null=True, blank=True)
    cilindros = models.IntegerField(null=True, blank=True)
    precioLista = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    interesAnual = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    interesMensual = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    fotoLateral = models.ImageField(default='acura.png', upload_to='autosTresCuartos/') 

    def save(self, *args, **kwargs):
        self.interesAnual = (self.precioLista*8)/100
        self.interesMensual = self.interesAnual/12
        if not self.transmision:
            url = "https://api.api-ninjas.com/v1/cars"
            headers = {"X-Api-Key": "rinSB3ooRmJU9D2zt70Nww==oARMQxF6jZwoGlGs"}
            params = {
                "make": self.marca,
                "model": self.modelo,
                "year": self.año
            }
            try:
                response = requests.get(url, headers=headers, params=params)
                if response.status_code == 200:
                    data = response.json()
                    if data:
                        self.transmision = data[0].get("transmission")
                        self.tipoCombustible = data[0].get("fuel_type")
                        self.traccion = data[0].get("drive")
                        self.cilindros = data[0].get("cylinders")
                    else:
                        print(f"No se encontró información en la API para {self.marca} {self.modelo} {self.año}.")
                        self.transmision = "X"
                        self.tipoCombustible = "X"
                        self.traccion = "X"
                        self.cilindros = "X"
                else:
                    print(f"Error al consultar la API: {response.status_code}")
            except requests.RequestException as e:
                print(f"Error al realizar la solicitud a la API: {e}")
        else:
            print("Algunos valores ya definidos, por favor bórrelos si desea consultar la API")
        super(Vehículo, self).save(*args, **kwargs)

    def getTransmision(self):
        if self.transmision == "a":
            return "Automática"
        elif self.transmision == "m":
            return "Manual"
        return ""
    
    def getTipoCombustible(self):
        if self.tipoCombustible == "gas":
            return "Gasolina"
        elif self.tipoCombustible == "diesel":
            return "Diesel"
        elif self.tipoCombustible == "electricity":
            return "Eléctrico"
        return ""
    
    def getTraccion(self):
        if self.traccion == "fwd":
            return "Delantera"
        elif self.traccion == "rwd":
            return "Trasera"
        elif self.traccion == "4wd":
            return "4x4"
        return ""

    def __str__(self):
        return self.marca + ' - ' + self.modelo


class Plan(models.Model):
    mensualidades = models.DecimalField(max_digits=10, decimal_places=2)
    plazo = models.IntegerField()
    montoAFinanciar = models.DecimalField(max_digits=10, decimal_places=2)
    pagoInicial = models.DecimalField(max_digits=10, decimal_places=2)
    seguroContado = models.DecimalField(max_digits=10, decimal_places=2)
    tazaInteres = models.DecimalField(max_digits=5,decimal_places=2,default=8.00)
    comisionApertura = models.DecimalField(max_digits=10,decimal_places=2,default=15000.00)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    vehículo = models.ForeignKey(Vehículo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} - {self.usuario.first_name} - {self.vehículo.marca} {self.vehículo.modelo}"

class Promociones(models.Model):
    descuento = models.IntegerField()
    vehículo = models.ForeignKey(Vehículo, on_delete=models.CASCADE)