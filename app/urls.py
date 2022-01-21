from django.urls import path

from .views import HomePageView, AboutPageView, PostDetailView, PostUpdateView, PostDeleteView, PostCreateView, NavBarView, \
    MedicineListPageView, MedicineSearchView, TermsView, MyPostsListView, PostCreateSuccessView, PostDeleteSuccessView, \
    PasswordResetView, PasswordChangeView

urlpatterns = [
    # home page url pattern
    path('', HomePageView.as_view(), name='home'),

    # url patterns related to posts
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('my-posts/', MyPostsListView.as_view(), name='my_posts'),

    # other url patterns
    path('about/', AboutPageView.as_view(), name='about'),
    path('medicine_list/', MedicineListPageView.as_view(), name='medicine_list'),
    path('search/', MedicineSearchView.as_view(), name='medicine_search'),
    path('navbar/', NavBarView.as_view(), name='nav'),
    path('terms/', TermsView.as_view(), name='terms'),
    path('create-post-success/', PostCreateSuccessView.as_view(), name='post_create_success'),
    path('delete-post-success/', PostDeleteSuccessView.as_view(), name='post_delete_success'),
    path('users/password_reset/', PasswordResetView.as_view(), name='password_reset_form'),
    path('users/password_change/', PasswordChangeView.as_view(), name='password_change_form'),
]
