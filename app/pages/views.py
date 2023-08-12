from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    UpdateView,
    DeleteView,
    DetailView,
    CreateView,
)
from .models import Tweets


# Create your views here.


class TweetsListView(ListView):
    model = Tweets
    template_name = "pages/list.html"
    context_object_name = "tweets"


class TweetsCreateView(CreateView):
    model = Tweets
    template_name = "pages/create.html"
    fields = ["text"]
    success_url = "/"


class TweetsUpdateView(UpdateView):
    model = Tweets
    template_name = "pages/update.html"
    context_object_name = "tweet"
    fields = ["text"]
    success_url = "/"


class TweetsDeleteView(DeleteView):
    model = Tweets
    template_name = "pages/delete.html"
    context_object_name = "tweet"
    success_url = "/"


class TweetsDetailView(DetailView):
    model = Tweets
    template_name = "pages/detail.html"
    context_object_name = "tweet"
