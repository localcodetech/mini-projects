
"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.


"""


def main():
    s = "madam"
    t = "damam"
    

    ouput = anagram_checker(s,t)
    print(ouput)

    

def anagram_checker(s,t):
    new_list = list(s)
    new_list_2 = list(t)

    for var in new_list:
        new_list.sort()
        for item in new_list_2:
            new_list_2.sort()
        if new_list == new_list_2:
            return True
        else:
            return False
    return var, item

if __name__ == "__main__":
    main()