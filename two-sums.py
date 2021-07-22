def twoSum(nums, target):
    
    
    checker = {}
    for i, v in enumerate(nums):
        print("check",checker)
        print("i",i)
        print("v",v)
        
        if target - v in checker:
            return [checker[target - v], i]
        else:    
            checker[v] = i
    return [] 
