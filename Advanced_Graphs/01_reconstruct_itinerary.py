import collections
class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        adj = {src: collections.deque() for src, dst in tickets}
        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst)
        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False
            temp = list(adj[src])
            for i, v in enumerate(temp):
                adj[src].popleft()
                res.append(v)
                if dfs(v):
                    return True
                adj[src].append(v)
                res.pop()
            return False
        dfs("JFK")
        return res
