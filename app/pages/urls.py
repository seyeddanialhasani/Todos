from django.urls import path
from . import views

urlpatterns = [
    path("", views.TweetsListView.as_view(), name="tweets_list"),
    path("create/", views.TweetsCreateView.as_view(), name="tweets_create"),
    path("<int:pk>/update/", views.TweetsUpdateView.as_view(), name="tweets_update"),
    path("<int:pk>/delete/", views.TweetsDeleteView.as_view(), name="tweets_delete"),
    path("<int:pk>/", views.TweetsDetailView.as_view(), name="tweets_detail"),
]
