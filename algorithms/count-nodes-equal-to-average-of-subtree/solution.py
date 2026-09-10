# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        from collections import deque
        def bfs(start):
            q=deque([start])
            visited=set()
            l=[]
            while q:
                node=q.popleft()
                
                visited.add(node)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                l.append(node.val)
            return l
        def get_node(start):
            q=deque([start])
            visited=set()
            l=[]
            while q:
                node=q.popleft()
                
                visited.add(node)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                l.append(node)
            return l
        l1=get_node(root)
        result=0
        for node in l1:
            values=bfs(node)
            if node.val==sum(values)//len(values):
                result+=1
        return result
            
