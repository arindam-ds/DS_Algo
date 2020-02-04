'''You are given an array of integers. 
Return the length of the longest consecutive elements sequence in the array.

For example, the input array [100, 4, 200, 1, 3, 2] has the longest consecutive sequence 
1, 2, 3, 4, and thus, you should return its length, 4.
'''
def longest_consecutive(nums):
    nums.sort()
    length = 1
    max_length = 0
    if len(nums) > 1:
        ptr = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == ptr+1:
                length+=1
            else:
                if length > max_length:
                    max_length = length
            ptr = nums[i]
    return max_length
            

print(longest_consecutive([100, 4, 200, 1, 3, 2]))