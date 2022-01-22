from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import MedicinePost
from django.urls import reverse_lazy, reverse
from django.db.models import Q
from django.http import HttpResponseRedirect
from .forms import MedicineForm, EditPostForm
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied


# Create your views here.

class HomePageView(ListView):
    model = MedicinePost
    template_name = 'home.html'
    context_object_name = 'all_posts_list'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class TermsView(TemplateView):
    template_name = 'terms.html'


class NavBarView(TemplateView):
    template_name = 'navbar.html'


class MedicineListPageView(ListView):
    model = MedicinePost
    template_name = 'medicine_list.html'
    context_object_name = 'posts'


class MedicineSearchView(LoginRequiredMixin, ListView):
    model = MedicinePost
    template_name = 'search_for_medicine_results.html'
    context_object_name = 'posts'
    paginate_by = 10
    login_url = 'login'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')

        # rstrip() removes the whitespace after the end of the input
        object_list = MedicinePost.objects.filter(
            Q(medicine_name__contains=query.rstrip().lstrip())
        )
        if len(query.rstrip().lstrip()) == 0:
            return MedicinePost.objects.filter(
                Q(medicine_name__contains="nullNone")
            )
        return object_list


# POST VIEWS

class PostCreateSuccessView(TemplateView):
    template_name = 'post_create_success.html'


class PostDeleteSuccessView(TemplateView):
    template_name = 'post_delete_success.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = MedicineForm
    # model = MedicinePost
    template_name = 'new_post.html'
    # fields = ['address', 'medicine_name', 'medicine_quantity', 'expiry_date', 'medicine_image', 'post_type',
    #           'phone_number', ]
    login_url = 'login'

    success_url = reverse_lazy('post_create_success')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(PostCreateView, self).get_context_data(**kwargs)
        context['google_key'] = settings.GOOGLE_KEY
        return context


class PostUpdateView(UpdateView):
    model = MedicinePost
    template_name = 'post_edit.html'
    fields = ['address', 'medicine_name', 'medicine_quantity', 'expiry_date', 'medicine_image', 'post_type',
              'phone_number', 'extra_info']
    success_url = reverse_lazy('my_posts')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):  # new
        obj = self.get_object()

        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PostUpdateView, self).get_context_data(**kwargs)
        context['google_key'] = settings.GOOGLE_KEY
        return context


class PostDeleteView(DeleteView):
    model = MedicinePost
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_delete_success')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):  # new
        obj = self.get_object()

        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class PostDetailView(DetailView):
    model = MedicinePost
    template_name = 'post_detail.html'
    context_object_name = 'post'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['google_key'] = settings.GOOGLE_KEY
        return context


class MyPostsListView(LoginRequiredMixin, ListView):
    model = MedicinePost
    template_name = 'my_posts.html'
    login_url = 'login'
    paginate_by = 10
    context_object_name = "posts"

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return MedicinePost.objects.filter(author=self.request.user)
        return MedicinePost.objects.filter(author=None)


class PasswordResetView(TemplateView):
    template_name = 'registration/password_reset_form.html'


class PasswordChangeView(TemplateView):
    template_name = 'registration/password_change_form.html'
