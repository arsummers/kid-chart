from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('kids/', views.KidListView.as_view(), name='kids'),
    path('kids/<int:pk>', views.KidDetailView.as_view(), name='kid-detail'),
]