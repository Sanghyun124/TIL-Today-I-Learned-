def gcd(a, b):
    r = 0
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def lcm(a, b):
    return a * b / gcd(a, b)


def is_prime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
            if count > 2:
                break
    print(True if count == 2 else False)


for a in range(10):
    is_prime(a)
