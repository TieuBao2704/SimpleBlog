from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate


# Create your views here.

# @login_required(login_url='registration/register.html')
class IndexPost(ListView):
    # login_url = 'login'
    model = Post
    template_name = "theblog/homepage.html"

    # Order by attribute of model
    ordering = ['time']


class DetailPost(DetailView):
    model = Post
    template_name = "theblog/article_detail.html"


class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = "theblog/addpost.html"
    # fields = "__all__"


class EditUpdatePost(UpdateView):
    model = Post
    template_name = "theblog/update_post.html"
    fields = ['title', 'author', 'body']


class DeletePost(DeleteView):
    model = Post
    template_name = "theblog/remove.html"
    success_url = reverse_lazy('theblog:homepage')


#autheticate user



