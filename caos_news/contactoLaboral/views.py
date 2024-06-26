from django.shortcuts import render

# Create your views here.
def contactoLaboral(request):
    context = {}
    return render(request, 'contacto-laboral.html', context)