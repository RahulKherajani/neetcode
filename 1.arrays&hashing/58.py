# https://leetcode.com/problems/length-of-last-word/
# Time: O(n)
# Space: O(1)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i, length = len(s) - 1, 0
        while s[i] == " ":
            i-=1
        while i > 0 and s[i] != " ":
            length += 1
            i -= 1
        return length