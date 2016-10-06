# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

###################My Answer########################
def longest_repetition(somelist):
    if somelist == []:
        return None
    answer = []
    previous = None
    count = 0
    big = 0
    for e in somelist:
        if e == previous:
            answer.append([e,count])
            if count > big:
                big = count
            count +=1
        if e != previous:
            previous = e
            count = 0
    if answer == []:
        return somelist[0]
    for i in range(0,len(answer)):
        if big in answer[i]:
            if answer[i][1] == big:
                return answer[i][0]
            
#####################Preofesor's Answer#################
###caveat - produces wrong outputs
'''def longest_repetition(input_list):
    best_element = None
    length = 0
    current = None
    current_length = 0
    for element in input_list:
        if current != element:
            current = element
            length = current_length
        else:
            current_length = current_length + 1
        if current_length > length:
            best_element = current
            length = current_length
    return best_element'''
    
  
    



#For example,
print longest_repetition([2, 2, 2, 3, 3, 3, 3, 4, 4, 4])
#3
print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1,2,3,4,5])
# 1

print longest_repetition([[1], [2, 2], [2, 2], [2, 2], [3, 3, 3]])

print longest_repetition([])
# None

