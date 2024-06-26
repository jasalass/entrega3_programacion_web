from django.shortcuts import render

# Create your views here.
def busqueda(request):
    context = {}
    return render(request, 'busqueda.html', context)