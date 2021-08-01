from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import HaveMedicinePost, NeedMedicinePost
from django.urls import reverse_lazy
from django.db.models import Q


# Create your views here.

class HomePageView(ListView):
    model = HaveMedicinePost
    template_name = 'home.html'
    context_object_name = 'all_posts_list'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class FormPageView(TemplateView):
    template_name = 'form.html'


class NavBarView(TemplateView):
    template_name = 'navbar.html'


class BlogDetailView(DetailView):
    model = HaveMedicinePost
    template_name = 'post_detail.html'
    context_object_name = 'post'


class HaveMedicineListPageView(ListView):
    model = HaveMedicinePost
    template_name = 'have_medicine_list.html'
    context_object_name = 'posts'


class NeedMedicineListPageView(ListView):
    model = NeedMedicinePost
    template_name = 'need_medicine_list.html'
    context_object_name = 'posts'


class HaveMedicineSearchView(ListView):
    model = HaveMedicinePost
    template_name = 'search_for_have_medicine_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        object_list = HaveMedicinePost.objects.filter(
            Q(medicine_name__contains=query) | Q(address__contains=query)
        )
        return object_list


class NeedMedicineSearchView(ListView):
    model = NeedMedicinePost
    template_name = 'search_for_need_medicine_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        object_list = NeedMedicinePost.objects.filter(
            Q(medicine_name__contains=query) | Q(address__contains=query)
        )
        return object_list


class BlogCreateView(CreateView):
    model = HaveMedicinePost
    template_name = 'donate_new_post.html'
    fields = '__all__'


class BlogUpdateView(UpdateView):
    model = HaveMedicinePost
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):
    model = HaveMedicinePost
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_new')


# MAPBOX VIEW

class DonatePostView(CreateView):
    model = HaveMedicinePost
    fields = ['address', 'medicine_name', 'medicine_quantity', 'expiry_date', ]
    template_name = 'donate_new_post.html'
    success_url = reverse_lazy('post_new')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['addresses'] = Post.objects.filter(address__exact=Post.address)
        context['addresses'] = HaveMedicinePost.objects.filter(address=self.model.address)
        return context


class ReceiveDonationPostView(CreateView):
    model = NeedMedicinePost
    fields = ['address', 'medicine_name', 'medicine_quantity', ]
    template_name = 'receive_donation_new_post.html'
    success_url = reverse_lazy('receive_donation_post_new')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['addresses'] = Post.objects.filter(address__exact=Post.address)
        context['addresses'] = HaveMedicinePost.objects.filter(address=self.model.address)
        return context
