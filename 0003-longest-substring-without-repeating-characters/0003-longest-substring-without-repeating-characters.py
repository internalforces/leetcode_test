from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        q = deque()
        max_len = 0

        for char in s:
            while char in q:
                q.popleft()
            q.append(char)
            max_len = max(max_len, len(q))
        return max_len
        