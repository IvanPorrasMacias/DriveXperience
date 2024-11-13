from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .models import Usuario,Vehículo
from .serializers import UsuarioSerializer,VehículoSerializer
from .forms import CustomUserAuthenticationForm, CustomUserRegistrationForm

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
    data = {
        'form': CustomUserRegistrationForm()
    }
    if request.method == 'POST':
        user_creation_form = CustomUserRegistrationForm(data=request.POST)
        if user_creation_form.is_valid():
            auth_user = user_creation_form.save()
            auth_user = authenticate(
                username=user_creation_form.cleaned_data['username'],
                password=user_creation_form.cleaned_data['password1']
            )
            if auth_user is not None:
                login(request, auth_user)
                return redirect('indexCar')
            else:
                data['error'] = "Error de autenticación. Por favor, intenta de nuevo."
        else:
            data['error'] = "El formulario no es válido. Revisa los datos ingresados."
        data['form'] = user_creation_form 
    return render(request, 'registration/register.html', data)


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