class Solution:
    def majorityElement(self, nums: List[int]) -> int:
#         count = defaultdict(int)
#         for num in nums:
#             count[num] += 1
#             if count[num] > len(nums)/2:
#                 return num
            
# # time and space complexity
# # time: O(n)
# # space: O(n)
        
        nums.sort()
        return nums[len(nums) // 2]