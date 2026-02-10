"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



"""


def main():
    integer_array =  [1,1,1,3,3,4,3,2,4,2]
    
    print (duplicate(integer_array))
    




def duplicate(integer_array):
    new_list = []
    ans = {}
    
    
    for value in integer_array:
        new_list.append(value)
        if new_list.count(value) >= 2:          
            new_list.sort()
        ans = set(new_list)
    if len(new_list) != len(ans):
        return True
    else:
        return False
    
        
       
    
        
    
   


        
    




if __name__ == "__main__": main()


