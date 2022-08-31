def my_compare(str1, str2):
    if str1 == str2:
        return 0
    else:
        n1 = len(str1)
        n2 = len(str2)
        n = n1 if n2 > n1 else n2
        for i in range(n):
            if str1[i] > str2[i]:
                return 1
            elif str1[i] < str2[i]:
                return -1
        if n == n1:
            return -1
        else:
            return 1


while True:
    str1 = input()
    str2 = input()
    print(my_compare(str1, str2))
