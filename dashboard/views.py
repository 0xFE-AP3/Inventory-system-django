from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from .filters import ProductFilter


@login_required
def index(request):
    orders = Order.objects.all()
    items = Product.objects.get
    if request.method=='POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-product')
    else:
        form = OrderForm()
    context = {
        'orders' : orders,
        'form' : form,
    }
    return render(request, 'dashboard/profile.html', context)

@login_required
def staff(request):
    workers = User.objects.all()
    context = {
        'workers':workers
    }
    return render(request, 'dashboard/staff.html', context)

def staff_detail(request, pk):
    workers = User.objects.get(id=pk)
    context = {
        'workers': workers,
    }
    return render(request, 'dashboard/staff_detail.html', context)

@login_required
def product(request):
    items = Product.objects.all() #ORM
    #items = Product.objects.raw('SELECT * FROM dashboard_product')

    myFilter = ProductFilter(request.GET, queryset=items)
    items = myFilter.qs

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('nome')
            messages.success(request, f'{product_name} è stato aggiunto')
            return redirect('dashboard-product')
    else:
        form = ProductForm()
    context = {
        'items': items,
        'form': form,
        'myFilter': myFilter,
    }
    return render(request, 'dashboard/product.html', context)

def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=item)
        if form.is_valid():
            quantity = form.cleaned_data['order_quantity']
            item.quantita += quantity
            if item.quantita == 0:
                item.nome = item.nome.replace(' DA ORDINARE', ' ORDINATO')
            if item.quantita > 0:
                #item.nome = item.nome - " DA ORDINARE"
                item.nome = item.nome.replace(' DA ORDINARE', '')
                item.nome = item.nome.replace(' ORDINATO', '')
            form.save()
            return redirect('dashboard-product')
    else:
        form = OrderForm(instance=item)
    context = {
        'form':form,
    }
    return render(request, 'dashboard/product_delete.html', context)

def product_update(request, pk):
    item = Product.objects.get(id=pk)
    
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=item)
        if form.is_valid():
            quantity = form.cleaned_data['order_quantity']
            if item.quantita >= quantity and quantity != 0:
                item.quantita -= quantity
                if item.quantita <= quantity or item.quantita == 1:
                    item.nome = item.nome + " DA ORDINARE"
            else:
                return redirect('dashboard-order')
            form.save()
            return redirect('dashboard-product')
    else:
        form = OrderForm(instance=item)
    context = {
        'form':form,
    }
    return render(request, 'dashboard/product_update.html', context)


@login_required
def order(request):
    orders = Order.objects.all()

    context = {
        'orders':orders,
    }
    return render(request, 'dashboard/order.html', context)

