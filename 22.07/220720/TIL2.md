# 함수
코드의 재사용을 위해 함수를 사용한다.

함수는 이름이 붙여진 코드 조각이라고 생각하자.

## 함수 기본 구조
- 선언과 호출
- 입력
- 문서화
- 범위
- 결과값
  
```python
def 함수이름(parameters):
    body
    return None
```

## 선언과 호출
함수의 선언은 def키워드를 활용함

들여쓰기를 통해 Function body를 작성함

함수는 parameter를 넘겨줄 수 있음

함수는 동작 후에 return을 통해 결괏값을 전달함

```python
def add(x,y):
    return x+y #선언

add(2,3) #호출
```

## 함수의 결과값

Void function
- 명시적인 return 값이 없는 경우, None을 반환하고 종료

Value returning function
- 함수 실행 후, return구문을 통해 값 반환
- return을 하게되면 값 반환 후 함수가 바로 종료

```python
def minus_and_product(x,y):
    return x - y, x * y

y = minus_and_product(4,5)
print(y)#(-1,20)
print(type(y))#<class 'tuple'>
```

## 함수의 입력

- Parameter : 함수를 정의할 때 함수 내부에서 사용되는 변수
- Argument : 함수를 호출 할 때, 넣어주는 값

### Argument

함수 호출 시 함수의 parameter를 통해 전달되는 값

Argument는 소괄호 안에 할당 func_name(argument)
- 필수 Argument : 반드시 전달되어야하는 argument
- 선택 Argument : 값을 전달하지 않아도 되는 경우는 기본값이 전달

#### positional argument
- 기본적으로 함수 호출 시 argument 위치에 따라 함수 내에 전달됨
```python
def add(x,y):
    return x+y

add(2,3)

def add(x,y):
    #x=2,y=3
    return x+y #5
```

#### Keyword Argument
- 직접 변수의 이름으로 특정 Argument를 전달할 수 있음
- Keyword argument 다음에 Positional argument를 활용할 수 없음
```python
def add(x,y):
    return x+y

add(2,3)
add(x=2,y=5)
add(2,y=5)
add(x=2,5)#-> Error 발생
```

#### Default Arguments Values
- 기본값을 지정하여 함수 호출 시 argument 값을 설정하지 않도록 함
- 정의됭 것 보다 더 적은 개수의 argument들로 호출될 수 있음

```python
def add(x,y=0):
    return x+y #선언

add(2)

def add(x,y=0):
    #x=2
    return x+y #2
```

### 가변인자(*args)
가변인자란?
- 여러 개의 Positional Argument를 하나의 필수 parameter로 받아서 사용
- 몇개의 Positional Argument를 받을지 모르는 함수를 정의할 때 유용

```python
def add(*args):
    for arg in args:
        print(arg)

add(2)#2
add(2,3,4,5)
'''
2
3
4
5
'''
```

### 패킹/언패킹
패킹 : 여러개의 데이터를 묶어서 변수에 할당하는것

언패킹 : 시퀀스 속으 요소들을 여러개의 변수에 나누어 할당하는 것
```python
numbers = (1,2,3,4,5) #패킹
a,b,c,d,e=numbers #언패킹

a,b,*rest=numbers # 1 2 [3 4 5]
```

언패킹시 변수의 개수와 할당하고자 하는 요소의 갯수가 동일해야함

언패킹시 왼쪽의 변수에 '*'를 붙이면 할당하고 남은 요소를 리스트에 담을 수 있음

### 가변 키워드 인자(**kwargs)
- 몇 개의 키워드 인자를 받을 지 모르는 함수를 정의할 때 유용
- **kwargs는 딕셔너리로 묶여 처리되며, parameter에 **을 붙여 표현함!

```python
def family(**kwargs):
    for key, value in kwargs.items():
        print(key, ':', value)
family(father='아부지',mother='어무니', baby='아기')
'''
father : 아부지
mother : 어무니
baby : 아기
'''
```

## Python의 범위
함수는 코드 내부에 local scope를 생성하며 그 외의 공간인 global scope로 구분

- scope
   - global scope : 코드 어디에서든 참조할 수 있는 공간
   - local scope : 함수가 만든 scope 함수 내부에서만 참조 가능
- variable
   - global variable : global scope에 정의된 변수
   - local variable : local scope에 정의된 변수

### 이름 검색 규칙
#### LEGB Rule
- local scope : 지역범위
- Enclosed scope : 지역 범위 한단계 위 범위
- Global scope : 최상단에 위치한 범위
- Built-in scope : 모든것을 담고있는 범위

### global문
현재 코드 블록 전체에 적용되며, 나열된 식별자가 global variable임을 나타냄
- global에 나열된 이름은 같은 코드 블록에서 global 앞에 등장할 수 없음
- global에 나열된 이름은 parameter, for루프 대상, 클래스/함수 정의 등으로 정의도지 않아야 함!

```python
#함수 내부에서 글로벌 변수 변경하기
a = 10
def func1():
    global a
    a=3
print(a)#10
func1()
print(a)#3

#global 주의사항1
a = 10
def func1():
    print(a)#global a 선언 전에 사용
    global a
    a=3
print(3)
func1()
print(a)
# SyntaxError: name 'a' is used prior to global declaration

#global 주의사항2
a = 10
def func1(a):
    global a # parameter에 global사용 불가
    a=3
print(a)
func1(3)
print(a)
# SyntaxError: name 'a' is parameter and global
```

### nonlocal
- global을 제외하고 가장 가까운 (둘러싸고있는) scope의 변수를 연결하도록 함
    - nonlocal에 나열된 이름은 같은 코드 블록에서 nonlocas 앞에 등장할 수 없음
    - nonlocal에 나열된 이름은 parameter, for루프 대상, 클래스/함수 정의 등으로 정의도지 않아야 함!
- global과는 달리 이미 존재하는 이름과의 연결만 가능함

```python
#nonlocal 예시
x = 0
def func1():
    x = 1
    def func2():
        nonlocal x
        x = 2
    func2()
    print(x) # 2
func1()
print(x) # 0
```

## 함수 응용
- filter(함수,데이터구조) : 순회 가능한 데이터구조의 모든 요소에 함수를 적용하고, 그 결과가 True인 것들을 filter object로 반환

```python
def odd(n):
    return n%2
numbers=[1,2,3]
result=filter(odd,numbers)
print(result,type(result))#<filter object at 0x000001Fb4B217F><class 'filter'>
print(list(result))#[1, 3]
```

- zip(*iterables) : 복수의 iterable을 모아 튜플을 원소로 하는 zip object를 반환

```python
girls=['jane','ashley']
boys=['justin','eric']
pair=zip(girls,boys)
print(pair,type(pair))#<zip object at 0x000001Fb4B217F><class 'zip'>
print(list(pair))#[('jane','justin'),('ashley','eric')]
```

# 모듈
- 모듈 : 다양한 기능을 하나의 파일로
- 패키지 : 다양한 파일을 하나의 폴더로
- 라이브러리 : 다양한 패키지를 하나의 묶음으로
- pip : 이것을 관리하는 관리자

## 모듈과 패키지 호출
```python
import module
from module import var,function,Class
from module import *#전부 가져오는것

from package import module
from package.module import var, function, Class
```