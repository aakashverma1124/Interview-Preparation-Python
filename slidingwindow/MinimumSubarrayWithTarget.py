import math
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ws=0
        wsum=0
        min_len=math.inf

        
        for we in range(len(nums)):
            wsum+=nums[we]
            while (wsum>=target):
                min_len=min(min_len,we-ws+1)
                wsum-=nums[ws]
                ws+=1
        if min_len<math.inf:
            return min_len
        else:
            return 0
