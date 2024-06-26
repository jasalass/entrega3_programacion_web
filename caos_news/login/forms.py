from django import forms
from .models import Usuario
from suscripcion.models import Suscripcion

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su correo'}),label='Correo')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}), label='Password')




class RegistroForm(forms.ModelForm):
    correo = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ingrese su correo'
    }), label='Correo')
    
    nombre = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ingrese su nombre'
    }), label='Nombre')
    
    apellido = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ingrese su apellido'
    }), label='Apellido')
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Contraseña'
    }), label='Password')
    
    descripcion = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ingrese una descripción'
    }), label='Descripción', required=False)
    
    periodista = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input'
    }), label='Periodista', required=False)
    
    suscripcion = forms.ModelChoiceField(queryset=Suscripcion.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control'
    }), label='Suscripción', required=False)
    
    class Meta:
        model = Usuario
        fields = ['correo', 'nombre', 'apellido', 'password', 'descripcion', 'periodista', 'suscripcion']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
