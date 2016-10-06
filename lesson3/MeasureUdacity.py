# Define a procedure, measure_udacity,
# that takes as its input a list of strings,
# and returns a number that is a count
# of the number of elements in the input
# list that start with the uppercase 
# letter 'U'.

def measure_udacity(s):
    sum1 = 0
    i = 0
    list2 = []
    for e in s:
       if(e.find('U', 0) == 0):  # e reps the whole string
           i = i + 1 # could also use if(e[0] == 'U'): for above line
    return i
        
        




print measure_udacity(['Dave','Sebastian','Katy'])
#>>> 0

print measure_udacity(['Umika','Umberto'])
#>>> 2
