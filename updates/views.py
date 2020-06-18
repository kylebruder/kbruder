from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    )
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.core.files.images import ImageFile
from django.urls import reverse
from django.utils import timezone
from accounts.models import Member
from accounts.mixins import UserObjectProtectionMixin
from images.models import Image, Gallery, Piece
from links.models import Link
from people.models import Artist
from .forms import UpdateForm
from .models import Update

class HomePageView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # use the last update on the homepage
        
        context['update'] = Update.objects.filter(is_public=True).first()
        context['updates'] = Update.objects.filter(is_public=True).all()[1:16]
        context['gallery'] = Gallery.objects.filter(
            is_public=True
        ).order_by(
            '-weight', 
            '-creation_date'
        ).first()
        context['galleries'] = Gallery.objects.filter(
             is_public=True
        ).order_by(
            '-weight',
            '-creation_date'
        )[1:10]
        context['links'] = Link.objects.order_by(
            '-weight',
            '-creation_date'
        )[0:10]
        context['artist'] = Artist.objects.filter(
            is_public=True
        ).order_by(
            '-weight',
            '-creation_date'
        ).first()
        context['artists'] = Artist.objects.filter(
            is_public=True
        ).order_by(
            '-weight',
            '-creation_date'
        )[1:10]
        context['piece'] = Piece.objects.filter(
            is_public=True
        ).order_by(
            '-weight',
            '-creation_date'
        ).first()
        context['pieces'] = Piece.objects.filter(
            is_public=True
        ).order_by(
            '-weight',
            '-creation_date'
        )[1:10]
        return context

class UpdatesCreateView(LoginRequiredMixin, CreateView):

    model = Update
    form_class = UpdateForm
    
    def get_success_url(self, **kwargs):
        # return the slug with the success url
        if kwargs != None:
          return reverse_lazy('updates:update_detail', kwargs={'slug': self.object.slug})

    def form_valid(self, form):
        form.instance.creation_date = timezone.now()
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(UpdatesCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class UpdatesListView(ListView):

    queryset = Update.objects.filter(is_public=True)
    paginate_by = 16 
    ordering = ['-publication_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class UpdatesUserListView(ListView):

    model = Update
    paginate_by = 16 
    ordering = ['-publication_date']

    def get_queryset(self):
        return Update.objects.filter(
            user=self.request.user,
        ).order_by(
            'is_public',
            '-publication_date',
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_only'] = True
        return context

class UpdatesDetailView(DetailView):

    model = Update

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

class UpdatesUpdateView(LoginRequiredMixin, UserObjectProtectionMixin, UpdateView):

    model = Update
    form_class = UpdateForm

    def form_valid(self, form):
        form.instance.last_modified = timezone.now()
        return super().form_valid(form)
    
    def get_form_kwargs(self):
        kwargs = super(UpdatesUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        else:
            return reverse_lazy('updates:update_detail', 
                kwargs={'slug': self.object.slug}
            )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class UpdatesDeleteView(LoginRequiredMixin, UserObjectProtectionMixin, DeleteView):

    model = Update
       
    def get_success_url(self):
        return reverse('updates:update_user_list',
            kwargs={'user': self.request.user}
        )

def updates_publish_view(request, pk):
    user = request.user
    instance = get_object_or_404(Update, pk=pk)
    successful = instance.publish(instance, user)
    if successful:
        messages.add_message(
            request,
            messages.INFO,
            '{} has been published'.format(
                instance,
            )
        )
    else:
        messages.add_message(
            request,
            messages.ERROR,
            '{} could not be published'.format(
                instance,
            )
        )    
    return HttpResponseRedirect(
        reverse(
            'updates:update_detail', 
            kwargs={'slug': instance.slug}
        )
    )
    
# promote view for marshmallow weight allocation
def promote_update(request, pk):
    m = get_object_or_404(Member, pk=request.user.pk)
    o = get_object_or_404(Update, pk=pk)
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
    return HttpResponseRedirect(reverse('updates:update_list'))
