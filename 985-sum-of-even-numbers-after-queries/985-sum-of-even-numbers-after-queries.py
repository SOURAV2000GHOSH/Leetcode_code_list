class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        pos_to_even_nums = defaultdict(int)
        
        output = []
        
        for i, n in enumerate(nums):
            if n % 2 == 0:
                pos_to_even_nums[i] = n
        
        even_sum = sum(pos_to_even_nums.values())
        
        for i, q in enumerate(queries):
            val = q[0]
            index = q[1]
            previous_value = nums[index]
            nums[index] += val
            
            if index in pos_to_even_nums:
                # the number was even, remove from even_sum
                even_sum -= previous_value  
                pos_to_even_nums.pop(index)
                
            # if new value is now even and needs to be added
            if nums[index] % 2 == 0:
                even_sum += nums[index]
                pos_to_even_nums[index] = nums[index]

            output.append(even_sum)
        
        return output