from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy
from django.db.models import Q


# Create your views here.

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class FormPageView(TemplateView):
    template_name = 'form.html'


class NavBarView(TemplateView):
    template_name = 'navbar.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


class MedicineListPageView(ListView):
    model = Post
    template_name = 'medicine_list.html'
    context_object_name = 'posts'


class SearchView(ListView):
    model = Post
    template_name = 'search_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
            Q(medicine_name__contains=query) | Q(address__contains=query)
        )
        return object_list


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_new')


# MAPBOX VIEW

class NewPostView(CreateView):
    model = Post
    fields = ['address', 'medicine_name', 'medicine_quantity', 'expiry_date', ]
    template_name = 'post_new.html'
    success_url = reverse_lazy('post_new')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['addresses'] = Post.objects.filter(address__exact=Post.address)
        context['addresses'] = Post.objects.filter(address=self.model.address)
        return context
