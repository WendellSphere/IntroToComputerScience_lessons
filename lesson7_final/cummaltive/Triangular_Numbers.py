# Question 2. Triangular Numbers

# The triangular numbers are the numbers 1, 3, 6, 10, 15, 21, ...
# They are calculated as follows.

# 1                         n = 1
# 1 + 2 = 3                 n = 2
# 1 + 2 + 3 = 6             n = 3
# 1 + 2 + 3 + 4 = 10
# 1 + 2 + 3 + 4 + 5 = 15

# Write a procedure, triangular, that takes as its input a positive 
# integer n and returns the nth triangular number.

def triangular(n):
    if n == 1:
        return 1
    current_n = n
    previous_n = n - 1
    index_add = 2
    final_add = 1
    i = 1
    answer = 0
    while i < previous_n:
        answer = current_n + previous_n + final_add
        final_add = final_add + index_add
        index_add = index_add + 1
        i += 1
    return answer

           
################ my solution above, professor's below##########            
'''def triangular(n):
    number = 0
    for i in range(1, n+1):     # with range you can add the i to whatever
        number += i             # but for loops without range you can't add 
    return number'''               # i to whatever
                   
                   
                   #return 1 + triangular(n-1)


print triangular(1)
#>>>1

print triangular(3)
#>>> 6
print  triangular(4)

print triangular(20)
#>>> 55
