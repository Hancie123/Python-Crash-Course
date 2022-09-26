from array import array

#declare array

# nums= array('i',[])
# print(nums)
#
# nums.append(6)
# nums.append(8)
# print(nums)

#index(self, v, start=0, stop=9223372036854775807, /)

# nums=array("i",[3,6,8,9,2,3,6,4,5,2,3,3,2])
# tmp=1
# result=nums.index(tmp,0,len(nums))
# print(result)



nums=array('i',[9,6,7,8,9,2,3,1,2])
tmp=5
result=nums.count(tmp)
if result>0:
    result2=nums.index(tmp,0,len(nums))
    print("{} fount at {}".format(tmp,result2))
else:
    print("{} is not found".format(tmp))