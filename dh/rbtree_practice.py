# #이진트리 구현하기

# from __future__ import annotations
# from this import d
# from typing import Any, Type

# class Node:
#     """이진 검색 트리의 노드"""
#     def __init__(self, key: Any,value: Any, left: Node =None,right: Node = None):
#         """생성자(constructor)"""
#         self.key = key  #키
#         self.value = value  #값
#         self.left = left  #왼쪽 포인터
#         self.right = right #오른쪽 포인트
    

# class BinarySearchTree:
#     """이진 검색 트리"""

#     def __init__(self):
#         """초기화"""
#         self.root = None #루트


#     def search(self, key: Any):
#         """키가 key인 노드를 검색"""
#         p = self.root
#         while True:
#             if p is None:
#                 return None
#             if key == p.key:
#                 return p.value
#             elif key < p.key:
#                 p = p.left
#             else:
#                 p = p.right


#     def add(self, key: Any, value: Any):

#         def add_node(node: Node, Key: Any, value: Any):
#             """node를 루트로 하는 서브트리에 키가 key이고 값이 value인 노드를 삽입""" #키와 벨류를 정해서 입력하는 경우 
#             if key == node.key:
#                 return False
#             elif key < node.key:
#                 if node.left is None:
#                     node.left = Node(key, value, None, None)
#                 else:
#                     add_node(node.left, key, value)
#             else :
#                 if node.right is None:
#                     node.right = Node(key, value, None, None)
#                 else:
#                     add_node(node.right, key, value)
            
#             return True

#         if self.root is None:
#             self.root = Node(key, value)
#             return True
#         else :
#             return add_node(self.roof, key, value)

    
#     def remove(self, key: Any):
#         """키가 key인 노드 삭제"""
#         p = self.root
#         parent = None
#         is_left_child = True

#         while True:
#             if p is None:
#                 return False
            
#             if key == p.key:
#                 break
#             else:
#                 parent = p
#                 if key < p.key:
#                     is_left_child = True
#                     p = p.left
#                 else:
#                     is_left_child = False
#                     p = p.right

#         if p.left is None:
#             if p is self.roof:
#                 self.roof = p.right
#             elif is_left_child:
#                 parent.left = p.right
#             else :
#                 parent.right = p.right
        
#         elif :
#             print()