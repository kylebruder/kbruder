from django.urls import path
from people.views import ArtistCreateView

app_name = "people"
urlpatterns = [
    path('artists/new/', ArtistCreateView.as_view(), name="artist_create"),
]
