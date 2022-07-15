T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    sudoku=[]
    check=1
    for i in range (0,9):
        sudoku.append(list(map(int,input().split())))
    for j in range (0,9):
        if sudoku[j]!=set(sudoku[j]):
            check=0
    for i in range(0,9):
        temp=[]
        temp.append(j[i] for j in sudoku)
        if temp!=set(temp):
            check=0
    index=0
    for a in range(0,9):
        temp=[]
        if a%3==0 :
            index=0
        for b in range(0,3):
            for c in range(0,3):
                temp.append(sudoku[b+((a//3)*3)][c+index])
        if temp!=set(temp):
            check=0
            break
        index+=3

    print('#%d %d'%(test_case,check))