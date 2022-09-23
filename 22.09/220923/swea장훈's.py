# def nCr(r,now,temp):
#     global possible_ans
#     if len(temp)==r:
#         possible_ans.append(temp[:])
#     else:
#         for i in range(now,n):
#             temp.append(s[i])
#             nCr(r,i+1,temp)
#             temp.pop()


T = int(input())
for t in range(T):
    n, b = map(int, input().split())
    s = list(map(int, input().split()))

    possible_ans=[]

    for i in range(1<<n):
        temp=[]
        for j in range(n):
            if i & (1<<j):
                temp.append(s[j])
        if sum(temp)>=b:
            possible_ans.append(sum(temp))

    print(f'#{t+1} {min(possible_ans)-b}')






