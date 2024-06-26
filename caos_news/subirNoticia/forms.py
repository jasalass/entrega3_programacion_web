from django import forms
from .models import Noticia

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'bajada_de_titulo', 'cuerpo', 'imagen']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el título'}),
            'bajada_de_titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la bajada de título'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese el cuerpo de la noticia'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
