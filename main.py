def twoSum(target, len, nums=[]):
    for i in range(0,len-1,1):
        for j in range(i+1, len, 1):
            if(nums[i]+nums[j]==target):
                result_array = [i, j]
                return result_array

nums = [2,7,11,15]
result = twoSum(9,len(nums),nums)
print(result)