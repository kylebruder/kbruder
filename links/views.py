from django.contrib import messages
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    )
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Link

# Create your views here.

class LinkCreateView(LoginRequiredMixin, CreateView):

    model = Link
    fields = ['title', 'description', 'image', 'url']
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('links:link_list')

    def form_valid(self, form):
        form.instance.creation_date = timezone.now()
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class LinkListView(ListView):

    model = Link
    paginate_by = 16 
    ordering = ['-creation_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class LinkDetailView(DetailView):

    model = Link
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class LinkUpdateView(LoginRequiredMixin, UpdateView):

    model = Link
    fields = ['title','description', 'url']
    template_name_suffix = '_update_form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class LinkDeleteView(LoginRequiredMixin, DeleteView):

    model = Link
    success_url = reverse_lazy('links:links_list')
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

