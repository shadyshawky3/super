from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category
from category.models import Category  # تأكد من الاستيراد
from django.contrib import messages
from .forms import *
# views.py
def product_list(request):
    products = Product.objects.filter(is_deleted=False)
    return render(request, 'product/product_list.html', {'products': products})



def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product/product_detail.html', {'product': product})
def products_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'product/product_list.html', {
        'category': category,
        'products': products
    })



def product_new(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        category_id = request.POST.get('category')
        stock = request.POST.get('stock')  # Uncommented stock field
        sku = request.POST.get('sku')  # Uncommented sku field
        image = request.FILES.get('image')
        # if Product.objects.filter(sku=sku).exists():
        #     messages.error(request, "This SKU already exists. Please choose a different one.")
        #     return render(request, 'product/product_new.html', {
        #         'categories': categories,
        #         'error': 'SKU already exists',
        #     })
        # ربط الكاتيجوري
        category = Category.objects.get(id=category_id)

        Product.objects.create(
            name=name,
            description=description,
            price=price,
            category=category,
            stock=stock,  # Assuming you have a stock field
            sku=sku,  # Assuming you have a sku field
            image=image
        )

        return redirect('product_list')  # رجع لصفحة عرض المنتجات

    return render(request, 'product/product_new.html', {'categories': categories})






# def product_update(request, pk):
#     product = Product.objects.get(pk=pk)
#     categories = Category.objects.all()

#     if request.method == "POST":
#         product.name = request.POST.get('name')
#         product.description = request.POST.get('description')
#         product.price = request.POST.get('price')
#         category_id = request.POST.get('category')
#         product.category = Category.objects.get(id=category_id)
#         product.stock = request.POST.get('stock')  # Assuming you have a stock field
#         if request.FILES.get('image'):
#             product.image = request.FILES.get('image')
#         product.save()
#         return redirect('product_list')  # Redirect to the product list after saving

#     return render(request, 'product/product_edit.html', {
#         'product': product,
#         'categories': categories,
#     })

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    categories = Category.objects.all()
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'product/product_edit.html', {'form': form, 'product': product, 'categories': categories})





# def product_hard_delete(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     if request.method == 'POST':
#         product.delete()
#         return redirect('product_list')
#     return render(request, 'product/product_delete.html', {'product': product})

# def product_soft_delete(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     if request.method == 'POST':
#         product.is_deleted = True
#         product.save()
#         return redirect('product_list')
#     return render(request, 'product/product_soft_delete.html', {'product': product})

def product_soft_delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductSoftDeleteForm(request.POST, instance=product)
        if form.is_valid():
            product.is_deleted = True
            product.save()
            return redirect('product_list')
    else:
        form = ProductSoftDeleteForm(instance=product)

    return render(request, 'product/product_soft_delete.html', {'form': form, 'product': product})



def product_hard_delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductHardDeleteForm(request.POST, instance=product)
        if form.is_valid():
            product.delete()
            return redirect('product_list')
    else:
        form = ProductHardDeleteForm(instance=product)
    
    return render(request, 'product/product_delete.html', {'form': form, 'product': product})






















































# def product_add(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         description = request.POST.get('description')
#         price = request.POST.get('price')
#         stock = request.POST.get('stock')
#         sku = request.POST.get('sku')
#         category_id = request.POST.get('category')
#         image = request.POST.get('image')  # Assuming you are getting the image URL from the form

#         category = Category.objects.get(id=category_id)
#         product = Product(
#             name=name,
#             description=description,
#             price=price,
#             stock=stock,
#             sku=sku,
#             category=category,
#             image=image
#         )
#         product.save()
#         return render(request, 'product/product_detail.html', {'product': product})
#     else:
#         categories = Category.objects.all()
#         return render(request, 'product/product_add.html', {'categories': categories})
# def product_edit(request, product_id):
#     product = Product.objects.get(id=product_id)
#     if request.method == 'POST':
#         product.name = request.POST.get('name')
#         product.description = request.POST.get('description')
#         product.price = request.POST.get('price')
#         product.stock = request.POST.get('stock')
#         product.sku = request.POST.get('sku')
#         category_id = request.POST.get('category')
#         category = Category.objects.get(id=category_id)
#         product.category = category
#         product.image = request.POST.get('image')  # Assuming you are getting the image URL from the form
#         product.save()
#         return render(request, 'product/product_detail.html', {'product': product})
#     else:
#         categories = Category.objects.all()
#         return render(request, 'product/product_edit.html', {'product': product, 'categories': categories})
# def product_delete(request, product_id):
#     product = Product.objects.get(id=product_id)
#     if request.method == 'POST':
#         product.delete()
#         return render(request, 'product/product_list.html', {'products': Product.objects.all()})
#     return render(request, 'product/product_delete.html', {'product': product})

# def product_search(request):
#     query = request.GET.get('q')
#     if query:
#         products = Product.objects.filter(name__icontains=query)
#     else:
#         products = Product.objects.all()
#     return render(request, 'product/product_search.html', {'products': products})


