from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Autor, Categoria, Post
from .forms import AutorForm, CategoriaForm, PostForm, BusquedaPostForm

def home(request):
    ultimos = Post.objects.order_by('-fecha')[:5]
    return render(request, 'home.html', {'ultimos': ultimos})

def lista_posts(request):
    posts = Post.objects.order_by('-fecha')
    return render(request, 'lista_posts.html', {'posts': posts})

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AutorForm()
    return render(request, 'autor_form.html', {'form': form})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoriaForm()
    return render(request, 'categoria_form.html', {'form': form})

def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_posts')
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})

def buscar_post(request):
    resultados = []
    form = BusquedaPostForm(request.GET or None)
    if form.is_valid() and form.cleaned_data.get('query'):
        q = form.cleaned_data['query']
        resultados = Post.objects.filter(
            Q(titulo__icontains=q) | Q(contenido__icontains=q)
        ).order_by('-fecha')
    return render(request, 'buscar_post.html', {'form': form, 'resultados': resultados})
