class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

# 전위 순회(Preorder Traversal)
def pre_order(node):
    print(node.data, end=' ')
    if node.left_node != None:
        pre_order(tree[node.left_node])
    if node.right_node != None:
        pre_order(tree[node.right_node])

# 중위 순회(Inorder Traversal)
def in_order(node):
    if node.left_node != None:
        in_order(tree[node.left_node])
    print(node.data, end=' ')
    if node.right_node != None:
        in_order(tree[node.right_node])

# 후위 순회(Postorder Traversal)
def post_order(node):
    if node.left_node != None:
        post_order(tree[node.left_node])
    if node.right_node != None:
        post_order(tree[node.right_node])
    print(node.data, end=' ')

n = int(input())
tree = {}

for i in range(n):
    data, left_node, right_node = input().split()
    if left_node == "None":
        left_node = None
    if right_node == "None":
        right_node = None
    tree[data] = Node(data, left_node, right_node)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])




"""
         A
      /     \
    B         C
  /   \     /   \
 D     E   F     G

입력 예시
7
A B C
B D E
C F G
D None None
E None None
F None None
G None None
"""


"""

import sys
input = sys.stdin.readline

n = int(input())
tree = dict()   # tree = {}

for _ in range(n):
    root, left, right = input().split()
    tree[root] = [left, right]

# 전위 순회(현재노드 -> 왼쪽 -> 오른쪽)
def preorder(now):
    if now == '.':
        return
    print(now, end='')          # 1. 현재 노드
    preorder(tree[now][0])      # 2. 왼쪽
    preorder(tree[now][1])      # 3. 오른쪽

# 중위 순회(왼쪽 -> 현재 -> 오른쪽)
def inorder(now):
    if now == '.':
        return
    inorder(tree[now][0])       # 1. 왼쪽
    print(now, end='')          # 2. 현재 노드
    inorder(tree[now][1])       # 3. 오른쪽

# 후위 순회(왼쪽 -> 오른쪽 -> 현재)
def postorder(now):
    if now == '.':
        return
    postorder(tree[now][0])     # 1. 왼쪽
    postorder(tree[now][1])     # 2. 오른쪽
    print(now, end='')          # 3. 현재 노드

preorder('A')
print()
inorder('A')
print()
postorder('A')

"""
# 'None'를 '.'로 변경
