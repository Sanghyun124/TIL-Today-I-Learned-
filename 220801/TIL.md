# WEB

웹사이트 : 웹브라우저(크롬, 엣지, 익스플로러, 등)를 통해 접속하는 웹페이지들의 모음  
웹 사이트에 접근하기 위해서는 주소(ex : www.naver.com)

웹페이지는 글,그림,동영상 여러가지 정보들을 담고 있는데, 마우스로 클릭하면 다른 웹사이트(다른 주소)로 이동하는 '링크' 들도 있다. '링크'를 통해서 여러개의 웹페이지를 연결한 것을 웹사이트라고 함

## 구성
HTML, CSS, JAVASCRIPT

- HTML : 웹페이지의 구조
- CSS : 웹페이지를 어떻게 표현할건지 (꾸미기)
- JAVASCRIPT : 웹 페이지를 어떻게 동작시킬건지
  
#
## 웹 사이트와 웹 브라우저
웹 사이트는 웹 브라우저를 통해서 보고있다.  
-> 웹사이트는 웹 브라우저를 통해 동작한다.

브라우저마다 동작이 약간씩 다르다 -> 브라우저를 만든곳이 각자 달라서 차이 발생

## 웹 표준
웹에서 표준적으로 사용되는 기술, 규칙  
어떤 브라우저든 웹페이지가 동일하게 보이도록(동작하도록) 한다. > 크로스 브라우징  
브라우저별 호환성 체크, 웹 페이지를 개발할 때 다양한 브라우저에서 볼 수 있도록 호환성 체크

#
확장 프로그램 설치 : 편한거 찾아서 쓰면 됨

크롬 개발자 도구(f12) : 크롬에서 지원하는 개발자 기능

#

## HTML
Hyper Text Markup Language  
태그 등을 이용해서 문서나 데이터의 구조를 명시하는 언어 : Markup Language  
ex) markdown

웹 페이지를 작성(구조화)하기 위한 언어이다.

.html 확장자를 가짐

#
```html
<!DOCTYPE html>
<!-- 주석 표시!! -->
<html lang="en">
    <head>
        <!--메타데이터 : 이 문서를 설명하는 요소들이 들어있다.-->
        <!--문서를 설명하는 요소들이 meta 태그를 통해 작성된다.-->
        <meta charset="UTF-8">
        <!--브라우저의 상단 탭에 표시될 타이틀-->
        <title>문서의 제목</title>
        <!--외부 파일을 가져오고 싶을때 씀-->
        <link href="style.css" rel="stylesheet">
        <!--자바 스크립트 넣는곳-->
        <script src="javascript,js"></script>
        <style>
            p{
                color : blue
            }
        </style>
        
    </head>
    <!--실제 웹페이지에 표시되는 요소들이 들어있다.-->
    <body>
        <h1>제목</h1>
        <p>본문 내용</p>
    </body>
</html>
```
#
## HTML 요소
HTML 작성 방법: <태그이름> 태그내용 </태그이름>  
내용이 없는 태그들도 존재 : 닫는 태그가 없음, 여는 동시에 닫는 태그가 존재  
ex) br, hr, img ... 등

HTML요소는 중첩된다!!!! (조건문 안에 조건문 같이)  
- 중첩을 통해서 문서를 구조화 할 수 있다.
- 여는 태그와 닫는 태그의 쌍을 잘 확인해야한다. 해당 태그의 범위가 어디까지인지 알아야 구조화가 잘 된다.
- 코드를 잘못 작성하면 오류를 반환하는게 아니라 그냥 화면이 깨지거나 오작동을 한다. : 디버깅이 힘들어진다. (어디가 잘못되었는지 한눈에 찾기 어렵다.)
  
#
## HTML 태그의 속성(attribute)
```html
<a href="http://google.com"></a>
```
- 함부로 스페이스를 넣으면 안됨
  
속성을 통해서 태그의 부가적인 정보를 설정할 수 있다.  
html 요소는 속성을 가질 수 있다. 경로, 요소의 크기 같은 추가적인 속성을 제공  
요소의 '시작태그'에 작성, 보통 이름과 값이 하나의 쌍으로 존재한다.(=)

#
## 시멘틱 태그
```html
<header>웹페이지의 상단에 존재하는 div태그</header>
<footer>웹페이지의 상단에 존재하는 div태그</footer>
```
- div 태그에 역할에 따른 이름을 부여 ==> 의미론적 마크업
- 단순히 구역을 나누는 것에 더해 태그가 의미를 가지도록 해주는 요소
- 의미가 명확해지기 때문에 코드의 가독성을 높일 수 있다. ==> 유지보수가 쉬워진다
- 검색엔진 최적화를 위해서 사용한다.
#
## CSS 적용 원칙
기본적으로는 CSS는 박스 형태로 지정된다.  
box model  
위에서부터 아래로, 왼쪽에서 오른쪽으로 쌓인다.  
모든 html요소는 box형태로 되어있다. (눈에 보이는거랑 다르다.)  
하나의 박스는 아래 4가지 부분으로 이루어져있다.
- margin : 요소 외부에 다른 요소와의 거리(간격)을 말함.
- border : 요소 외부의 경계선
- padding : 요소 내부 content와 border 간의 간격을 말한다.
- content : 요소 내부의 내용들....
#
## Display
웹페이지에서 사용자에게 보여주는 방식을 설명하는 css 속성  
인라인/블록 속성 지정 가능  
- block : 줄바꿈이 일어나게 해주는 속성(한줄 공간을 모두 차지하게 된다.)
  - 블록요소 안에는 inline 요소가 들어갈 수 있다.
  - ex) div ul ol li p


- inline : 줄바꿈이 일어나지 않게 해주는 속성(내용의 크기만큼만 공간 차지)
  - width, height 이런 속성들 지정 불가능
  - 상하 여백을 line-height속성을 통해 지정할 수 있다.
  - ex> span a img input 기타 텍스트 태그

- inline-block
  - block 특성과 inline 특성을 모두 가지고 있는 속성
  - inline처럼 한줄에 표시할 수 있고, block처럼 width, height 이런 속성을 모두 지정 가능

- none
  - 해당 요소를 화면에 표시하지 않고, 차지할 공간조차 부여하지 않는다.
  - visibillity : hidden ==> 공간은 차지하나 화면에 표시만 안한다.
#
## CSS Position
위치를 지정해주는 CSS 속성  
position : static

- static : 모든 태그의 기본값(기준 위치) 특별하게 설정해주지 않으면 이 값을 기본값으로 가지고 있다.
  - 일반적인 요소의 배치 순서를 따른다.(좌측 상단)
  - 부모 요소 안에서 배치될 때는 부모 요소의 위치를 기준으로 배치 된다.
- relate : 상대적인 위치
  - 자기 자신의 static 위치를 기준으로 이동(기본적인 css위치 흐름을 유지한다.)
- absolute : 절대적인 위치
  - 일반적인 css 위치 흐름을 벗어나게 된다.(공중에 둥둥 뜬것처럼)
  - 기준 위치가 static이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동한다.
- fixed : 고정 위치
  - 일반적인 css 위치 흐름을 벗어나게 된다.
  - 부모 요소와 관계없이 viewport(사용자의 화면)을 기준으로 이동한다.
    - 스크롤 시에도 항상 같은곳에 위치한다.
- sticky : 스크롤에 따라 고정 또는 아님
  - 원래 자리를 유지하고 있다가 스크롤을 통해 벗어나게 되면 화면 상단/하단에 달라붙는 특성