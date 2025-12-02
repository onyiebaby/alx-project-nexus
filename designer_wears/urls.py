from django.urls import path, include
from .import views
from .views import create_checkout_session
from .views import webhook
urlpatterns = [
    path('', views.index, name='homepage'),
    path('', views.home, name='homepage'),
    path('designers/', views.DesignerListCreateView.as_view(), name='designer-detail'),
    path('designers/<int:pk>/', views.DesignerRetrieveUpdateDestroyView.as_view(), name='designer-detail'),

    path('categories/', views.CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:pk>/',views.CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail'),

    path('products/', views.ProductListCreateView.as_view(), name='product-list'),
    path('products/<int:pk>/', views.ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),

    path('customers/', views.CustomerListCreateView.as_view(), name='customer-list'),
    path('customers/<int:pk>/', views.CustomerRetrieveUpdateDestroyView.as_view(), name='customer-detail'),

    path('orders/', views.OrderListCreateView.as_view(), name='order-list'),
    path('orders/<int:pk>/', views.OrderRetrieveUpdateDestroyView.as_view(), name='order-detail'),

    path('create-checkout-session/', create_checkout_session, name='checkout'),
    path('stripe/webhook/', webhook, name='stripe-webhook'),

    path('', views.index, name='index'),
]
