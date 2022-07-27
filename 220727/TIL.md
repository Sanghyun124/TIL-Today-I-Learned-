# 객체지향 프로그래밍

객체지향 프로그래밍 > 프로그래밍을 하는 방법 중 하나.

메세지를 주고받는다 > 메소드(함수)를 사용한다

데이터를 처리한다 > 객체 안에 정보를 저장하거나 메소드를 통해 가공한다.

현실세계를 프로그램 설계에 반영하는 방법이다.

#

## 객체지향의 장점/단점
- 장점
  - 클래스 단위로 모듈화 시켜 개발할 수 있다.
  - 객체 > 사용자 정의 자료구조처럼 사용한다
  - 필요한 부분만 골라서 수정할 수 있다. > 프로그램의 유지보수가 쉬워진다

- 단점
  - 설계시 많은 노력과 시간이 필요하다.
  - 실행속도가 상대적으로 느리다.
#
## 객체
속성과 행동으로 구성된 모든 것

가수로 객체를 만들때

가수의 속성 > 그 가수를 표현할 수 있는 특징(데이터:어떤 값을 가지고 있는지)

ex) 생년월일,국적,이름,대표곡 등 데이터를 저장할 수 있음  
가수의 행동 > 그 가수가 동작하는 것들(메소드:어떤 행동을 하는지 정의하는것)

ex) 랩하기,노래하기,댄스

#
## 클래스와 객체
클래스 : 객체를 어떻게 만들어야하는지 나와있는 설계도
(객체의 구성이 어떻게 되어있는지 : 속성은 어떻게 되어있고, 행동은 무엇무엇이 있는지
)

가수 클래스
가수의 속성 : 이름, 대표곡, 생년월일, 국적
가수의 행동 : 랩하기, 노래하기, 춤추기

객체 : 설계도를 통해서 실제로 만들어낸 사례

가수 객체  
임재범 : 이름=임재범, 대표곡=너를위해, 생년월일='', 국적=대한민국  
임재범의 행동 : 랩하기, 노래하기, 춤추기

#
### 인스턴스?
임재범은 객체이다(o)
임재범은 인스턴스다(x)
임재범은 가수의 인스턴스다(o)

우리가 사용하고 있는 파이썬의 모든 데이터:   
정수 문자열, 리스트 > 객체이다

### 객체??
객체는 특정타입(크래스)의 인스턴스이다!

객체
속성 : 어떤 상태(데이터)를 가지는가?
메소드 : 어떤 행위(동작)을 할 수 있는가?
타입 : 어떤 클래스를 통해 만들어진 객체인가?
#
## 클래스를 정의하는 방법
```python
class MyClass : #클래스의 이름은 대문자로 시작하는게 '관례'이다!
    pass

#인스턴스를 생성(객체 생성)
my_instance = MyClass()

#메소드를 호출한다.(객체를 동작시킨다.)
my_instance.my_method()

#속성(객체 안에 저장되어있는 데이터)
my_instance.my_attribute
```

## Example Class
```python
#클래스 생성
class Cat:

    color = 'white'

    def make_sound(self):
        print('야옹')

#객체 생성
my_cat=Cat()

#Cat클래스의 메소드를 사용
my_cat.make_sound()#야옹

print(my_cat.color)#white
```
#
## 변수의 종류
1. 클래스 변수(공통으로 가지고 있는 속성)
2. 인스턴스 변수(인스턴스마다 다르게 가지고 있는 속성)

class Car:  
소나타 : 바퀴가 4개, 이름 = '소나타'  
그랜저 : 바퀴가 4개, 이름 = '그랜저'
  
바퀴 -> 클래스 변수  
이름 -> 인스턴스 변수


