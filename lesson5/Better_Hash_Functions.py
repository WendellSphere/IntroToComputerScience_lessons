# Define a function, hash_string,
# that takes as inputs a keyword
# (string) and a number of buckets,
# and returns a number representing
# the bucket for that keyword.

def hash_string(keyword,buckets):
    bucket_location = 0   # bucket for keyword
    total_char_num = 0    # will keep ascii number sum for all chars in keyword
    for char in keyword:
        total_char_num += ord(char)
    bucket_loaction = total_char_num % buckets   
    return bucket_loaction





print hash_string('a',12)
#>>> 1

print hash_string('b',12)
#>>> 2

print hash_string('a',13)
#>>> 6

print hash_string('au',12)
#>>> 10

print hash_string('udacity',12)
#>>> 11
