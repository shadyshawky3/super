from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def product_list(request):
    products = Product.objects.all()
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


