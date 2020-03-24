from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    )
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.core.files.images import ImageFile
from .models import Image, Gallery

# Create your views here.

class ImageCreateView(LoginRequiredMixin, CreateView):

    model = Image
    fields = ['image_file', 'caption', 'alt_text',]
    template_name_suffix = '_create_form'

    def form_valid(self, form):
        form.instance.creation_date = timezone.now()
        form.instance.user = self.request.user
        return super().form_valid(form)
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ImageListView(ListView):

    model = Image
    paginate_by = 32
    ordering = ['-creation_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ImageDetailView(DetailView):

    model = Image

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ImageUpdateView(LoginRequiredMixin, UpdateView):

    model = Image
    fields = ['image_file', 'caption', 'alt_text',]
    template_name_suffix = '_update_form'
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
		
class ImageDeleteView(LoginRequiredMixin, DeleteView):

    model = Image
    success_url = reverse_lazy('images:image_list')
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class GalleryCreateView(CreateView):

    model = Gallery
    fields = []

    #def form_valid(self, form):
    #    form.instance.user = self.request.user
    #    return super().form_valid(form)
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class GalleryListView(ListView):

    model = Gallery
    paginate_by = 32
    ordering = ['-creation_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class GalleryDetailView(DetailView):

    model = Gallery
    paginate_by = 32
    ordering = []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class GalleryUpdateView(UpdateView):

    model = Gallery
    fields = []
    #template_name_suffix = '_update_form'
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
		
class GalleryDeleteView(DeleteView):

    model = Gallery
    success_url = reverse_lazy('')
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
