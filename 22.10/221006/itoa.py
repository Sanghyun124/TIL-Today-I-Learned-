def i_to_a(num):
    string = ''

    while num >= 1:
        temp = num % 10
        s = chr(48 + temp)
        string += s
        num = num // 10

    return string[::-1]


num = int(input())
print(num, type(num), i_to_a(num), type(i_to_a(num)))
