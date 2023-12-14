from django.utils.timezone import datetime
from django.shortcuts import render

def home(request):
    return render(request, "contabil/dashboard.html")

def dashboard(request):
    return render(request, "contabil/dashboard.html")

def cadastro_func(request):
    return render(request, "contabil/cadastro-func.html")

def lista_func(request):
    return render(request, "contabil/lista-func.html")

def calculo_recisao(request):
    return render(request, "contabil/calculo-recisao.html")

def cadastro_projeto(request):
    return render(request, "contabil/cadastro-projeto.html")

def orcamentos(request):
    return render(request, "contabil/orcamentos.html")

def rubricas(request):
    return render(request, "contabil/rubricas.html")

def login(request):
    return render(request, "contabil/log-in.html")

def settings(request):
    return render(request, "contabil/settings.html")
