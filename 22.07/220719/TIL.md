# 6 네모출력
두개의 정수 n과 m이 주어졌을 때, 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 '*'문자를 이용하여 출력하시오.

n,m=5,9

```python
 print((('*' * n)+ '\n' ) * m )
 ```

# 디렉토리에 화살표 표시가 있을때
### 원인
해당 폴더 그니깐 상위폴더가 아닌 해당 폴더에 .git 폴더가 생겨서 발생하는 문제이다. 이미 최상위 디렉토리에 .git 폴더가 생겼는데, 해당 디렉토리에서도 push를 진행하는 과정에 .git 폴더가 생겨서 발생하는 오류이다.

### 해결
.git 파일 제거 > 스테이지 파일 제거 > add, commit push

```linux
rm -rf .git

git add .
git commit -m ""
git push origin master
```

# Origin에 설정된 url 변경

```
git remote set-rul origin url