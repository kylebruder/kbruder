from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from .models import Objective, Status, Priority, GitBranch

# Create your views here.


class ObjectiveCreateView(LoginRequiredMixin, CreateView):

    model = Objective
    fields = [
        'summary',
        'assigned_to',
        'priority',
        'target_date',
        'status',
        'git_branch',
    ]
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('backlog:objective_list')

class ObjectiveDetailView(LoginRequiredMixin, DetailView):

    model = Objective
    
class CurrentObjectiveListView(LoginRequiredMixin, ListView):

    model = Objective
    queryset = Objective.objects.filter(committed=False)

class ObjectiveUpdateView(LoginRequiredMixin, UpdateView):

    model = Objective
    fields = [
        'summary',
        'assigned_to',
        'priority',
        'target_date',
        'status',
        'git_branch',
    ]
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('backlog:objective_list')

class ObjectiveDeleteView(LoginRequiredMixin, DeleteView):

    model = Objective
    success_url = reverse_lazy('backlog:backlog_list')

def complete_objective(request, pk):
    o = get_object_or_404(Objective, pk=pk)
    Objective.mark_complete(o)
    return HttpResponseRedirect(reverse('backlog:objective_list'))

def commit_objective(request, pk):
    o = get_object_or_404(Objective, pk=pk)
    Objective.mark_committed(o)
    return HttpResponseRedirect(reverse('backlog:objective_list'))

def pay_bounty(request, pk):
    o = get_object_or_404(Objective, pk=pk)
    Objective.mark_bounty_claimed(o)
    return HttpResponseRedirect(reverse('backlog:objective_list'))


