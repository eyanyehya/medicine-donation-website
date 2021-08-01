from django.urls import path

from .views import HomePageView, AboutPageView, BlogDetailView, BlogCreateView, BlogUpdateView, FormPageView, \
    BlogDeleteView, NavBarView, MedicineListPageView, SearchView, NewPostView

urlpatterns = [
    # home page url pattern
    path('', HomePageView.as_view(), name='home'),

    # url patterns related to posts
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/new/', NewPostView.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),

    # other url patterns
    path('about/', AboutPageView.as_view(), name='about'),
    path('medicine_list/', MedicineListPageView.as_view(), name='medicine_list'),
    path('search/', SearchView.as_view(), name='search_results'),
    path('navbar/', NavBarView.as_view(), name='nav'),
    path('form/', FormPageView.as_view(), name='form'),
]
