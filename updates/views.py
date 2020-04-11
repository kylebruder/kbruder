from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    )
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.core.files.images import ImageFile
from django.urls import reverse
from django.utils import timezone
from .models import Update
from images.models import Gallery
from links.models import Link

class HomePageView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # use the last update on the homepage
        try:
            context['latest_update'] = Update.objects.first()
            context['gallery'] = Gallery.objects.first()
            context['link'] = Link.objects.first()
        except:
            pass
        return context

class UpdatesCreateView(LoginRequiredMixin, CreateView):

    model = Update
    fields = [
        'title',
        'slug',
        'publication_date',
        'location',
        'headline',
        'headline_img',
        'featured_img',
        'introduction',
        'content',
        'conclusion',
        'gallery',
        'links',
        'tags',
        'is_public',
    ]
    template_name_suffix = '_create_form'
    
    def get_success_url(self):
        # return the slug with the success url
        if 'slug' in self.kwargs:
            slug = self.kwargs['slug']
        else:
            return reverse('updates:update_list')
        return reverse('updates:update_detail', kwargs={'slug': slug})

    def form_valid(self, form):
        form.instance.creation_date = timezone.now()
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class UpdatesListView(ListView):

    model = Update
    paginate_by = 16 
    ordering = ['-publication_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class UpdatesDetailView(DetailView):

    model = Update

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class UpdatesUpdateView(LoginRequiredMixin, UpdateView):

    model = Update
    fields = [
        'title',
        'slug',
        'publication_date',
        'location',
        'headline',
        'headline_img',
        'featured_img',
        'introduction',
        'content',
        'conclusion',
        'gallery',
        'links',
        'tags',
        'is_public',
    ]

    template_name_suffix = '_update_form'
    
    def get_success_url(self):
        # return the slug with the success url
        if 'slug' in self.kwargs:
            slug = self.kwargs['slug']
        else:
            return reverse('updates:update_list')
        return reverse('updates:update_detail', kwargs={'slug': slug})

    #def form_valid(self, form):
    #    return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class UpdatesDeleteView(DeleteView):

    model = Update

    def get_success_url(self):
      return reverse('updates:update_list')

