#from django.contrib import admin
from django.urls import path
from .views import (
    UpdatesListView, UpdatesDetailView, UpdatesCreateView,
    UpdatesUpdateView, UpdatesDeleteView, promote_update, UpdatesUserListView
)

app_name = 'updates'
urlpatterns = [
    path('', UpdatesListView.as_view(), name='update_list'),
    path('add/', UpdatesCreateView.as_view(), name='update_create'),
    path('modify/<slug:slug>/', UpdatesUpdateView.as_view(), name='update_update'),
    path('delete/<int:pk>/', UpdatesDeleteView.as_view(), name='update_delete'),
    path('promote/<int:pk>/', promote_update, name='promote'),
    path('member/<slug:user>/', UpdatesUserListView.as_view(), name='update_user_list'),
    path('<slug:slug>/', UpdatesDetailView.as_view(), name='update_detail'),
]
