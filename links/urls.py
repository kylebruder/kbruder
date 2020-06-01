from django.urls import path
from .views import (LinkCreateView, LinkListView, LinkDetailView,
     LinkUpdateView, LinkDeleteView, LinkUserListView, promote_link)

app_name = "links"

urlpatterns = [
    path('add/', LinkCreateView.as_view(), name='link_create'),
    path('', LinkListView.as_view(), name='link_list'),
    path('<int:pk>/', LinkDetailView.as_view(), name='link_detail'),
    path('modify/<int:pk>/', LinkUpdateView.as_view(), name='link_update'),
    path('delete/<int:pk>/', LinkDeleteView.as_view(), name='link_delete'),
    path('promote/<int:pk>/', promote_link, name='promote'),
    path('member/<slug:user>/', LinkUserListView.as_view(), name='link_user_list')
]
 
