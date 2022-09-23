binary = [0, 1]
triplet = [0, 1, 2]

T = int(input())
for t in range(T):
    bin = list(input())
    tri = list(input())

    possible_bin = []
    for i in range(len(bin)):
        b_temp = bin[:]
        if b_temp[i] == '0':
            b_temp[i] = '1'
        else:
            b_temp[i] = '0'
        possible_bin.append(''.join(b_temp))

    possible_tri = []
    for i in range(len(tri)):
        t_temp = tri[:]
        now = t_temp.pop(i)
        temp = triplet.pop(int(now))
        for x in triplet:
            t_temp.insert(i, str(x))
            possible_tri.append(''.join(t_temp))
            t_temp.pop(i)
        triplet.insert(temp, temp)

    for x in range(len(possible_tri)):
        possible_tri[x]=int(possible_tri[x],3)

    for x in range(len(possible_bin)):
        possible_bin[x]=int(possible_bin[x],2)



    for x in possible_tri:
        if x in possible_bin:
            break
    print(f'#{t+1} {x}')