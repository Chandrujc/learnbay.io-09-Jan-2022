class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        unique_dict = {num: 0 for num in nums}
        for num in nums:
            unique_dict[num] += 1

        for key, value in unique_dict.items():
            if value == 1:
                return key