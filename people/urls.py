from django.urls import path
from people.views import (ArtistCreateView, ArtistListView, ArtistDetailView,
    ArtistUpdateView, ArtistDeleteView, promote_artist)

app_name = "people"

urlpatterns = [
    path('artists/new/', ArtistCreateView.as_view(), name="artist_create"),
    path('artists/', ArtistListView.as_view(), name="artist_list"),
    path('artists/<slug:slug>/', ArtistDetailView.as_view(), name="artist_detail"),
    path('artists/modify/<slug:slug>/', ArtistUpdateView.as_view(), name="artist_update"),
    path('artists/delete/<int:pk>/', ArtistDeleteView.as_view(), name="artist_delete"),
    path('artists/promote/<int:pk>/', promote_artist, name="artist_promote"),
]
