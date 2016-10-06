# Define a procedure, union,
# that takes as inputs two lists.
# It should modify the first input
# list to be the set union of the two
# lists. You may assume the first list
# is a set, that is, it contains no 
# repeated elements.

def union(p, p2):
    i = 0
    for e in p2:
        if(p2[i] in p): #if value at current index of p2 is in p
            True
        else:
            p.append(p2[i])
        i = i + 1

#solution from Udacity        
# def union(p, q):
#     for e in q:
#           if not in p:
#               p.append(e)
    




# To test, uncomment all lines 
# below except those beginning with >>>.

a = [1,2,3]
b = [2,4,6]
union(a,b)
print a 
#>>> [1,2,3,4,6]
print b
#>>> [2,4,6]
