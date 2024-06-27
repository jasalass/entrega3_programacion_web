from django.shortcuts import render, redirect, get_object_or_404
from .forms import NoticiaForm
from django.contrib.auth.decorators import login_required
from .models import Noticia

@login_required
def subirNoticia(request):
    
    if request.method == 'POST':
    
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            noticia = form.save(commit=False)
            noticia.usuario = request.user  # Asigna el usuario actual a la noticia
            noticia.save()
            return redirect('listar-noticias')  # Redirigir a la página principal después de guardar la noticia
    else:
        if not request.user.periodista:
            return redirect('index')
        else:
            form = NoticiaForm()
            return render(request, 'subir-noticia.html', {'form': form})

@login_required
def lista_noticias(request):
    if not request.user.periodista:
            return redirect('index')
    else:
        noticias = Noticia.objects.filter(usuario=request.user)
        return render(request, 'listar-noticias.html', {'noticias': noticias})


@login_required
def actualizar_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES, instance=noticia)
        if form.is_valid():
            form.save()
            return redirect('listar-noticias')
    else:
        if not request.user.periodista:
            return redirect('index')
        else:
            form = NoticiaForm(instance=noticia)
            return render(request, 'actualizar_noticia.html', {'form': form})
        

@login_required
def eliminar_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk, usuario=request.user)
    if request.method == 'POST':
        noticia.delete()
        return redirect('listar-noticias')
    return render(request, 'subirNoticia/eliminar_noticia.html', {'noticia': noticia})