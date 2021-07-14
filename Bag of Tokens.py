'''
You have an initial power of P, an initial score of 0,
and a bag of tokens where tokens[i] is the value of the ith token (0-indexed).

Your goal is to maximize your total score by potentially playing each token in one of two ways:
If your current power is at least tokens[i], you may play the ith token face up, losing tokens[i] power and gaining 1 score.
If your current score is at least 1, you may play the ith token face down, gaining tokens[i] power and losing 1 score.
Each token may be played at most once and in any order. You do not have to play all the tokens.

Return the largest possible score you can achieve after playing any number of tokens.

Constraints:
0 <= tokens.length <= 1000
0 <= tokens[i], P < 104
'''
from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        '''
        greedy alg, first sorting tokens
        使用了两个指针，左边指向翻成正面的token，右边指向翻成反面的token.
        step 1. 对token先排序。
        step 2. 我们用现在所有的power把左边的都翻成正面，同时获得了一些点。这一步之后，我们使用power贪心地获得了所有的点数。
        step 3. 我们看右边能翻转多少个反面，这个能获得Power，所以我们使用的点数换取了更多的power.
        step 4. 这两步来回走的话，就能获得更多的Points。
        需要注意的是，如果剩余的token只有一个的时候，我们是不把它换成power的。
        '''
        tokens.sort()  # step 1
        if not tokens or P < tokens[0]:
            return 0

        N = len(tokens)
        left, right = 0, N - 1
        score = 0
        remain = N

        # step 2
        while left < N and tokens[left] <= P:
            P -= tokens[left]
            left += 1
            score += 1
            remain -= 1

        if left == 0 or left == N: return score

        # step 3
        while score > 0 and remain > 1:
            P += tokens[right]
            right -= 1
            score -= 1
            remain -= 1
            while left <= right and tokens[left] <= P:  # stpe 4
                P -= tokens[left]
                left += 1
                score += 1
                remain -= 1
        return score

    def bagOfTokensScore2(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        if not tokens or P < tokens[0]:
            return 0
        score = 0
        left, right = 0, len(tokens) - 1
        while left <= right:
            if P >= tokens[left]:
                P -= tokens[left]
                left += 1
                score += 1
            else:
                if right - left > 1:
                    P += tokens[right]
                    right -= 1
                    score -= 1
                else:
                    break
        return score


''''
Example 1:
Input: tokens = [100], P = 50
Output: 0
Explanation: Playing the only token in the bag is impossible because you either have too little power or too little score.

Example 2:
Input: tokens = [100,200], P = 150
Output: 1
Explanation: Play the 0th token (100) face up, your power becomes 50 and score becomes 1.
There is no need to play the 1st token since you cannot play it face up to add to your score.

Example 3:
Input: tokens = [100,200,300,400], P = 200
Output: 2
Explanation: Play the tokens in this order to get a score of 2:
1. Play the 0th token (100) face up, your power becomes 100 and score becomes 1.
2. Play the 3rd token (400) face down, your power becomes 500 and score becomes 0.
3. Play the 1st token (200) face up, your power becomes 300 and score becomes 1.
4. Play the 2nd token (300) face up, your power becomes 0 and score becomes 2.'''
