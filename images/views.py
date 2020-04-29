from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    )
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views.generic.edit import CreateView, FormView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.core.files.images import ImageFile
from accounts.models import Member
from .models import Image, Gallery

# Create your views here.

class ImageCreateView(LoginRequiredMixin, CreateView):

    model = Image
    fields = ['image_file', 'title', 'caption', 'credit', 'is_public']
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
    paginate_by = 12 
    ordering = ['-weight', '-creation_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ImageDetailView(DetailView):

    model = Image

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Tell the template whether or not to render the marshmallow
        u = self.request.user
        if u.is_authenticated:
            # get the users Member function
            m = get_object_or_404(Member, pk=u.pk)
            context['can_allocate'] = m.check_can_allocate_weight
        else:
            context['can_allocate'] = False
        return context

class ImageUpdateView(LoginRequiredMixin, UpdateView):

    model = Image
    fields = ['image_file', 'caption', 'title', 'credit', 'is_public']
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

class GalleryCreateView(LoginRequiredMixin, CreateView):

    model = Gallery
    fields = ['title', 'slug', 'caption', 'images', 'tags', 'is_public']
    template_name_suffix = '_create_form'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
	
    def get_success_url(self):
        # return the slug with the success url
        if 'slug' in self.kwargs:
            slug = self.kwargs['slug']
        else:
            return reverse('images:gallery_list')
        return reverse('images:gallery_detail', kwargs={'slug': slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class GalleryListView(ListView):

    queryset = Gallery.objects.filter(is_public=True)
    paginate_by = 32
    ordering = ['-weight', '-creation_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class GalleryDetailView(DetailView):

    model = Gallery
    paginate_by = 32

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Tell the template whether or not to render the marshmallow
        u = self.request.user
        if u.is_authenticated:
            # get the users Member function
            m = get_object_or_404(Member, pk=u.pk)
            context['can_allocate'] = m.check_can_allocate_weight
        else:
            context['can_allocate'] = False
        return context

class GalleryUpdateView(LoginRequiredMixin, UpdateView):

    model = Gallery
    fields = ['title', 'slug', 'caption', 'images', 'tags', 'is_public']
    template_name_suffix = '_update_form'
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
		
class GalleryDeleteView(LoginRequiredMixin, DeleteView):

    model = Gallery
    success_url = reverse_lazy('')
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def promote_image(request, pk):
    m = get_object_or_404(Member, pk=request.user.pk)
    o = get_object_or_404(Image, pk=pk)
    successful, link, weight  = m.allocate_weight(o)
    if successful:
        messages.add_message(
            request, messages.INFO,
            'You gave a marshmallow to {} weighing {}'.format(
                link,
                round(weight, 2)
            )
       )
    else:
        messages.add_message(
            request,
            messages.ERROR,
            'You failed to give a marshmallow to {}'.format(link)
        )
    return HttpResponseRedirect(reverse('images:image_list'))

def promote_gallery(request, pk):
    m = get_object_or_404(Member, pk=request.user.pk)
    o = get_object_or_404(Gallery, pk=pk)
    successful, link, weight  = m.allocate_weight(o)
    if successful:
        messages.add_message(
            request, messages.INFO,
            'You gave a marshmallow to {} weighing {}'.format(
                link,
                round(weight, 2)
            )
       )
    else:
        messages.add_message(
            request,
            messages.ERROR,
            'You failed to give a marshmallow to {}'.format(link)
        )
    return HttpResponseRedirect(reverse('images:gallery_list'))
