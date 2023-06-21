from django.urls import path,include
from shop import views

from rest_framework import routers
router=routers.DefaultRouter()
router.register('products',views.ProductViewSet)
router.register('users',views.UserViewSet)

app_name='shop'
urlpatterns = [
    path('api/',include(router.urls)), #api

    path('',views.home,name='home'),
    path('category',views.category,name='category'),
    path('products/<slug:cslug>',views.products,name='products'),
    path('prodetail/<slug:pslug>',views.prodetail,name='prodetail'),

    path('register', views.register, name='register'),
    path('usersignin', views.usersignin, name='usersignin'),
    path('usersignout', views.usersignout, name='usersignout'),
]


from rest_framework.authtoken import views
urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token)
]