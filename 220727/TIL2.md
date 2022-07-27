# 객체지향의 핵심개념 4가지
상속 : 클래스의 자원을 재사용할 수 있도록 만들어 주는 기술(코드의 중복을 줄인다)
추상화 : 복잡한 것은 숨기고, 필요한 것만 노출
캡슐화 : 객체의 일부 구현 내용에 대해 외부로부터 직접적인 접근을 차단
다형성 : 동일한 이름을 가진 메서드가 클래스에 따라 다르게 동작하는 것

```python
#상속 예시

#겹치는 기능 talk를 상속
'''class Person:

    def __init__(self,name):
        self.name=name

    def talk(self):
        print(f'반갑습니다. 제 이름은 {self.name}입니다.')

class Student:

    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
    
    def talk(self):
        print(f'반갑습니다. 제 이름은 {self.name}입니다.')'''

class Person:

    def __init__(self,name):
        self.name=name

    def talk(self):
        print(f'반갑습니다. 제 이름은 {self.name}입니다.')

class Student(Person):#Person 클래스는 Student 클래스의 부모 클래스가 된다.

    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
    
person1 = Person('김싸피')
student1 = Student('박싸피',1)

person1.talk()#반갑습니다. 제 이름은 김싸피입니다.
student1.talk()#반갑습니다. 제 이름은 박싸피입니다.
#자기가 정의한 적이 없는데도 클래스 정의 부분의() 안에 있는 클래스의 기능을 사용할 수 있다.
```
### super()
자식 클래스에서 부모 클래스를 사용하고 싶은 경우

```python
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade

person1=Person('김싸피')
student1 = Student('박싸피',1)

print(student1.grade) # 1
```
#
## 상속

파이썬의 모든 클래스는 object라는 클래스로부터 상속된다.  
(모든 클래스의 부모를 계속 알아가다 보면 마지막에 object)

부모클래스의 모든 요소(속성,메소드)가 상속된다  
==자식클래스는 부모클래스의 속송, 메소드를 사용할 수 있다.  
==super()를 통해 부모 클래스의 요소를 호출 가능하다.

### 메소드 오버라이딩
    자식클래스에서 부모의 메소드를 재정의하는 기능
    부모의 메소드를 호출하는데, 자식이 재정의 해버리면
    재정의 한대로 실행된다.(부모에서 작성된 기능으로는 동작하지 않는다.)

상속관계에서 이름공간을 탐색하는 순서  
인스턴스 -> 자식클래스 -> 부모클래스

파이썬에서는 다중상속(여러개의 클래스의 기능을 물려받아 사용하는게 가능하다.)  
상속받은 모든 클래스들의 기능을 사용 가능하다.  
중복된 속성(클래스a와 클래스b에 똑같은 이름을 가진 메소드,변수)이 있을 경우 상속 순서에 따라 결정이 된다.

```python
class Person:
    pass

class Mom(Person):
    gene='XX'

class Dad(Person):
    gene='XY'

class Baby(Dad,Mom):
    pass

print(Baby.gene) # XY
#상속받은 순서에 따라 Dad의 gene이 출력됨
```
#
## 다형성
동일한 이름을 가진 메서드가 클래스에 따라 다르게 동작하는 것을 말한다.  
메소드 오버라이딩을 통해 구형

```python
class Animal:

    def make_sound(self):
        print('소리를 낸다.')

class Dog(Animal):

    def make_sound(self):
        print('개는 멍멍 짖는다.')

class Cat(Animal):

    def make_sound(self):
        print('고양이는 야옹한다.')

animal1=Animal()
dog1=Dog()
cat1=Cat()

animal1.make_sound()#소리를 낸다.
dog1.make_sound()#개는 멍멍 짖는다.
cat.make_sound()#고양이는 야옹한다.
```
#
## 캡슐화
객체의 일부 구현 내용에 대해 외부로부터 직접적인 접근을 차단한다.  
-> 객체 내부에 숨시고 싶은 정보가 있을 때 사용  
파이썬에서 암묵적으로 전재하지만, 언어적으로는 존재하지 않는다.

### 접근 제어자
접근할 수 있는 범위를 지정한다.

- public : 언더바 없이 시작하는 메서드나 속성, 어디서나 호출이 가능하다(누구나 사용 가능)
- protected : 언더바 1개로 시작하는 메서드나 속성, 암묵적 규칙에 의해서 부모 클래스와 자식 클래스에서만 호출이 가능하다.
- private : 언더바 2개로 시작하는 메서드나 속성, 오직 자기 자신만이 사용 가능하다. 외부에서 접근이 불가능


### getter / setter
변수에 접근할 수 있는 메서드를 별도로 생성해서 사용할 수 있게 한다.

getter: 변수의 값을 읽어주는 메서드
 - @property 데코레이터 사용

setter : 변수의 값을 설정하는 메서드
 - @변수.setter 사용

```python
class Person:
    def __init__(self, age):
        self.age = age

    @property
    def age(self): # age라는 변수를 getter 메소드를 통해 접근할 수 있도록 한다.
        return self._age
    
    @age.setter
    def age(self,new_age): # age라는 변수를 setter 메소드를 통해 수정할 수 있게 한다.
        if new_age < 20 or new_age > 100:
            return
        self._age=new_age


person1=Person(21)
print(person1.age)#21

person1.age=33
print(person1.age)#33

person1.age=19
print(person1.age)#33

person1.age=9999
print(person1.age)#33
```