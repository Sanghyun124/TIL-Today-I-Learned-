import random
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def greeting(request):
    # 화면에 필요한 데이터들
    foods=['사과', '바나나', '코코넛',]
    info={'name' : '박상현'}

    context={
        'foods' : foods,
        'info' : info,
    }

    return render(request,'articles/greeting.html', context)

def dinner(request):
    foods=['족발', '햄버거', '치킨', '초밥',]
    pick = random.choice(foods)

    numbers=11

    context={
        'pick':pick,
        'foods':foods,
        'numbers':numbers
    }
    return render(request,'articles/dinner.html', context)

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    message=request.GET.get('message')
    context={
        'message':message
    }

    return render(request, 'articles/catch.html',context)


def hello(request,name):
    context={
        'name':name,
    }
    return render(request, 'articles/hello.html',context)