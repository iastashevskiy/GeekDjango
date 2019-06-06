from django.shortcuts import render

def products(request):
    return render(request, 'mainapp/products.html')

# Create your views here.
def contacts(request):
    return render(request, 'mainapp/contacts.html')

def index(request):
    return render(request, 'mainapp/index.html')

def catalogue(request):
    return render(request, 'mainapp/catalogue.html')