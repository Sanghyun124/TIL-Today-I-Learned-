class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# BinarySearchTree
class BST:
    def __init__(self):
        self.root = None  # root는 트리의 시작지점

    # 탐색연산
    def search(self, target):
        now = self.root
        cnt = 0

        # 찾을때까지 반복
        while now:
            # 현재 내가있는 노드의 키값과 찾고있는 값이 같으면 반환
            if target == now.data:
                print(cnt)
                return now

            # 내가있는 노드의 키값이 찾고있는 값보다 작으면 왼쪽으로 이동
            elif target < now.data:
                now = now.left

            # 내가있는 노드의 키값이 찾고있는 값보다 크면 오른쪽으로 이동
            elif target > now.data:
                now = now.right
            cnt += 1
        # 만약 반복이 끝나버렸다. ==> 찾는 데이터가 이진 트리안에 없다.
        return now

    def insert(self, node):
        now = self.root

        if now == None:
            self.root = node
            return

        # 탐색을 진행해서 탐색 실패한 지점에 노드를 삽입
        while True:
            p = now  # now가 바뀌기 전에 부모를 기억해놓자
            # 넣고싶은 데이터가 현재 노드보다 작으면 왼쪽
            if node.data < now.data:
                now = now.left  # 왼쪽으로 간다.
                # 왼쪽으로 갔는데 노드가 없다??
                if not now:
                    # 왼쪽이 없으면 (삽입할 자리를 찾았으면) 여기에 추가
                    # 부모 노드의 왼쪽에 추가
                    p.left = node
                    return

            # 넣고싶은 데이터가 현재 노드보다 크면 오른쪽
            else:
                now = now.right
                # 오른쪽으로 갔는데 노드가 없다?
                if not now:
                    # 오른쪽이 내가 넣어야할 자리이다.
                    p.right = node
                    return


def preorder(node):
    if node:
        print(node.data, end=' ')
        preorder(node.left)
        preorder(node.right)

# root = Node(9)
# root.left = Node(4)
# root.right = Node(12)
# root.left.left = Node(3)
# root.left.right = Node(6)
# root.right.right = Node(15)
# root.right.right.left = Node(13)
# root.right.right.right = Node(17)

#
# target = 13
bst = BST()

data_list = [9,4, 12, 3, 6, 15, 13, 17]

for x in data_list:
    now = Node(x)
    bst.insert(now)
# bst.search(13)

preorder(bst.root)
