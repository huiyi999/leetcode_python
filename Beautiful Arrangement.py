'''
Suppose you have n integers labeled 1 through n.
A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement
if for every i (1 <= i <= n), either of the following is true:
perm[i] is divisible by i.
i is divisible by perm[i].
Given an integer n, return the number of the beautiful arrangements that you can construct.

Constraints:

1 <= n <= 15
'''


'''
解释：
1.arr[i]能够被i整除，i = 1, 2, …, N2.i能够被arr[i]整除，i = 1, 2, …, N
2.pos%i==0 or i%pos==0 ,pos表示当前的位置，i表示当前可用的数字
简单分析该题可以发现，将N个数字放置在N个位置上，这样的问题是较为典型的回溯问题：假设前i个数字已经放置好（满足条件1或条件2），则对于第i+1个位置，如果能从还未被放置的数字集合unused（或visited）中找到一个满足条件的数字k，则将其放在第i+1个位置，同时将k从unused中去掉（或者将visited[k - 1]标记为true），继续对第i+2执行相同的操作（通过递归调用）；如果找不到满足条件的数字，则回溯到上一层，修改第i个位置的数字，再尝试第i+1个位置···依此类推。
递归的base case应当是递归树的高度达到了N，如果当前层次为第N层，则表示从0到N-1层得到的这条路径是一个Beautiful Arrangement，count++。
'''

class Solution:
    def countArrangement(self, n: int) -> int:
        self.visited = [False] * n
        self.count = 0
        self.N = n

        def dfs(pos):
            if pos == 0:
                self.count += 1
                return
            for i in range(1, self.N + 1):
                if (self.visited[i - 1] or (pos % i != 0 and i % pos != 0)):
                    continue

                self.visited[i - 1] = True
                dfs(pos - 1)
                # 回溯
                self.visited[i - 1] = False

        dfs(n)
        return self.count


'''
Example 1:

Input: n = 2
Output: 2
Explanation: 
The first beautiful arrangement is [1,2]:
    - perm[1] = 1 is divisible by i = 1
    - perm[2] = 2 is divisible by i = 2
The second beautiful arrangement is [2,1]:
    - perm[1] = 2 is divisible by i = 1
    - i = 2 is divisible by perm[2] = 1
Example 2:

Input: n = 1
Output: 1

'''
