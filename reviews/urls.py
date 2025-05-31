from django.urls import path

from reviews.apps import ReviewsConfig

from reviews.views import (ReviewListView,ReviewDeactivatedListView,ReviewCreateView,
                           ReviewDeleteView,ReviewDetailView,ReviewUpdateView)

app_name = ReviewsConfig.name

urlpatterns = [
    path('',ReviewListView.as_view(),name='reviews_list'),
    path('deactivated/',ReviewDeactivatedListView.as_view(),name='reviews_deactivated_list'),
    path('create/',ReviewCreateView.as_view(),name='reviews_create'),
    path('detail/<slug:slug>/',ReviewDetailView.as_view(),name='reviews_detail'),
    path('update/<slug:slug>/',ReviewUpdateView.as_view(),name='reviews_update'),
    path('delete/<slug:slug>/',ReviewDeleteView.as_view(),name='reviews_delete'),
]