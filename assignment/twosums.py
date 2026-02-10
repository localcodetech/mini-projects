'''

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


'''


def main():
    num = [2,7,11,15]
    target = 18
    output = twosums(target,num)
    print(output)


def twosums(target,num):

    for var in num:
        for value in num:
            if var + value == target:
                return num.index(var), num.index(value)








if __name__ =="__main__":
    main()
