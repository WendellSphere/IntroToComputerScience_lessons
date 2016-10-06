# Deep Count 

# The built-in len operator outputs the number of top-level elements in a List,
# but not the total number of elements. For this question, your goal is to count
# the total number of elements in a list, including all of the inner lists.

# Define a procedure, deep_count, that takes as input a list, and outputs the
# total number of elements in the list, including all elements in lists that it
# contains.


# For this procedure, you will need a way to test if a value is a list. We have
# provided a procedure, is_list(p) that does this:

def is_list(p):
    return isinstance(p, list)

# It is not necessary to understand how is_list works. It returns True if the
# input is a List, and returns False otherwise.

def deep_count(p):
    for e in p:
        if is_list(e) == True and e != []:
            return len(p) + deep_count(e)
    return len(p) 
            
######################teacher's solition################################
#def deep_count(p):
 #   sumlist = 0
  #  for e in p:
   #     sumlist = sumlist + 1
    #    if is_list(e):
     #       sumlist = sumlist + deep_count(e)
    #return sumlist

print deep_count([1, 2, 3])
#>>> 3

# The empty list still counts as an element of the outer list
print deep_count([1, [], 3]) 
#>>> 3 

print deep_count([1, [1, 2, [3, 4]]])
#>>> 7

print deep_count([[[[[[[[1, 2, 3]]]]]]]])
#>>> 10

 
