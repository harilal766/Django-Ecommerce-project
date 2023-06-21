from django.urls import path
from cart import views

app_name='cart'

urlpatterns=[
    path('cart_view', views.cart_view, name='cart_view'),
    path('add_cart/<int:p>', views.add_cart, name='add_cart'),
    path('minus/<int:p>', views.minus, name='minus'),
    path('delete/<int:p>', views.delete, name='delete'),
    path('order', views.order, name='order'),
    path('order_views', views.order_views, name='order_views'),
]