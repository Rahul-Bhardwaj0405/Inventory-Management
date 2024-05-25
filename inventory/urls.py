from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add/', views.add_product, name='add_product'),
    path('update/<str:product_id>/', views.update_product, name='update_product'),
    path('delete/<str:product_id>/', views.delete_product, name='delete_product'),
    path('update_stock/<str:product_id>/', views.update_stock, name='update_stock'),
    path('process_sale/', views.process_sale, name='process_sale'),
    path('report/', views.generate_report, name='generate_report'),
    path('low_stock_report/', views.generate_low_stock_report, name='generate_low_stock_report'),
]
