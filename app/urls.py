from django.urls import path

from .views import HomePageView, AboutPageView, BlogDetailView, BlogCreateView, BlogUpdateView, \
    BlogDeleteView, NavBarView, HaveMedicineListPageView, HaveMedicineSearchView, NeedMedicineSearchView, DonatePostView, ReceiveDonationPostView, NeedMedicineListPageView

urlpatterns = [
    # home page url pattern
    path('', HomePageView.as_view(), name='home'),

    # url patterns related to posts
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('donate-post/new/', DonatePostView.as_view(), name='donate_post_new'),
    path('receive-donation-post/new/', ReceiveDonationPostView.as_view(), name='receive_donation_post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),

    # other url patterns
    path('about/', AboutPageView.as_view(), name='about'),
    path('have_medicine_list/', HaveMedicineListPageView.as_view(), name='have_medicine_list'),
    path('need_medicine_list/', NeedMedicineListPageView.as_view(), name='need_medicine_list'),
    path('donate-search/', HaveMedicineSearchView.as_view(), name='donate_search'),
    path('need-search/', NeedMedicineSearchView.as_view(), name='get_donation_search'),
    path('navbar/', NavBarView.as_view(), name='nav'),
]
