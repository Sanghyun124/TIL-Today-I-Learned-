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
