# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and returns the last position in the search string
# where the target string appears, or -1 if there
# are no occurrences.
#
# Example: find_last('aaaa', 'a') returns 3

# Make sure your procedure has a return statement.

def find_last(search, target):
    size = len(search)
    i = 1
    if(size > 0 and target == ""):
        return search.find(target,size) 
    while (search.find(target, size -i) == -1): # test for cases where target is bigger than 1 char
        if(search.find(target, size -i) != 0
           and search.find(target, size -i) != -1):
            return  search.find(target, size -i)
            #break
        i = i + 1  # in conjunction with last above comment, accounts for mutiple char of target 
        if(search.find(target) == -1):
            break   #breaks out of loop, excutes next line, for cases when target is not in search
    return search.find(target, size -i)   

print find_last('aaaa', 'a')
#>>> 3

print find_last('aaaaa', 'aa')
#>>> 3

print find_last('aaaa', 'b')
#>>> -1

print find_last("111111111", "1")
#>>> 8

print find_last("222222222", "")
#>>> 9

print find_last("", "3")
#>>> -1

print find_last("", "")
#>>> 0
