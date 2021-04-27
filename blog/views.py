from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import CommentForm
from .models import Post, Comment

# Create your views here.

class HomePageView(ListView):
  model = Post
  template_name = 'homepage.html'
  context_object_name = 'all_blogs_list'

class BlogListView(ListView):
  model = Post
  template_name = 'home.html'
  context_object_name = 'posts'

# def BlogDetailView(request,pk):
#    post = get_object_or_404(Post, pk= pk)
#    comments = post.comments.all()
#    new_comment = None
#    template_name = 'blog_details.html'

class BlogDetailView(DetailView):
  model = Post
  template_name = 'post_detail.html'

class BlogCreateView(CreateView):
  model = Post
  template_name = 'post_new.html'
  fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView):
  model = Post
  template_name = 'post_edit.html'
  fields = ['title', 'body']

class BlogDeleteView(DeleteView):
  model =  Post
  template_name = 'post_delete.html'
  success_url = reverse_lazy('home')