class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        que = deque([start])
        d = 0
        vis = set()
        vis.add(start)
        while que:
            r = len(que)
            for _ in range(r):
                temp = que.popleft()
                if temp == end :
                    return d
                for nb in bank:
                    if nb not in vis:
                        b = 0
                        for i in range(8):
                            if nb[i] != temp[i]:
                                b+=1
                            if b>1:
                                break
                        if b ==1:
                            que.append(nb)
                            vis.add(nb)
            d+=1       
        return -1
        