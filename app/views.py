from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import MedicinePost
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import HttpResponseRedirect
from .forms import MedicineForm


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


class BlogDetailView(DetailView):
    model = MedicinePost
    template_name = 'post_detail.html'
    context_object_name = 'post'


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


class BlogCreateView(CreateView):
    model = MedicinePost
    template_name = 'new_post.html'
    fields = '__all__'


class BlogUpdateView(UpdateView):
    model = MedicinePost
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):
    model = MedicinePost
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_new')


# MAPBOX VIEW

class PostView(CreateView):
    form_class = MedicineForm
    # model = MedicinePost
    # fields = ['address', 'medicine_name', 'medicine_quantity', 'expiry_date', 'medicine_image', 'post_type']
    template_name = 'new_post.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['addresses'] = Post.objects.filter(address__exact=Post.address)
        context['addresses'] = MedicinePost.objects.filter(address=self.model.address)
        return context

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        else:
            return render(request, self.template_name, {'form': form})

