from typing import List


def canJump(nums: List[int]) -> bool:
    if len(nums) == 1:
        return True
    max_reach = nums[0]
    i=1
    while i <=max_reach:
        max_reach = max(max_reach, i + nums[i])
        i+=1
        if max_reach >= len(nums) - 1:
            return True

    return False


if __name__ == '__main__':
    l: List[int] = [1, 1, 1, 0]
    print(canJump(l))
