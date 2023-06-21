
from django.urls import path
from search import views

app_name='search'

urlpatterns = [
    path('searchresult',views.searchresult,name='searchresult'),
]