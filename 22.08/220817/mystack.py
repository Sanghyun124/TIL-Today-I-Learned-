class stack:
    def __init__(self):
        self.items = []

    # push 원소 삽입
    def push(self, item):
        self.items.append(item)
        print(f'push {item}')

    # pop 원소 제거
    def pop(self):
        item = self.items.pop(-1)
        print(f'pop {item}')
        return item

    # peek top에 있는 원소 반환
    def peek(self):
        print(f'peek {self.items[-1]}')
        return self.items[-1]

    # isEmpty 스택이 비어있는지 확인
    def isEmpty(self):
        return not self.items