from django.shortcuts import render,redirect
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from .models import Movie
from .forms import MovieForm

# Create your views here.
@require_safe
def index(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    movies=Movie.objects.all()
    context={
        'movies':movies
    }
    return render(request,'movies/index.html',context)

@require_http_methods(['POST', 'GET'])
def create(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    if request.method=='POST':
        form=MovieForm(request.POST)
        if form.is_valid():
            movie=form.save(commit=False)
            movie.author=request.user
            movie.save()
            return redirect('movies:detail',movie.pk)
    else: 
        form=MovieForm()
    context={
        'form':form
    }
    return render(request,'movies/create.html',context)

@require_safe
def detail(request,pk):
    movie=Movie.objects.get(pk=pk)
    context={
        'movie':movie
    }
    return render(request,'movies/detail.html',context)

@require_http_methods(['POST', 'GET'])
def update(request,pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    movie=Movie.objects.get(pk=pk)
    if request.method=='POST':
        form=MovieForm(request.POST, instance=movie)
        if form.is_valid():
            movie=form.save(commit=False)
            movie.author=request.user
            movie.save()
            return redirect('movies:detail', movie.pk)
    else:
        form=MovieForm(instance=movie)
    context={
        'form':form,
        'movie':movie
    }
    return render(request,'movies/update.html',context)

@require_POST
def delete(request,pk):
    movie=Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('movies:index')