```python
class Car:
    tire = 4 #클래스 변수

    #__init__함수는 객체(인스턴스)가 생성될 때 반드시 실행되는 함수
    def __init__(self,name): # self->자기 자신을 뜻하는 파라미터
        print(f'{name}이름을 가진 Car 인스턴스가 생성됨')
        self.name=name


my_car=Car('소나타')
print(my_car.tire) # 4
print(my_car.name) # 소나타

a_car = Car('소나타')
b_car = Car('아반떼')

#클래스 변수를 수정
Car.tire=2
print(a_car.tire)#2
print(b_car.tire)#2

#인스턴스 변수를 수정
b_car.tire=2
print(a_car.tire)#4
print(b_car.tire)#2

Car.tire=6 
print(a_car.tire)#6
print(b_car.tire)#2
#인스턴스 변수를 클래스 변수보다 먼저 찾아서 할당하기 때문에 b_car는 tire클래스 변수를 공통으로 사용할 수 없게 된다.
```
### self > 인스턴스 자기 자신을 뜻한다 (클래스가 아니다)
### cls > 클래스를 뜻한다(공통)


```python
class Dog:
    pass


a_dog=Dog()

a_dog.name='초코'
a_dog.color='검은색'

```
#
## 메서드
1. 인스턴스메서드
   - 인스턴스 변수를 사용하거나 인스턴스 변수에 값을 설정할 수 있는 메서드
   - 대부분의 클래스 내부에 선언되는 메서드의 종류
   - 호출시 첫번째 인자로 인스턴스 자기자신을 뜻하는 self가 전달된다.
2. 클래스메서드
   - 클래스가 사용할 메서드
   - 메서드 위에 @classmethod 데코레이터를 사용하여 정의한다.
   - 호출시, 첫번째 인자로 cls(클래스) 자기자신을 뜻하는 인자가 전달된다.  
3. 스태틱메서드(정적메서드)
   - 인스턴스 변수, 클래스 변수도 사용하지 않는 메서드
   - 클래스의 속성을 아예 다루지 않고 단지 기능(행동)만을 할 때 사용하는 메서드
   - @staticmethod 데코레이터를 사용하여 정의

## 데코레이터
함수를 꾸며주는 일을 하는 함수  
순서대로(위에서 아래) 적용되기 때문에 순서가 중요

```python
#인스턴스 메서드
class MyClass:

    def method1(self):#인스턴스 메서드다!!
        pass

my_class1 = MyClass()
my_class2 = MyClass()
```

```python
#클래스 메서드
class MyClass:
    count = 0 #클래스 변수
    def __init__(self):
        MyClass.count += 1

    @classmethod#데코레이터
    def number_of_population(cls):# cls:클래스를 뜻하는 인자
        print(f'인구수는 {cls.count}입니다.')

my_class1 = MyClass()
my_class2 = MyClass()
my_class3 = MyClass()

MyClass.number_of_population()# 인구수는 3입니다.
```

```python
#함수를 꾸미는 함수 만들기(데코레이터)
def add_print(original):#original :꾸며줄 대상이 되는 함수
    def wrapper():# 함수 내에서 새로운 함수를 선언한다.
        print('함수 시작')#추가기능 :  함수 시작 전에 출력
        original()
        print('함수 종료')#추가기능 :  함수 종료시 출력
    return wrapper#새로 만든 함수를 리턴한다.


# 꾸미고 싶은 함수
@add_print
def print_hello():
    print('hello')

print_hello()
'''
함수 시작
hello
함수 종료
'''
```

```python
#스태틱 메서드(정적메서드)
class Person:
    count = 0 #클래스 변수
    def __init__(self):
        Person.count += 1

    @staticmethod
    def check_rich(money):#스태틱 메서드는 cls, self 사용불가
        return money>10000

person1 = Person()
person2 = Person()

print(Person.count)#2
print(Person1.check_rich(20000)) #True
print(Person.check_rich(30000)) #True
```

## 클래스 메서드와 인스턴스 메서드의 차이
클래스 메서드 -> 클래스 변수를 사용한다(인스턴스 변수 사용 xxxx)  
인스턴스 메서 -> 클래스 변수도 사용할 수 있고, 인스턴스 변수 도 사용할 수 있다.

#
### 인스턴스 메서드
    호출한 인스턴스를 의미하는 self 매개변수를 통해 인스턴스를 조작
### 클래스 메서드    
    클래스를 의미하는 cls 매개변수를 통해 클래스를 조작  
### 스태틱 메서드 
    클래스 변수나 인스턴스 변수를 사용하지 않는 경우에 사용 객체의 상태나 클래스의 상태를 변경할 수 없다.