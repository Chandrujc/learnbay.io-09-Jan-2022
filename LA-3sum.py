def threeSumClosest(self, nums: List[int], target: int) -> int:
    nums.sort()
    result = nums[0] + nums[1] + nums[-1]
    for i in range(len(nums) - 2):

        start, end = i + 1, len(nums) - 1

        while start < end:
            closest_sum = nums[i] + nums[start] + nums[end]
            if closest_sum == target:
                return closest_sum
            elif closest_sum < target:
                start += 1
            elif closest_sum > target:
                end -= 1

            if abs(closest_sum - target) < abs(result - target):
                result = closest_sum

    return result
