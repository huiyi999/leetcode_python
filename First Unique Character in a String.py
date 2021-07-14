from collections import Counter, OrderedDict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = OrderedDict()
        for ch in list(s):
            if ch not in count:
                count[ch] = 1
            else:
                count[ch] += 1
        # print(count)
        for key, value in count.items():
            if value == 1:
                return s.find(key)

        return -1

    def firstUniqChar2(self, s: str) -> int:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        indexes = [s.index(l) for l in letters if s.count(l) == 1]
        return min(indexes) if len(indexes) > 0 else -1


so = Solution()
print(so.firstUniqChar("leetcode"))
print(so.firstUniqChar("loveleetcode"))
print(so.firstUniqChar("loveleetcodeloveleetcode"))

'''

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.

'''
