class Solution:
    def searchRange(self, nums, target: int) :
        if not nums:
            return [-1, -1]
        l = len(nums)
        first = 0
        last = l - 1
        left, right = -1, -1
        while (first <= last):

            mid = (first + last) // 2

            if (mid == 0 or target > nums[mid - 1]) and nums[mid] == target:
                left = mid
            elif nums[mid] >= target:
                last = mid - 1
            else:
                first = mid + 1

        if left == -1:
            return [-1, -1]
        first = 0
        last = l - 1
        while (first <= last):

            mid = (first + last) // 2

            if ((mid == l - 1 or target < nums[mid + 1]) and nums[mid] == target):
                right = mid
            elif nums[mid] <= target:
                first = mid + 1
            else:
                last = mid - 1

        return [left, right]


if __name__ == '__main__':
    obj = Solution()
    arr = [5, 7, 7, 8, 8, 10]
    target = 8
    print(obj.searchRange(arr,target))
