#
# @lc app=leetcode id=151 lang=python
# @lcpr version=30203
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Step 1: reverse the full string
        reversed_full_s = s[::-1]
        # Step 2: split the string by spaces
        split_reversed_s = reversed_full_s.split()
        # Step 3: reverse each word
        reversed_words_list = []
        for word in split_reversed_s:
            reversed_words_list.append(word[::-1])
        # Step 4: join the words with a white space
        result = " ".join(reversed_words_list)
        return result

        
# @lc code=end



#
# @lcpr case=start
# "the sky is blue"\n
# @lcpr case=end

# @lcpr case=start
# "  hello world  "\n
# @lcpr case=end

# @lcpr case=start
# "a good   example"\n
# @lcpr case=end

#

