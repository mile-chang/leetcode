#
# @lc app=leetcode id=5 lang=python3
# @lcpr version=30202
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = "" 
        # Step 1: try each character as the center of a palindrome
        for i in range(len(s)):
            # 1.1 consider odd length palindrome (the center is a single character)
            odd_pal = self.palindrome(s, i, i)
            # 1.2 conside even length palidrome. (the center is between two characters)
            even_pal = self.palindrome(s, i, i + 1)
        # Step 2: update the result if we found a longer palindrome
            res = res if len(res) > len(odd_pal) else odd_pal
            res = res if len(res) > len(even_pal) else even_pal
        return res
    
    def palindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            # expand window to left
            left -= 1
            # expand window to right
            right += 1
        # left + 1 is the start index, right is the end index (exclusive)
        return s[left + 1:right]
        
# @lc code=end



#
# @lcpr case=start
# "babad"\n
# @lcpr case=end

# @lcpr case=start
# "cbbd"\n
# @lcpr case=end

#

