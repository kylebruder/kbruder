#from django.contrib import admin
from django.urls import path
from .views import (
    UpdatesListView, UpdatesDetailView, UpdatesCreateView,
    UpdatesUpdateView, UpdatesDeleteView, promote_update,
    UpdatesUserListView, updates_publish_view,
)

app_name = 'updates'
urlpatterns = [
    path('', UpdatesListView.as_view(), name='update_list'),
    path('add/', UpdatesCreateView.as_view(), name='update_create'),
    path('modify/<slug:slug>/', UpdatesUpdateView.as_view(), name='update_update'),
    path('delete/<int:pk>/', UpdatesDeleteView.as_view(), name='update_delete'),
    path('promote/<int:pk>/', promote_update, name='promote'),
    path('publish/<int:pk>/', updates_publish_view, name='publish_update'),
    path('member/<slug:user>/', UpdatesUserListView.as_view(), name='update_user_list'),
    path('<slug:slug>/', UpdatesDetailView.as_view(), name='update_detail'),
]
