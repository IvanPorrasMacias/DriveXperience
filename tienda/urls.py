from django.urls import path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet,VehículoViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'vehiculos', VehículoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('indexCar/', views.IndexView, name='indexCar'),
    path('login/', views.LoginView, name='login'),
    path('registro/',views.RegistroView, name='registro'),
    path('cotizador/',views.CotizadorView, name='cotizador'),
    path('catalogo/', views.CatalogoView, name='catalogo')
]