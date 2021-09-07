from django.shortcuts import render, get_object_or_404
# LoginRequired mixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
# generic django view
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    )
from .models import Post
from django.contrib.auth.models import User

# a function based view


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

# class based view
# inherits from ListView


class PostListView(ListView):
    model = Post

    # specifying which template to use
    template_name = 'blog/home.html'

    # specifying which variable contains the objects that will be
    # iterated over
    context_object_name = 'posts'

    # changing the ordering of the query
    # newest first -date_posted
    # oldest first date_posted
    ordering = ['-date_posted']

    # gives some pagination
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

# example of minimal code
# object to be iterated over is assigned to a variable
# called object by default


class PostDetailView(DetailView):
    # all that you need to specify is the name of the model
    model = Post

# inherits from LoginRequiredMixin and CreateView
# must provide the fields for the form
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # overriding the form_valid method
    def form_valid(self, form):
        # set the author of the post to the currently logged in user
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # overriding the form_valid method
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    # check if a user passes a specified condition or conditions
    def test_func(self):
        # get the post that is currently being updated
        post = self.get_object()
        # check if the user updating the post is the same as the author
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    # overriding the form_valid method
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    # check if a user passes a specified condition or conditions
    def test_func(self):
        # get the post that is currently being updated
        post = self.get_object()
        # check if the user updating the post is the same as the author
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
