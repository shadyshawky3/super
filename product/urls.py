from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.product_new, name='product_new'),
    # path('<int:pk>/edit/', views.product_update, name='product-update'),
    # path('<int:product_id>/delete/', views.product_hard_delete, name='product_hard_delete'),
    # path('<int:product_id>/soft-delete/', views.product_soft_delete, name='product_soft_delete'),

    path('', views.product_list, name='product_list'),  # ← لازم يكون فيه name='product_list'
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('<slug:category_slug>/', views.products_by_category, name='product-by-category'),  

    path('edit/<int:pk>/', views.product_update, name='product_update'),
    path('delete/<int:product_id>/', views.product_hard_delete, name='product_hard_delete'),
    path('soft_delete/<int:product_id>/', views.product_soft_delete, name='product_soft_delete'),

]

    # path('category/<slug:slug>/', views.products_by_category, name='product-by-category'),


# path('product/add/', views.product_add, name='product_add'),
    # path('product/edit/<int:product_id>/', views.product_edit, name='product_edit'),
        # path('product/search/', views.product_search, name='product_search'),