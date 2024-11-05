from django import forms
from .models import Usuario

# class RegistroForm(forms.ModelForm):
#     class Meta:
#         model = Usuario
#         fields = ['nombre', 'apellidos', 'direccion', 'teléfono', 'RFC', 'contraseña']
#         widgets = {
#             'contraseña': forms.PasswordInput(),
#         }
