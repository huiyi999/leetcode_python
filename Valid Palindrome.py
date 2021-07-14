

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2=[x.lower() for x in s if x.isalnum()]
        for i in range(len(s2)//2):
            if s2[i]!=s2[len(s2)-1-i]:
                return False
        return True
    def isPalindrome2(self, s: str) -> bool:
        s=s.lower()
        n=filter(str.isalnum,s)
        s="".join(n)
        if (s==s[::-1]):
            return True
        else:
            return False
so = Solution()
print(so.isPalindrome("A man, a plan, a canal: Panama"))
print(so.isPalindrome("race a car"))
print(so.isPalindrome("0P"))
'''
Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false

'''