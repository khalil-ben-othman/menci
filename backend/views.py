from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Item, Client, Order, Message
from django.contrib import messages


def index(request):
    return render(request, 'index.html')
    
def index_id(request, id):
    return render(request, 'index.html')
    
def error404(request, exeption):
    return render(request, '404.html')