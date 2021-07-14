'''
There are 1000 buckets, one and only one of them is poisonous, while the rest are filled with water.
They all look identical. If a pig drinks the poison it will die within 15 minutes.
What is the minimum amount of pigs you need to figure out which bucket is poisonous within one hour?

Answer this question, and write an algorithm for the general case.

General case:
If there are n buckets and a pig drinking poison will die within m minutes,
how many pigs (x) you need to figure out the poisonous bucket within p minutes? There is exactly one bucket with poison.

Note:
A pig can be allowed to drink simultaneously on as many buckets as one would like, and the feeding takes no time.
After a pig has instantly finished drinking buckets, there has to be a cool down time of m minutes.
During this time, only observation is allowed and no feedings at all.
Any given bucket can be sampled an infinite number of times (by an unlimited number of pigs).
'''
import math
'''
60/15+1=5是每一只猪包含状态的数量，1000是状态的总数，ln（1000）/ln5，再向上取整数，就能得出答案
int base=minutesToTest/minutesToDie+1;
double temp=Math.log(buckets)/Math.log(base);//log是以e为底的对数
return (int)Math.ceil(temp);//ceil向上取整
'''

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        times = minutesToTest / minutesToDie + 1
        pigCount = 0
        while (math.pow(times, pigCount) < buckets):
            pigCount += 1

        return pigCount

    def poorPigs2(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        pigs = 0
        while (minutesToTest / minutesToDie + 1) ** pigs < buckets:
            pigs += 1
        return pigs


'''
   Hide Hint #1
What if you only have one shot? Eg. 4 buckets, 15 mins to die, and 15 mins to test.

   Hide Hint #2
How many states can we generate with x pigs and T tests?

   Hide Hint #3
Find minimum x such that (T+1)^x >= N

'''
