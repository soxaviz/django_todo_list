from django.shortcuts import render, redirect
from . import models
from .forms import LoginForm, RegistrationForm, CommentForm, PostForm
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.views.generic import UpdateView


def index(request):
    todo = models.Todo.objects.all()
    slides = models.HomeSlider.objects.all()
    context = {
        'slides': slides,
        'todo': todo

    }
    return render(request, 'blog_app/index.html', context)


def category_view(request, pk):
    category = models.Category.objects.get(pk=pk)
    todo = models.Todo.objects.filter(category=category)
    context = {
        'category': category,
        'todo': todo,
    }
    return render(request, 'blog_app/category.html', context)


def todo_list(request, pk):
    todo = models.Todo.objects.get(pk=pk)
    photos = models.TodoGallery.objects.filter(post=todo)
    context = {
        'todo': todo,
        'photos': photos,
    }
    return render(request, 'blog_app/todo_list.html', context)



def search(request):
    query = request.GET.get('q')  # nam
    # nam in name
    todos = models.Todo.objects.filter(name__iregex=query)
    if not query:
        todos = []
    context = {
        'todos': todos,
    }
    return render(request, 'blog_app/search_results.html', context)





def login_view(request):
    next_query = request.GET.get('next')

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,
                                password=password)
            # None, User object(1)
            if user is not None:
                login(request, user)
                if next_query:
                    return redirect(next_query)
                return redirect('index')
    else:
        form = LoginForm()

    context = {
        'form': form,
    }

    return render(request, 'blog_app/login.html', context)


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = RegistrationForm()

    context = {
        'form': form,
    }
    return render(request, 'blog_app/registration.html', context)


def logout_view(request):
    next_query = request.GET.get('next')
    logout(request)
    if next_query:
        return redirect(next_query)
    return redirect('index')