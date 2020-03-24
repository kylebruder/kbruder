from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    )
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.core.files.images import ImageFile
from .models import Update

class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_update'] = Update.objects.all()[0]
        return context
      
class UpdatesListView(ListView):
    model = Update
    paginate_by = 64
    ordering = ['-publication_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class UpdatesDetailView(DetailView):
    model = Update

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
