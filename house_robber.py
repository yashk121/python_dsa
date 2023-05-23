def robUtil(dp,nums , i,ans):
    if i >= len(nums):
        return ans
    if dp[i] != -1:
        return ans + dp[i]

    
    
    dp[i] = max(robUtil(dp,nums,i+2,ans+nums[i]), robUtil(dp,nums,i+1,ans),robUtil(dp,nums,i+3,ans+nums[i]))
    return dp[i]

class Solution:
    def rob(self, nums) -> int:
        dp = [-1 for i in range(len(nums) + 1)]
        return robUtil(dp,nums,0,0)


if __name__=="__main__":
    obj = Solution()
    ls = [1,2,3,3]
    print(obj.rob(ls))


