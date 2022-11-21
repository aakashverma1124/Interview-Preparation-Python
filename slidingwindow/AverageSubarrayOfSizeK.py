class AverageSubarrayOfSizeK:

    @staticmethod
    def average_subarray(arr, k):
        ans = []
        window_start = 0
        window_sum = 0
        for window_end in range(len(arr)):
            window_sum += arr[window_end]
            if window_end >= k - 1:
                ans.append(window_sum/k)
                window_sum -= arr[window_start]
                window_start += 1
        return ans

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6]
    k = 3
    ans = AverageSubarrayOfSizeK.average_subarray(arr, k)
    for a in ans:
        print(a, end = " ")