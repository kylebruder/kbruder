from django.urls import path
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from .views import (ImageCreateView, ImageListView, ImageDetailView,
    ImageUpdateView, ImageDeleteView, GalleryCreateView, GalleryListView,
    GalleryDetailView, GalleryUpdateView, GalleryDeleteView, PieceCreateView,
    PieceListView, PieceDetailView, PieceUpdateView, PieceDeleteView,
    promote_gallery, promote_piece, ImageUserListView, GalleryUserListView,
    PieceUserListView)

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
        'artworks/add/',
        PieceCreateView.as_view(),
        name='piece_create'
    ),
    path(
        'artworks/modify/<slug:slug>/',
        PieceUpdateView.as_view(),
        name='piece_update'
    ),
    path(
        'artworks/',
        PieceListView.as_view(),
        name='piece_list'
    ),
    path(
        'artworks/<slug:slug>/',
        PieceDetailView.as_view(),
        name='piece_detail'
    ),
    path(
        'artworks/delete/<int:pk>/',
        PieceDeleteView.as_view(),
        name='piece_delete'
    ),
    path(
        'artworks/promote/<int:pk>/',
        promote_piece,
        name='promote_piece'
    ),
    path(
        'member/<slug:user>/',
        ImageUserListView.as_view(),
        name='image_user_list'
    ),
    path(
        'gallery/member/<slug:user>/',
        GalleryUserListView.as_view(),
        name='gallery_user_list'
    ),
    path(
        'artworks/member/<slug:user>/',
        PieceUserListView.as_view(),
        name='piece_user_list'
    ),
]
