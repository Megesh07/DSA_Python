import collections
class Solution:
    def rightSideView(self, root):
        res = []
        q = collections.deque([root] if root else [])
        while q:
            rightSide = None
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res
