# Creating an Empty Hash Table
# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.

def make_hashtable(nbuckets):
    hashtable = []
    i = 0
    while i < nbuckets:
        hashtable.append([])
        i = i + 1
    return hashtable
        
example_hashTable = make_hashtable(7)
example_hashTable[1].append(['ud',['http://udacity.com']])
print example_hashTable[0]
print example_hashTable[1]

#better verision

'''def make_hashtable(nbuckets):
    hashtable = []
    for unused in range(0, nbuckets):
        hashtable.append([])
    return hashtable'''
