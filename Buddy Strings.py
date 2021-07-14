'''
Given two strings A and B of lowercase letters,
return true if you can swap two letters in A so the result is equal to B, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed)
such that i != j and swapping the characters at A[i] and A[j].
For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

Constraints:

0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist of lowercase letters.
'''


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B) or (len(A) == 0 and len(B) == 0): return False
        if A == B:
            return len(A) - len(set(A)) >= 1
        # if A == B:
        #     a = list(A)
        #     n = len(a)
        #     for i in range(n):
        #         print(a[i])
        #         print(A.count(a[i]))
        #         if A.count(a[i]) != 1:
        #             return True
        #     return False

        res = False
        dif = []
        for i in range(len(A)):
            ca = A[i]
            cb = B[i]
            if ca == cb:
                continue
            else:
                dif.append(i)
            if len(dif) > 2:
                return False
        # print(len(dif))
        if len(dif) == 2 and A[dif[0]] == B[dif[1]] and A[dif[1]] == B[dif[0]]:
            res = True

        return res

    def buddyStrings2(self, A, B):
        if len(A) != len(B) or set(A) != set(B): return False
        if A == B:
            return len(A) - len(set(A)) >= 1
        else:
            indices = []
            counter = 0
            for i in range(len(A)):
                if A[i] != B[i]:
                    counter += 1
                    indices.append(i)
                if counter > 2:
                    return False
            return A[indices[0]] == B[indices[1]] and A[indices[1]] == B[indices[0]]


so = Solution()
print(so.buddyStrings("ab", "ab"))  # false
print(so.buddyStrings("", "aa"))  # false
print(so.buddyStrings("aa", "aa"))  # true
print(so.buddyStrings("ab", "ba"))  # true
print(so.buddyStrings("aaaaaaabc", "aaaaaaacb"))  # true
print(so.buddyStrings("abcd", "badc"))  # false
print(so.buddyStrings("", ""))  # false
print(so.buddyStrings("abccccc", "abccccc"))  # true
print(so.buddyStrings("abac", "abad"))  # false

'''
Example 1:
Input: A = "ab", B = "ba"
Output: true
Explanation: You can swap A[0] = 'a' and A[1] = 'b' to get "ba", which is equal to B.

Example 2:
Input: A = "ab", B = "ab"
Output: false
Explanation: The only letters you can swap are A[0] = 'a' and A[1] = 'b', which results in "ba" != B.

Example 3:
Input: A = "aa", B = "aa"
Output: true
Explanation: You can swap A[0] = 'a' and A[1] = 'a' to get "aa", which is equal to B.

Example 4:
Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true

Example 5:
Input: A = "", B = "aa"
Output: false
'''
