import random

'''menu=['치킨','마라탕','씨리얼','피자','갈비']

dinner=random.choice(menu)
print(dinner)'''

#로또 번호 1~45 사이의 수를 6개
nums=range(1,46)
lucky_nums=random.sample(nums,6)#sample(값의 범위, 갯수) -> 갯수만큼의 크기를 가진 리스트를 반환
#그 리스트 안의 값의 범위
print(lucky_nums)