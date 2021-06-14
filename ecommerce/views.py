from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'geral/home.html')

def produtos(request):
    return render(request, 'geral/produtos.html')

def produto_detalhe(request, id):
    return render(request, 'geral/produto_detalhe.html')

def about(request):
    return render(request, 'geral/about.html')