import requests

url='https://api.agify.io/?name=jun'
#이름이 jun인 사람의 나이를 알려달라고 서버에 요청
#서버에게 전달할 추가적인 정보가 있을때 ? 기호를 사용해서 값을 나열 -> 파라미터

#print(requests.get(url).json())#파이썬의 딕셔너리처럼 사용할 수 있는 json()
response=requests.get(url).json()#서버에게 요청을 보낸 후 서버의 응답 데이터를 변수에 저장

#이름만 출력하고 싶어요!
print(response.get("name")) # jun
#나이만 출력하고 싶어요
print(response.get("age")) # 50