def strlen(str):
    i = 0
    while str[i] != '\0':
        i += 1
    return i


string = 'asdf'

print(strlen(['a', 'b', 'c', 'd', '\0']))
