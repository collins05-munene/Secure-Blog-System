from django.http import HttpResponse    
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post
from .forms import PostCreationForm
# Create your views here.
class Home(LoginRequiredMixin, View):
    def get(self, request):
        posts = Post.objects.all()
        context = {'posts': posts}
        return render(request, 'apps/home.html', context)
    
class CreatePost(LoginRequiredMixin, View):
    def get(self, request):
        form = PostCreationForm()
        context = {'form': form}
        return render(request, 'apps/create-post.html', context)
    
    def post(self, request):
        form = PostCreationForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('home')
        post.author = request.user
                    
        
        context = {'form': form}
        return render(request, 'apps/create-post.html', context)

class UpdatePost(LoginRequiredMixin, View):
    def get(self, request, id):
        post = Post.objects.get(id=id)
        update_form = PostCreationForm(instance=post)

        if post.author != request.user:
                return HttpResponse("Not allowed to perform this action")
        
        context = {'post': post, "form": update_form}
        return render(request, 'apps/create-post.html', context)
    
    def post(self, request, id):
        post = Post.objects.get(id=id)
        update_form = PostCreationForm(request.POST, instance=post)

        
        if update_form.is_valid() and post.author == request.user:
            print('Author:', post.author)
            print('User:', request.user)
            post = update_form.save(commit=False)
            post.save()

            return redirect('home')            
        
        context = {'post': post, 'form': update_form}
        return render(request, 'apps/create-post.html', context)
