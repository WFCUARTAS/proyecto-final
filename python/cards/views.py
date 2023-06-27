from django.shortcuts import render
from django.http import HttpResponse ,JsonResponse
from .models import Mejores, Exclusivas


def  Listar_mejores(request):
    l = list(Mejores.objects.values())
    return JsonResponse(l , safe=False)

def  Listar_exclusivas(request):
    l = list(Exclusivas.objects.values())
    return JsonResponse(l , safe=False)