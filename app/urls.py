from django.urls import path

from .views import HomePageView, AboutPageView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, NavBarView, MedicineListPageView, MedicineSearchView, PostView

urlpatterns = [
    # home page url pattern
    path('', HomePageView.as_view(), name='home'),

    # url patterns related to posts
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/new/', PostView.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),

    # other url patterns
    path('about/', AboutPageView.as_view(), name='about'),
    path('medicine_list/', MedicineListPageView.as_view(), name='medicine_list'),
    path('search/', MedicineSearchView.as_view(), name='medicine_search'),
    path('navbar/', NavBarView.as_view(), name='nav'),
]
