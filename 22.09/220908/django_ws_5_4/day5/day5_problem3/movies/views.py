from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .models import Movies
from .forms import MovieForm

# Create your views here.
@require_safe
def index(request):
    movies=Movies.objects.all()
    context={
        'movies':movies
    }
    return render(request, 'movies/index.html',context)

@require_http_methods(['GET','POST'])
def create(request):
    if request.method=='POST':
        form=MovieForm(request.POST)
        if form.is_valid():
            movie=form.save()
            return redirect('movies:detail',movie.pk)
    else:
        form=MovieForm()
    context={
        'form':form
    }
    return render(request,'movies/create.html',context)

@require_safe
def detail(request,pk):
    movie=get_object_or_404(Movies,pk=pk)
    context={
        'movie':movie
    }
    return render(request,'movies/detail.html',context)

@require_POST
def delete(request,pk):
    movie=Movies.objects.get(pk=pk)
    movie.delete()
    return redirect('movies:index')

@require_http_methods(['GET','POST'])
def update(request,pk):
    movie=Movies.objects.get(pk=pk)
    if request.method=='POST':
        form = MovieForm(request.POST, instance=movie)
        # form = ArticleForm(data=request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)
    context = {
        'form': form,
        'movie': movie,
    }
    return render(request, 'movies/update.html', context)