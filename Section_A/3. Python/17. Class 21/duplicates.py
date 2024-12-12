def dup(nums):
    
    for i in range(0, len(nums)):
        
        for j in range(0, len(nums)):
            
            if i != j and nums[i] == nums[j]:
                return True
        
    return False
    
print(dup([1, 2, 1, 4]))

