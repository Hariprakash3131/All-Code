
class twoSum:
    def sum (self,nums,target):
        d={}
        for i in range(len(nums)):
            value=nums[i]
            difference=target-value
            if difference in d:
                return [d[difference],i]
            d[value]=i
            
s=twoSum()
print(s.sum([2,7,11,15],9))