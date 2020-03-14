from django.urls import path
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from .views import (ImagesCreateView, ImagesListView, ImagesDetailView,
    ImagesUpdateView, ImagesDeleteView, GalleryCreateView, GalleryListView,
    GalleryDetailView, GalleryUpdateView, GalleryDeleteView)

app_name = "images"

urlpatterns = [
    path(
        'upload/',
        ImagesCreateView.as_view(),
        name='images_create'
    ),
    path(
        '',
        ImagesListView.as_view(),
        name='images_list'
    ),
    path(
        '<int:pk>/',
        ImagesDetailView.as_view(),
        name='images_detail'
    ),
    path(
        'modify/<int:pk>/',
        ImagesUpdateView.as_view(),
        name='images_update'
    ),
    path(
        'delete/',
        ImagesDeleteView.as_view(),
        name='images_delete'
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
