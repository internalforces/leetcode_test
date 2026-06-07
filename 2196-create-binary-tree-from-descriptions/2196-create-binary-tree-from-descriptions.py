# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()

        for parent, child, isLeft in descriptions:
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if child not in nodes:
                nodes[child] = TreeNode(child)
            
            parentNode = nodes[parent]
            childNode = nodes[child]

            if isLeft == 1:
                parentNode.left = childNode
            else:
                parentNode.right = childNode

            children.add(child)

        for value in nodes:
            if value not in children:
                return nodes[value]
        