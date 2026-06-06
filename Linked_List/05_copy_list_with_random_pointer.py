class Node:
    def __init__(self, x: int, next=None, random=None): self.val = int(x); self.next = next; self.random = random
class Solution:
    def copyRandomList(self, head):
        oldToCopy = {None: None}
        cur = head
        while cur:
            oldToCopy[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]
