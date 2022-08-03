# float
화면에 둥둥 떠다니는 것처럼 표시해주는 css속성  
display나 위치를 직접 지정해주지 않고 float속성을 이용해서  
화면 왼쪽 또는 오른쪽에 위치시키는 방법

- left : 왼쪽
- right : 오른쪽
- none : 기본값(띄우지 않는다.)

#
## Flex Box, Flexible Box Layout
행과 열 형태로 내용들을 배치하는 레이아웃 모델(방법)

축
- main axis (메인 축)
- cross axis (교차 축)

구성요소
- Flex Container(부모요소), flex로 지정할 요소들을 포함하고 있는 요소
- Flex Item(자식요소), flex로 지정할 요소들

#
## 속성

- 부모 요소에 적용 가능한 속성  
  - display:flex(자식 요소들에게 flex 형태로 배치하도록 하는 속성)
  - flex-direction : 
    - row : (왼쪽에서 오른쪽으로)
    - row-reverse : (오른쪽에서 왼쪽으로)
    - column : (위쪽에서 아래쪽으로)
    - column-reverse : (아래쪽에서 위쪽으로)
  - flex-wrap : 컨테이너가(부모요소가) 자식요소들을 담을 여유 공간이 없을 때 어떻게 처리할 지
    - nowrap : 기본값, 삐져나갈 수도 있다. (줄바꿈을 하지 않는다.)
    - wrap : 크기를 줄여 표현(줄바꿈을 해서 inline-block처럼 한다.)
  - justify-content : 메인축(main-axis) 방향으로 아이템을 정렬하는 속성
    - flex-start : 왼쪽 정렬
    - flex-end : 오른쪽 정렬
    - center : 가운데 정렬
    - space-between : 양 끝부터 시작해서 요소들을 공백으로 띄워서 양끝, 가운데
    - space-around : 요소의 양 옆에 공백을 채워넣어서 space-between처럼 동작
    - space-evenly : space-around랑 비슷함!
  - align-content : 교차축(cross-axis)방향 아이템들을 정렬하는 속성(컨테이너를 기준으로 )
    - flex-start : 왼쪽 정렬
    - flex-end : 오른쪽 정렬
    - center : 가운데 정렬
    - space-between : 위쪽 끝, 아래쪽 끝에서 시작해서 요소들을 공백으로 띄워서 채운다
    - space-around : 요소의 양 옆에 공백을 채워넣어서 space-between처럼 동작
    - space-evenly : space-around랑 비슷함!
  - align-items : 모든 아이템을 세로축을 기준으로 정렬 줄을 기준으로 줄 안에서 아이템들을 어떻게 위치시킬지
    - flex-start : 왼쪽 정렬
    - flex-end : 오른쪽 정렬
    - center : 가운데 정렬
- 아이템에 적용 가능한 속성
  - align-self : 개별 아이템이 자기 자신을 어디에 위치시킬건지 정해주는 속성,  
   컨테이너에 적용하는것이 아닌 개별 아이템에 적용

#
## Bootstrap
우리가 css를 처음부터 다 설계하고 적용하는게 아니라 미리 정의된 클래스들을 통해서 적용하고 싶은 css속성들을 빠르게 사용할 수 있게 해주는 라이브러리

```HTML
<link></link>
```

cdn (content delivery network): 컨텐츠들을 효율적으로 전달해주기 위해서 서버를 여러개 나눠 놓고, 사용자가 해당 컨텐츠를 사용하려고 할때, 제일 가까운, 제일 빠르게 제공받을 수 있는 서버에서 사용할 수 있도록 해주는 방식(ex : AWS CloudFront)

```
https://getbootstrap.com/
아래 있는 링크들을 html파일에 포함시켜야 bootstrap을 사용할  수 있게 된다.

<!-- CSS only -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">

<!-- JavaScript Bundle with Popper -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
```

- 부트스트랩의 공백 주기(spacing) : margin, padding을 미리 지정된 값으로 class를 통해 쉽게 설정해주는 방법

{property : margin or padding}{sides : 적용시키고 싶은 방향}-{size : 크기}  
mt-3  
m : margin  
t : top   b : bottom  x: 좌우   y : 상하  
3 : 크기  
style="margin-top:30px"  
class="mt-3"  
1 : 0.25배  
2 : 0.5배  
3 : 1배  
4 : 1.5배  
5 : 3배  
p:padding  

mx-auto : 수평 중앙정렬 (가로 가운데 정렬)
#
## bootstrap에서 위치를 정해주는 position
inline, block  
d-inline  
d-block  
#
## bootstrap의 breakpoint
사용자가 보고있는 브라우저의 크기에 따라 다른 모양을 보여줄 수 있게 해주는 속성  
반응형 웹을 구현하기 위해 사용한다.  
md lg sm

#
## Bootstrap의 Grid system

화면의 레이아웃을 쉽고 빠르게 구성할 수 있도록 해준다.
flex를 이용해서 구현되어 있다. (비슷한 방식으로 동작한다.)

- Column : 실제 컨텐츠(sodyd : 텍스트..)를 포함하는 부분
- Gutter : Column들 사이사이의 빈공간 (간격)
- Container : Column들을 담고있는 공간 (div에다가 만들어준다.)
  - row, col
  
1줄은 12개의 column으로 구성된다. -> 한줄을 12등분 했다.