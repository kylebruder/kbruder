from django.urls import path
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from .views import (ImageCreateView, ImageListView, ImageDetailView,
    ImageUpdateView, ImageDeleteView, GalleryCreateView, GalleryListView,
    GalleryDetailView, GalleryUpdateView, GalleryDeleteView)

app_name = "images"

urlpatterns = [
    path(
        'upload/',
        ImageCreateView.as_view(),
        name='image_create'
    ),
    path(
        '',
        ImageListView.as_view(),
        name='image_list'
    ),
    path(
        '<int:pk>/',
        ImageDetailView.as_view(),
        name='image_detail'
    ),
    path(
        'modify/<int:pk>/',
        ImageUpdateView.as_view(),
        name='image_update'
    ),
    path(
        'delete/',
        ImageDeleteView.as_view(),
        name='image_delete'
    ),
    path(
        'gallery/create/',
        GalleryCreateView.as_view(),
        name='gallery_create'
    ),
    path(
        'gallery/',
        GalleryListView.as_view(),
        name='gallery_list'
    ),
    path(
        'gallery/<slug:slug>/',
        GalleryDetailView.as_view(),
        name='gallery_detail'
    ),
    path(
        'gallery/modify/<slug:slug>/',
        GalleryUpdateView.as_view(),
        name='gallery_update'
    ),
    path(
        'gallery/delete/',
        GalleryDeleteView.as_view(),
        name='gallery_delete'
    ),
]
