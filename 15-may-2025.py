class Solution(object):
    def getLongestSubsequence(self, words, groups):
        """
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        currgrp = groups[0]
        res = []
        res.append(words[0])
        for i in range(1,len(groups)):
            if(groups[i]!= currgrp):
                currgrp = groups[i]
                res.append(words[i])
        return res