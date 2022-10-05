from django.shortcuts import render,redirect
from .models import Movie

# Create your views here.
def index(request):
    movies=Movie.objects.all()
    context={
        'movies':movies,
    }
    return render(request,'movies/index.html',context)

def new(request):
    return render(request,'movies/new.html')

def create(request):
    title=request.POST.get('title')
    audience=request.POST.get('audience')
    release_date=request.POST.get('release_date')
    genre=request.POST.get('genre')
    score=request.POST.get('score')
    poster_url=request.POST.get('poster_url')
    description=request.POST.get('description')

    movie=Movie(title=title, audience=audience, release_date=release_date, genre=genre, score=score, poster_url=poster_url, description=description)
    movie.save()
    return redirect('movies:detail',movie.pk)


def detail(request,pk):
    pk_list=list(Movie.objects.values_list('id',flat=True).order_by('id'))

    if int(pk)==pk_list[0]:
        prev=0
        nex=1
    elif int(pk)==pk_list[-1]:
        prev=1
        nex=0
    else :
        prev=1
        nex=1

    movie=Movie.objects.get(pk=pk)
    context={
        'movie':movie,
        'prev':prev,
        'nex':nex,
    }
    return render(request, 'movies/detail.html', context)

def edit(request,pk):
    movie=Movie.objects.get(pk=pk)
    genres=['코미디', '액션', '판타지']
    context={
        'movie':movie,
        'genres':genres
    }
    return render(request, 'movies/edit.html', context)

def update(request,pk):
    movie=Movie.objects.get(pk=pk)
    movie.title=request.POST.get('title')
    movie.audience=request.POST.get('audience')
    movie.release_date=request.POST.get('release_date')
    movie.genre=request.POST.get('genre')
    movie.score=request.POST.get('score')
    movie.poster_url=request.POST.get('poster_url')
    movie.description=request.POST.get('description')
    movie.save()

    return redirect('movies:detail',movie.pk)

def delete(request,pk):
    movie=Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('movies:index')


