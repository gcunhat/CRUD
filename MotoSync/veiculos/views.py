from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse('Olá!')

def veiculosCad(request):
    return render(request, 'veiculos/veiculosCad.html')

def yourName(request, name):
    return render(request, 'veiculos/yourname.html', {'name':name})
    
    