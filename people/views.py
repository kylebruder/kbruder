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
from accounts.mixins import UserObjectProtectionMixin
from accounts.models import Member
from people.models import Artist

# Create your views here.

class ArtistCreateView(LoginRequiredMixin, CreateView):

    model = Artist
    fields = [
        'name',
        'slug',
        'home_town',
        'image',
        'links',
        'statement',
        'media',
        'is_public',
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
                return reverse('people:artist_list')
            return reverse_lazy('people:artist_detail', kwargs={'slug': slug})


class ArtistListView(ListView):

    queryset = Artist.objects.filter(is_public=True)
    paginate_by = 16
    ordering = ['-weight', '-creation_date',]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ArtistUserListView(ListView):

    model = Artist
    paginate_by = 16

    def get_queryset(self):
        return Artist.objects.filter(
            user=self.request.user
        ).order_by('is_public', '-creation_date')

    def get_context_date(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_only'] = True

class ArtistDetailView(DetailView):

    model = Artist

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Tell the template whether or not to render the marshmallow
        u = self.request.user
        if u.is_authenticated:
            print("AUTH OK!")
            # get the users Member function
            m = get_object_or_404(Member, pk=u.pk)
            context['can_allocate'] = m.check_can_allocate_weight()
        else:
            context['can_allocate'] = False
        artist = Artist.objects.get(slug=self.object.slug)
        context['pieces'] = artist.piece_set.all()
        return context

class ArtistUpdateView(LoginRequiredMixin, UserObjectProtectionMixin, UpdateView):

    model = Artist
    fields = [
        'name',
        'home_town',
        'image',
        'links',
        'statement',
        'media',
        'is_public',
    ]
    template_name_suffix = '_update_form'

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        else:
            if 'slug' in self.kwargs:
                slug = self.kwargs['slug']
            else:
                return reverse('people:artist_list')
            return reverse_lazy('people:artist_detail', kwargs={'slug': slug})

class ArtistDeleteView(LoginRequiredMixin, UserObjectProtectionMixin, DeleteView):

    model = Artist

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('people:artist_list')

def promote_artist(request, pk):
    m = get_object_or_404(Member, pk=request.user.pk)
    o = get_object_or_404(Artist, pk=pk)
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
    return HttpResponseRedirect(reverse('people:artist_list'))
