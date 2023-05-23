import sys
def fun(dp, i, nums):
    if i >= len(nums) - 1: return 0

    if i in dp: return dp[i]
    ans = sys.maxsize

    for j in range(i + 1, i + nums[i]+1):
        ans = min(ans, 1 + fun(dp, j, nums))
    dp[i] = ans
    return ans


class Solution:
    def jump(self, nums):
        dp = {}
        return fun(dp, 0, nums)


if __name__ == '__main__':
    f = Solution()
    l = [2, 2, 1, 1, 4]

    print(f.jump(l))
