from django.urls import path
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from .views import (ImageCreateView, ImageListView, ImageDetailView,
    ImageUpdateView, ImageDeleteView, GalleryCreateView, GalleryListView,
    GalleryDetailView, GalleryUpdateView, GalleryDeleteView, PieceCreateView,
    PieceListView, PieceDetailView, PieceUpdateView, PieceDeleteView, promote_image,
    promote_gallery)

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
    #path(
    #    'delete/<int:pk>/',
    #    ImageDeleteView.as_view(),
    #    name='image_delete'
    #),
    path(
        'promote/<int:pk>/',
        promote_image,
        name='promote_image'
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
        'gallery/delete/<int:pk>/',
        GalleryDeleteView.as_view(),
        name='gallery_delete'
    ),
    path(
        'gallery/promote/<int:pk>/',
        promote_gallery,
        name='promote_gallery'
    ),
    path(
        'pieces/create/',
        PieceCreateView.as_view(),
        name='piece_create'
    ),
    path(
        'pieces/modify/<slug:slug>/',
        PieceUpdateView.as_view(),
        name='piece_update'
    ),
    path(
        'pieces/',
        PieceListView.as_view(),
        name='piece_list'
    ),
    path(
        'pieces/<slug:slug>/',
        PieceDetailView.as_view(),
        name='piece_detail'
    ),
    path(
        'pieces/delete/<slug:slug>/',
        PieceDeleteView.as_view(),
        name='piece_delete'
    ),
]
