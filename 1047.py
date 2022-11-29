class Solution:
    def removeDuplicates(self, s: str) -> str:
        dq = collections.deque()
        for c in s:
            if dq and dq[-1] == c:
                dq.pop()
            else:
                dq.append(c)
        return ''.join(dq)
