def twoSum(nums, target):
    #print(range(len(nums)))
    for i in range(len(nums)):
        n=0
        while n< len(nums):
            if nums[i]+ nums[n] == target and i!=n:
                return i,n
            n=n+1


#ex 1
num=[2,7,11,15]
tar=9
print("ex1:",twoSum(num, tar))

#ex 2
num=[3,2,4]
tar=6
print("ex2:",twoSum(num, tar))

#ex3
num=[3,3]
tar=6
print("ex3:",twoSum(num, tar))




