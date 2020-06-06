from django.urls import path
from .views import (ObjectiveCreateView, ObjectiveDetailView,
    CurrentObjectiveListView, ObjectiveUpdateView, ObjectiveDeleteView,
    complete_objective, commit_objective, pay_bounty,)

app_name = "backlog"

urlpatterns = [
    path('', CurrentObjectiveListView.as_view(), name='objective_list'),
    path('objective/new/', ObjectiveCreateView.as_view(), name='objective_create'),
    path('objective/update/<int:pk>', ObjectiveUpdateView.as_view(), name='objective_update'),
    path('objective/delete/<int:pk>', ObjectiveDeleteView.as_view(), name='objective_delete'),
    path('objective/<int:pk>/', ObjectiveDetailView.as_view(), name='objective_detail'),
    path('objective/complete/<int:pk>/', complete_objective, name='complete_objective'),
    path('objective/commit/<int:pk>/', commit_objective, name='commit_objective'),
    path('objective/claim/<int:pk>/', pay_bounty, name='pay_bounty'),
]
