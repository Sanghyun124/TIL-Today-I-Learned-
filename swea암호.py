from collections import deque

binary = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100',
          '1101', '1110', '1111']

T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    ary = [input() for _ in range(n)]
    ary = list(set(ary))
    for x in range(len(ary)):
        ary[x] = ary[x].strip('0')
    ary.remove('')
    ary2=[]
    for x in range(len(ary)):
        if '000000' in ary[x]:
            queue=deque()
            word=''
            count=0
            for w in ary[x]:
                if w!=0:
                    queue.append(x)
                    count=0
                else:
                    if count==5:
                        for _ in range(count):
                            queue.pop()
                        while queue:
                            word+=queue.popleft()
                        ary2.append(word)
                        word=''
                    elif not queue:
                        pass
                    else:
                        queue.append(w)
                        count+=1
        else:
            ary2.append(ary[x])
    ary2=list(set(ary2))
    print(ary2)


    check = []
    for x in ary:
        temp = ''
        for char in x:
            if char.isdigit():
                temp += binary[int(char)]
            else:
                temp += binary[ord(char) - 65 + 10]
        check.append(temp)

    print(check)




'''
    for x in range(len(check)):
        check[x]=check[x].rstrip('0')
        size=len(check[x])
        lack=(size//56+1)*56-size
        for _ in range(lack):
            check[x]='0'+check[x]

    print(check)
    for sig in check:
        size2=len(sig)
        for j in range(size2//56):
            i=j+1
            print(i)
            codes = [
                '000' * i + '11' * i + '0' * i + '1' * i,
                '00' * i + '11' * i + '00' * i + '1' * i,
                '00' * i + '1' * i + '00' * i + '11' * i,
                '0' * i + '1111' * i + '0' * i + '1' * i,
                '0' * i + '1' * i + '000' * i + '11' * i,
                '0' * i + '11' * i + '000' * i + '1' * i,
                '0' * i + '1' * i + '0' * i + '1111' * i,
                '0' * i + '111' * i + '0' * i + '11' * i,
                '0' * i + '11' * i + '0' * i + '111' * i,
                '000' * i + '1' * i + '0' * i + '11' * i
            ]
            for position in range(size2-56*i+1):
                decoded_num=[]
                signal = [sig[start+position:position+start + 7 * i] for start in range(0, size2, 7 * i)]
                for k in range(8):
                    if signal[k] in codes:
                        decoded_num.append(codes.index(signal[k]))
                    else:
                        break
                else:
                    break
    print(decoded_num)
    total = 0
    for number in range(8):
        if number % 2:
            total += decoded_num[number]
        else:
            total += decoded_num[number] * 3

    if total % 10:
        print(f'#{t + 1} 0')
    else:
        print(f'#{t + 1} {sum(decoded_num)}')
'''

