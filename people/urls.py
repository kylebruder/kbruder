from django.urls import path
from people.views import (ArtistCreateView, ArtistListView, ArtistDetailView,
    ArtistUpdateView, ArtistDeleteView)

app_name = "people"

urlpatterns = [
    path('artists/new/', ArtistCreateView.as_view(), name="artist_create"),
    path('artists/', ArtistListView.as_view(), name="artist_list"),
    path('artists/<slug:slug>/', ArtistDetailView.as_view(), name="artist_detail"),
    path('artists/modify/<slug:slug>/', ArtistUpdateView.as_view(), name="artist_update"),
    path('artists/delete/<slug:slug>/', ArtistDeleteView.as_view(), name="artist_delete"),
]
