import requests

url='https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1021'

response = requests.get(url).json()

print(response.get('drwtNo1'))
print(response.get('drwtNo2'))
print(response.get('drwtNo3'))
print(response.get('drwtNo4'))
print(response.get('drwtNo5'))
print(response.get('drwtNo6'))

for i in range(1,7):
    key=f'drwtNo{i}'#응답데이터에서 알고 싶은 로또 번호
    print(response.get(key))