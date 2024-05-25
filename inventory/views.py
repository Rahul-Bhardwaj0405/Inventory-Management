
# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.contrib import messages

def add_product(request):
    if request.method == "POST":
        product_id = request.POST['product_id']
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        quantity = request.POST['quantity']
        Product.objects.create(product_id=product_id, name=name, description=description, price=price, quantity=quantity)
        messages.success(request, 'Product added successfully!')
        return redirect('product_list')
    return render(request, 'inventory/add_product.html')

def update_product(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    if request.method == "POST":
        product.update_info(
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            price=request.POST.get('price')
        )
        messages.success(request, 'Product updated successfully!')
        return redirect('product_list')
    return render(request, 'inventory/update_product.html', {'product': product})

def delete_product(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    if request.method == "POST":
        product.delete()
        messages.success(request, 'Product deleted successfully!')
        return redirect('product_list')
    return render(request, 'inventory/delete_product.html', {'product': product})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})

def update_stock(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    if request.method == "POST":
        quantity = int(request.POST['quantity'])
        product.quantity += quantity
        if product.quantity < 0:
            messages.error(request, 'Stock cannot be negative!')
        else:
            product.save()
            messages.success(request, 'Stock updated successfully!')
        return redirect('product_list')
    return render(request, 'inventory/update_stock.html', {'product': product})

def process_sale(request):
    if request.method == "POST":
        product_id = request.POST['product_id']
        quantity = int(request.POST['quantity'])
        product = get_object_or_404(Product, product_id=product_id)
        if product.quantity < quantity:
            messages.error(request, 'Not enough stock!')
        else:
            product.quantity -= quantity
            product.save()
            total_cost = quantity * product.price
            messages.success(request, f'Sale processed! Total cost: ${total_cost}')
        return redirect('product_list')
    return render(request, 'inventory/process_sale.html')

def generate_report(request):
    products = Product.objects.all()
    return render(request, 'inventory/report.html', {'products': products})

def generate_low_stock_report(request):
    threshold = 5
    low_stock_products = Product.objects.filter(quantity__lt=threshold)
    return render(request, 'inventory/low_stock_report.html', {'products': low_stock_products})
