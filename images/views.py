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
from accounts.mixins import UserObjectProtectionMixin
from accounts.models import User, Member
from .forms import ImageForm
from .models import Image, Gallery, Piece

# Create your views here.

class ImageCreateView(LoginRequiredMixin, CreateView):

    model = Image
    form_class = ImageForm
    template_name_suffix = '_create_form'

    def form_valid(self, form):
        form.instance.creation_date = timezone.now()
        form.instance.user = self.request.user
        return super().form_valid(form)
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        else:
            return reverse('images:image_detail', kwargs={'pk': self.object.pk})

class ImageListView(ListView):

    model = Image
    paginate_by = 30
    queryset = Image.objects.filter(is_public=True)
    ordering = ['-weight', '-creation_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ImageUserListView(ListView):

    model = Image
    paginate_by = 30 
    ordering = ['is_public', '-creation_date']

    def get_queryset(self, *args, **kwargs):
        target = User.objects.get(username=self.kwargs['user'])
        return Image.objects.filter(user=target)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        target = User.objects.get(username=self.kwargs['user'])
        context['user_only'] = True
        context['target'] = target 
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

class ImageUpdateView(LoginRequiredMixin, UserObjectProtectionMixin, UpdateView):

    model = Image
    form_class = ImageForm
    template_name_suffix = '_update_form'
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
		
class ImageDeleteView(LoginRequiredMixin, UserObjectProtectionMixin, DeleteView):

    model = Image
    success_url = reverse_lazy('images:image_list')
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class GalleryCreateView(LoginRequiredMixin, CreateView):

    model = Gallery
    fields = ['title', 'slug', 'cover_image', 'caption', 'pieces', 'tags', 'is_public']
    template_name_suffix = '_create_form'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        elif 'slug' in self.kwargs:
            slug = self.kwargs['slug']
            return reverse('images:gallery_detail', kwargs={'slug': slug})
        else:
            return reverse('studio')	

    def get_success_url(self):
        # return the slug with the success url
        if 'slug' in self.kwargs:
            slug = self.kwargs['slug']
        else:
            return reverse('images:gallery_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class GalleryListView(ListView):

    paginate_by = 16 
    queryset = Gallery.objects.filter(is_public=True)
    ordering = ['-weight', '-creation_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class GalleryUserListView(LoginRequiredMixin, ListView):

    paginate_by = 16
    ordering = ['-weight', '-creation_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_only'] = True
        return context

    def get_queryset(self):
        return Gallery.objects.filter(user=self.request.user)

class GalleryDetailView(DetailView):

    model = Gallery

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

class GalleryUpdateView(LoginRequiredMixin, UserObjectProtectionMixin, UpdateView):

    model = Gallery
    fields = ['title', 'slug', 'cover_image', 'caption', 'pieces', 'tags', 'is_public']
    template_name_suffix = '_update_form'
	
    def get_success_url(self):
        # return the slug with the success url
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        if 'slug' in self.kwargs:
            slug = self.kwargs['slug']
        else:
            return reverse_lazy('images:gallery_list')
        return reverse_lazy('images:gallery_detail', kwargs={'slug': slug})


class GalleryDeleteView(LoginRequiredMixin, UserObjectProtectionMixin, DeleteView):

    model = Gallery
	
    def get_success_url(self):
        return reverse_lazy('images:gallery_list')
      
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class PieceCreateView(LoginRequiredMixin, CreateView):

    model = Piece
    fields = [
        'slug',
        'image',
        'detail_images',
        'description',
        'number',
        'artists',
        'medium',
        'collection',
        'is_public',
        'price',
        'currency',
        'is_sold',
        'contact_name',
        'contact_email',
        'contact_link',
    ]
    template_name_suffix = '_create_form'
 
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        else:
            if 'slug' in self.kwargs:
                slug = self.kwargs['slug']
            else:
                return reverse('images:piece_list')
            return reverse('images:piece_detail', kwargs={'slug': slug})

class PieceListView(ListView):

    paginate_by = 30
    queryset = Piece.objects.filter(is_public=True)
    ordering = ['-weight', '-creation_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class PieceUserListView(LoginRequiredMixin, ListView):

    paginate_by = 30

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_only'] = True
        return context

    def get_queryset(self):
        return Piece.objects.filter(
            user=self.request.user
        ).order_by('is_public', '-creation_date')

class PieceDetailView(DetailView):

    model = Piece

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

class PieceUpdateView(LoginRequiredMixin, UserObjectProtectionMixin, UpdateView):

    model = Piece
    fields = [
        'image',
        'detail_images',
        'description',
        'number',
        'artists',
        'medium',
        'collection',
        'price',
        'currency',
        'is_sold',
        'is_public',
        'contact_name',
        'contact_email',
        'contact_link',
    ]
    template_name_suffix = '_update_form'
	
    def get_success_url(self):
        # return the slug with the success url
        if 'slug' in self.kwargs:
            slug = self.kwargs['slug']
        else:
            return reverse('images:pieces_list')
        return reverse('images:piece_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
		
class PieceDeleteView(LoginRequiredMixin, UserObjectProtectionMixin, DeleteView):

    model = Piece
	
    def get_success_url(self):
        return reverse_lazy('studio')
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def promote_piece(request, pk):
    m = get_object_or_404(Member, pk=request.user.pk)
    o = get_object_or_404(Piece, pk=pk)
    successful, link, weight = m.allocate_weight(o)
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
    return HttpResponseRedirect(reverse('images:piece_list'))

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
