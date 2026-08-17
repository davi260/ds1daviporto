from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Desevolvimento de Sistemas</h1>"
                        "<p>Projeto base - 2026</p>")

def sobre(request):
    return HttpResponse("<h2>Sobre</h2><p>App core do projeto DS1.</p>")

def saudacao(request, nome):
    return HttpResponse(f"<h2>Olá, {nome}!</h2>")
 
 
def dobro(request, numero):
    return HttpResponse(f"<p>O dobro de {numero} é {numero * 2}.</p>")

def tabuada(request, n):
    multi =[1,2,3,4,5,6,7,8,9,10]
    texto_final=""
    for numero in multi:
        resultado = n*numero
        texto_final += f"{n} x {numero} = {resultado} <br>"
    return HttpResponse(texto_final)

def perfil(request,nome,idade):
    return HttpResponse(f"Oi eu sou o {nome}! Tenho {idade} anos.")

# Create your views here.
