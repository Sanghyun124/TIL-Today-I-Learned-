# 제어문

특정 상황에 따라서 코드를 선택적으로 실행하거나 계속해서 실행(반복)하는 제어문


# 조건문
참/거짓을 판달할 수 있는 조건식(boolean)과 함께 사용
결과가 True 아니면 FAlse이면 조건식으로 사용할 수 있다.

조건이 참이면 : 코드블록을 실행
조건이 거짓이면 : 코드블록을 실행하지 않고 건너뛴다

## 복수 조건문

elif를 사용하여 표현함

## 중첩 조건문

조건문 내에 조건문을 중첩하여 사용

## 조건 표현식

삼항 연산자를 뜻함

```python
'True 일 경우 값' if (조건) else 'false일 경우 값'
```

# 반복문
특정 조건을 만족할 때 까지  같은 동작을 계속 반복하고 싶을 때 사용

조건이 참이면 반복문의 코드 블록을 계속 실행
조건이 거짓이 되면 반복을 종료하고 다음 코드를 실행한다.

## while문, for문

while문 : 종료조건에 해당하는 코드를 통해 반복문을 종료 시키는(반드시 종료 시켜야함) 반복은 언제 반복이 종료될지 우리가 한번에 예측하기 어렵다

for문 : 반복 가능한 객체(순회가능 : list, tuple, string, range, set, dictionary 등)을 모두 순회하면 종료시키는 반복문, 길이를 알고 있기 때문에 반복이 언제까지 될지 예측하기 쉽다.

반복문을 제어하는 키워드
break : 반복을 중간에 강제로 종료시키는 코드
continue : 현재 실행중인 코드 블록을 건너 뛰고 다음 반복을 실행하는 코드
pass : 아무것도 하지않음

## while문
조건식이 True일 경우 반복적으로 코드를 실행

조건이 True일 경우 "들려쓰기" 가 되어있는 코드블록을 실행한다.

코드블록을 모두 실행하고, 다시 조건식을 검사하여 True일 경우 반복을 계속하고, False일 경우 반복을 종료하고 다음 코드를 실행한다. 
!!! 무한루프를 하지 않도록 종료조건을 반드시 유효하게 설정해야한다.!!!

## for문
반복 가능한 객체(순회가능 : list, tuple, string, range, set, dictionary 등)을 모두 순회하면 종료시키는 반복문

### dictionary의 경우 추가 메서드 사용
keys() : Key로 구성된 결과
values() : value로 구성된 결과
items() : (key,value)의 튜플로 구성된 결과

### enumerate 순회
enumerate() : 인덱스와 객체를 쌍으로 담은 열거형 객체 반환

- (index,value)형태의 튜플로 구성된 열거 객체를 반환

## List Comprehension
표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성하는 법

```python
[code for 변수 in iterable]
[code for 변수 in iterable if  조건식]
```

## Dictionary Comprehension

표현식과 제어문을 통해 특정한 값을 가진 딕셔너리를 간결하게 생성하는 법

```python
{ode for 변수 in iterable}
{code for 변수 in iterable if  조건식}
```

