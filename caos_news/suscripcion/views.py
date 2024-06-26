from django.shortcuts import render

# Create your views here.
def suscripcion(request):
    context = {}
    return render(request,'suscripcion.html', context)