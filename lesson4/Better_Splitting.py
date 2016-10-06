# 1 Gold Star

# The built-in <string>.split() procedure works
# okay, but fails to find all the words on a page
# because it only uses whitespace to split the
# string. To do better, we should also use punctuation
# marks to split the page into words.

# Define a procedure, split_string, that takes two
# inputs: the string to split and a string containing
# all of the characters considered separators. The
# procedure should return a list of strings that break
# the source string up by the characters in the
# splitlist.


def split_string(source,splitlist):
    size_splitlist = len(splitlist)
    sisze_source = len(source)
    newsource = ''
    index = 0
    big = 0
    list1 = []
    list2 = []
    i = 0
    found = 0
    f = 0
    f2 = 0
    j = 0
    next1 = 0

    for e in splitlist:
        list1 += e
    print splitlist
    
    for e in list1:
        found = source.find(list1[i])
        #print found
        list2 += [found]
        i = i + 1
    print list2
        
    for e in list1:
        f = source.find(list1[next1])
        f = f + 2
        f2 = source.find(list1[next1], f)
        if(f2 != -1):
            list2 += [f2]
        next1 = next1 + 1
        
    list2.sort()
    newsource += source[0:list2[0]] + " "  #+ source[list2[0]+1:list2[1]]

    for e in list2:
        if(j != 0 and j < size_splitlist -1):
            newsource += source[list2[0]+1:list2[j]] + " "
            newsource += source[list2[j]+1:list2[j+1]]
        if(j == size_splitlist -1):
            newsource += " " + source[list2[size_splitlist -1]+1 :sisze_source -1]
        j = j +1
        
    newsource = newsource.split()
    return newsource
                        
    

    
    
    
    

            
out = split_string("This is a test-of the,string separation-code!"," ,!-")
print out
#>>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

out = split_string("After  the flood   ...  all the colors came out.", " .")
print out
#>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

#out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
#print out
#>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']





############################################################################################

 #while(j < s):
     #   if(splitlist[0] in source):
      #      spot = source.find(splitlist[j])
       #     print spot
        #    newsource = source[0:spot] + ' ' 
         #   print newsource
        
        #j = j +1
        #if(e in newsource):
         #   spot2 = newsource.find(e)
            #newsource = newsource[0:spot2] + ' ' + newsource[spot2+1:]


#for e in split:
     #   if('-' in e):
      #      spot = e.find('-')
    
       #     split[i]  = e[0:spot] + ' ' + e[spot +1:]
            
        #if( i > s3):
         #   break
        #i = i + 1
    #print split 
    #print split[3].split()
        
