'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

'''
import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[""]]
        elif len(strs) == 1:
            return [strs]
        result = []
        count = []
        visited = [False] * len(strs)
        for word in strs:
            count.append(collections.Counter(word))
        for i in range(len(strs)):
            if visited[i]:
                continue

            tmp = [strs[i]]
            visited[i] = True

            j = i + 1
            while j < len(strs):
                if not visited[j] and count[i] == count[j]:
                    tmp.append(strs[j])
                    visited[j] = True
                j += 1
            result.append(tmp)
        return result

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for s in strs:
            tmp = ''.join(sorted(s))
            if tmp not in result:
                result[tmp] = []
            result[tmp].append(s)
        return list(result.values())


so = Solution()
print(so.groupAnagrams2(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(so.groupAnagrams([""]))
print(so.groupAnagrams(["a"]))
'''
Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

'''
