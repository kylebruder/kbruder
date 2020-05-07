from django.urls import path
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from tags.views import TagCreateView

app_name = "tags"

urlpatterns = [
    path('new/', TagCreateView.as_view(), name='new'),
]
