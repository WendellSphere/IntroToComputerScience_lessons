# student's solution, doesnt work
'''def fibonacci(n):
    results = [0,1]
    i = 2
    while i < n:
        results.append(results[i-1]+results[i-2])        
        i = i + 1
    return results[n]
'''

###############################33
# Professor Dave's solution
#############################

'''def fibonacci(n):
    current = 0
    after = 1
    for i in range(0,n):
        current, after = after, current + after
    return current'''

########################################
# another student answer
#####################################3

def fibonacci(n):
    a = 0
    b = 1
    c = n
    if n!=0:
        i=1
        while i!=n:
            c=a+b
            a=b
            b=c
            i+=1
    return c


print fibonacci(5)
