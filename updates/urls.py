#from django.contrib import admin
from django.urls import path
from .views import UpdatesListView, UpdatesDetailView

app_name = 'updates'
urlpatterns = [
    path('', UpdatesListView.as_view(), name='update_list'),
    path('<slug:slug>/', UpdatesDetailView.as_view(), name='update_detail')
]
