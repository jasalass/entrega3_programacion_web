from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .forms import LoginForm
from .models import Usuario
from .forms import RegistroForm

def vista_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            correo = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            try:
                user = Usuario.objects.get(correo=correo)
                if user.check_password(password):  # Usa check_password para comparar de manera segura
                    auth_login(request, user)
                    return redirect('index')  # Redirigir a la página principal después del login exitoso
                else:
                    context = {'form': form, 'mensaje': 'Usuario o contraseña incorrecta'}  # Preservar el formulario
                    return render(request, 'login.html', context)
            except Usuario.DoesNotExist:
                context = {'form': form, 'mensaje': 'Usuario no existe'}  # Preservar el formulario
                return render(request, 'login.html', context)
        else:
            context = {'form': form, 'mensaje': 'Hay errores en el formulario. Por favor, inténtelo de nuevo.'}
            return render(request, 'login.html', context)
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})



def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
    else:
        form = RegistroForm()
        return render(request, 'registro.html', {'form': form})
    