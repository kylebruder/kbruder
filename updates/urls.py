#from django.contrib import admin
from django.urls import path
from .views import UpdatesListView, UpdatesDetailView, UpdatesCreateView

app_name = 'updates'
urlpatterns = [
    path('', UpdatesListView.as_view(), name='update_list'),
    path('add/', UpdatesCreateView.as_view(), name='update_create'),
    path('<slug:slug>/', UpdatesDetailView.as_view(), name='update_detail'),
]
