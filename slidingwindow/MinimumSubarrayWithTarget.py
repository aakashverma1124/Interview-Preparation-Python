import math
class MinSubArrayLenForTarget:
    def minSubArrayLen(nums, target):
        window_start = 0
        window_sum = 0
        minimum_length = math.inf 
        for window_end in range(len(nums)):
            window_sum += nums[window_end]
            while window_sum >= target:
                minimum_length = min(minimum_length,(window_end-window_start+1))
                window_sum -= nums[window_start]
                window_start += 1
        
        if minimum_length != math.inf:
            return minimum_length
        else:
            return 0 
if __name__== '__main__':
    nums = [2,3,1,2,4,3]
    target = 7
    minimum_length = MinSubArrayLenForTarget.minSubArrayLen(nums,target)
    print(minimum_length)
