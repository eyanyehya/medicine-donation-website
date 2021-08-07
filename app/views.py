from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import MedicinePost
from django.urls import reverse_lazy, reverse
from django.db.models import Q
from django.http import HttpResponseRedirect
from .forms import MedicineForm
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


class MedicineSearchView(ListView):
    model = MedicinePost
    template_name = 'search_for_medicine_results.html'
    context_object_name = 'posts'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        object_list = MedicinePost.objects.filter(
            Q(medicine_name__contains=query) | Q(address__contains=query)
        )
        return object_list


# POST VIEWS

class PostCreateView(LoginRequiredMixin, CreateView):
    # form_class = MedicineForm
    model = MedicinePost
    template_name = 'new_post.html'
    fields = ['address', 'medicine_name', 'medicine_quantity', 'expiry_date', 'medicine_image', 'post_type',
              'phone_number', ]
    login_url = 'login'

    # success_url = reverse_lazy('home')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # context['addresses'] = Post.objects.filter(address__exact=Post.address)
    #     context['addresses'] = MedicinePost.objects.filter(address=self.model.address)
    #     return context

    # def get(self, request, *args, **kwargs):
    #     form = self.form_class()
    #     return render(request, self.template_name, {'form': form})

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST, request.FILES)
    #     # userform = settings.AUTH_USER_MODEL(request.POST, request.FILES)
    #     # form = MedicineForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.instance.user = request.user
    #         form.save()
    #         messages.success(request, request.user)
    #         # form.instance.user = form.save(commit=True)
    #         # form.save()
    #         return redirect(self.success_url)
    #     else:
    #         return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = MedicinePost
    template_name = 'post_edit.html'
    fields = ['address', 'medicine_name', 'medicine_quantity', 'expiry_date', 'medicine_image', 'post_type',
              'phone_number']
    success_url = reverse_lazy('medicine_list')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):  # new
        obj = self.get_object()

        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class PostDeleteView(DeleteView):
    model = MedicinePost
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_new')
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


class MyPostsListView(ListView):
    model = MedicinePost
    template_name = 'my_posts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['myPosts'] = MedicinePost.objects.filter(author=self.request.user)
        return context



