'''
dust = 71

if dust>70:
    print('미세먼지 농도는 70보다 크다.')
elif dust>50:
    print('미세먼지 농도는 50보다 크다.')
else :
    print('미세먼지 농도는 50보다 작거나 같다.')
'''
#dust변수에 들어있는 값을 기준으로 미세먼지 정보 출력
#dust가 150보다 작다 : 매우 나쁨
#dust가 80보다 크로 150 이하이다 : 나쁨
#dust가 30보다 크로 80 이하이다 : 보통
#dust가 30 이하이다 : 좋음

dust=int(input())

if dust>150:
    print("매우 나쁨")
elif dust>80:
    print("나쁨")
elif dust>30:
    print("보통")
else :
    print("좋음")
