from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .models import Usuario,Vehículo
from .serializers import UsuarioSerializer,VehículoSerializer
#from .forms import RegistroForm

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class VehículoViewSet(viewsets.ModelViewSet):
    queryset = Vehículo.objects.all()
    serializer_class = VehículoSerializer

def IndexView(request):
    return render(request,'indexCar.html')

def LoginView(request):
    return render(request,'login.html')

def RegistroView(request):
    return render(request,'registro.html')

@login_required
def CotizadorView(request):
    return render(request, 'cotizador.html')

@login_required
def CatalogoView(request):
    vehículos = Vehículo.objects.all()
    return render(request, 'CatalogoAutos.html', {'vehículos': vehículos})

def exit(request):
    logout(request)
    return redirect('indexCar')