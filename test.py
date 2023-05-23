def fun(i, length, nums, sum, max_sum, dp):
    if (i >= length):
        return max_sum
    if (dp[i] != 0):
        return dp[i]
    sum += nums[i]
    max_sum = max(sum, max_sum)
    if i + 2 < length:
        max_sum = max(max_sum, fun(i + 2, length, nums, sum, max_sum, dp))
    if (i + 3 < length):
        max_sum = max(max_sum, fun(i + 3, length, nums, sum, max_sum, dp))
    dp[i] = max_sum
    return max_sum

def rob(nums) -> int:
    l = len(nums)
    if l == 1:
        return nums[0]
    dp = [0] * l

    a = fun(0, l, nums, 0, 0, dp)
    b = fun(1, l, nums, 0, 0, dp)
    return max(a, b)

if __name__ == '__main__':
    l = [1, 1, 2, 1]
    print(rob(l))
