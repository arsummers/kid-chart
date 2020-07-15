from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('kids/', views.KidListView.as_view(), name='kids'),
]