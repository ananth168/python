class Solution:
    def twosum(self, nums, target):
        store = {}
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if num in store:
                print("two elements are : ")
                return [store[num], i]
            else:
                store[complement] = i

obj = Solution()
result = obj.twosum([2, 5, 6, 1, 8], 9)
print(result)