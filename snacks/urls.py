from django.urls import path

from .views import AboutView, HomePageView, SnackDetailView, SnackListView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('snack', SnackListView.as_view(), name='snack_list'),
    path('snack/<int:pk>', SnackDetailView.as_view(), name='snack_detail'),
]