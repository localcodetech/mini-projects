
def main():


    nums = [3, 4, 5, 6]
    
    # count = 0
    target  = 11
    # counter =0
    output = two_sum_problem(nums,target)
    print(output)

    # oo = two_sums(count,nums,target,counter)
    # print(oo)

def two_sum_problem(nums,target):
    for i in nums:
        for k in nums:
            if (i + k) == target:
                c = nums.index(i)
                t = nums.index(k)
                return F"indices: {c,t} \nsum of {i,k} == {target}"
''' i,k used for loops to run through
checks if i + k equals to the target 
and if its equal, find its index and return
'''           
                    
            
    


# def two_sums(count,nums,target,counter):
#     while count < len(nums):
#         count +=1
#         while counter < len(nums):
#             if (nums[count] + nums[counter]) == target:
#                 counter += 1
#                 return count, counter
        
    





if __name__ == "__main__":
    main()
