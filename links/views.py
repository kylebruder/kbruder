from django.contrib import messages
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    )
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormView, UpdateView, DeleteView
from django.views.generic.list import ListView
from accounts.mixins import UserObjectProtectionMixin
from accounts.models import Member
from .forms import LinkForm
from .models import Link

# Create your views here.

class LinkCreateView(LoginRequiredMixin, CreateView):

    model = Link
    form_class = LinkForm

    def get_success_url(self):
        return reverse('links:link_user_list', kwargs={'user': self.request.user})

    def form_valid(self, form):
        form.instance.creation_date = timezone.now()
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_form_kwargs(self):
        kwargs = super(LinkCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class LinkListView(ListView):

    model = Link
    paginate_by = 16 
    ordering = ['-weight', '-creation_date',]
    queryset = Link.objects.filter(is_public=True)

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

class LinkUserListView(LoginRequiredMixin, ListView):

    model = Link
    paginate_by = 16
    ordering = ['-publication_date']

    def get_queryset(self):
        return Link.objects.filter(
            user=self.request.user,
        ).order_by(
            'is_public',
            '-publication_date',
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_only'] = True
        return context


class LinkDetailView(DetailView):

    model = Link
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class LinkUpdateView(LoginRequiredMixin, UserObjectProtectionMixin, UpdateView):

    model = Link
    form_class = LinkForm

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        else:
            return reverse_lazy('links:link_detail',
                kwargs={'slug': self.object.slug}
            )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_form_kwargs(self):
        kwargs = super(UpdatesCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class LinkDeleteView(LoginRequiredMixin, UserObjectProtectionMixin, DeleteView):

    model = Link

    def get_success_url(self):
        return reverse('links:link_user_list',
            kwargs={'user': self.request.user}
        )
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def publish_link_view(request, pk): 
    user = request.user
    instance = get_object_or_404(Link, pk=pk) 
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
            'links:link_list',
        )
    )
def promote_link(request, pk):
    m = get_object_or_404(Member, pk=request.user.pk)
    o = get_object_or_404(Link, pk=pk)
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
    return HttpResponseRedirect(reverse('links:link_list'))
