import math

class MinimumSubarrayWithTarget:

    @staticmethod
    def minimum_subarray_with_target(arr, target):
        window_sum = 0
        window_start = 0
        min_length = math.inf

        for window_end in range(len(arr)):
            window_sum += arr[window_end]
            while window_sum >= target:
                min_length = min(min_length, window_end - window_start + 1)
                window_sum -= arr[window_start]
                window_start += 1

        return min_length

if __name__ == '__main__':
    arr = [7, 4, 1, 11, 4, 5]
    target = 12
    print(MinimumSubarrayWithTarget.minimum_subarray_with_target(arr, target))