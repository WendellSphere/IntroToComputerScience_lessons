# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

def find_element(p, v): # p for list and v for value
    i = 0
    for e in p:
        if(e != v):
            i = i + 1
        if(e == v):
            return i
    return -1
        
            
# Another way to solve it is thus
#def find_element(p, v):
#    if v in p: could also use if v not in p
#        return p.index(v)
#    else:
#        return -1
x = [1, 2]
print x[0]

print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1