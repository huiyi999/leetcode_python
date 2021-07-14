from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        if len(strs) == 1: return strs[0]

        sorted_strs = sorted(strs, key=lambda x: len(x))
        print(sorted_strs)
        res = ""
        i = 0
        for ch in sorted_strs[0]:
            print("ch: ", ch)
            print("res: ", res)
            for word in sorted_strs[1:]:
                if word[i] != ch:
                    return res
            res += ch
            i += 1
        return res

    def longestCommonPrefix2(self, strs: List[str]) -> str:
        if len(strs) == 0: return ""
        long = strs[0]
        strs = strs[1:]
        for i in strs:
            while i.find(long) != 0:
                long = long[0:len(long) - 1]

        return (long)


so = Solution()
print(so.longestCommonPrefix(["flower", "flow", "flight"]))
print(so.longestCommonPrefix(["dog", "racecar", "car"]))

'''
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''
