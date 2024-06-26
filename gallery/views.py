from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .form import ProductForm
# Create your views here.

# THIS IS WHAT WE ARE DOING:
# product_list(request): retrieves the list of all the products
# product_detail(request, pk): retrieves a particular product based on primary key
# edit_product(request, pk): handles editing and updating the new product info if form is valid, else displays form for editing
# delete_product(request, pk): it deletes a product; if post request is made, 
# it deletes and redirectes to product list; otherwise displays a confirmation page for deleting

def product_list(request):
    products =Product.objects.all()
    return render(request, 'gallery/template/gallery/index.html', {'products':products})

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'gallery/template/gallery/index2.html', {'product':product})

def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'gallery/template/gallery/edit.html',{'form':form})

def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'gallery/template/gallery/delete.html',{'product':product})

def home(request):
    return HttpResponse('Hello, World!')