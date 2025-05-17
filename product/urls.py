from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),  # ← لازم يكون فيه name='product_list'
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('<slug:category_slug>/', views.products_by_category, name='product-by-category'),  # ← هذا هو المطلوب
]

    # path('category/<slug:slug>/', views.products_by_category, name='product-by-category'),


# path('product/add/', views.product_add, name='product_add'),
    # path('product/edit/<int:product_id>/', views.product_edit, name='product_edit'),
    # path('product/delete/<int:product_id>/', views.product_delete, name='product_delete'),
    # path('product/search/', views.product_search, name='product_search'),