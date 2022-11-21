class MaxSubarraySum:

    @staticmethod
    def max_subarray_sum(arr, k):
        window_start = 0
        window_sum = 0
        max_sum = 0
        for window_end in range(len(arr)):
            window_sum += arr[window_end]
            if window_end >= k - 1:
                max_sum = max(max_sum, window_sum)
                window_sum -= arr[window_start]
                window_start += 1
        return max_sum

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6]
    k = 3
    ans = MaxSubarraySum.max_subarray_sum(arr, k)
    print(ans)