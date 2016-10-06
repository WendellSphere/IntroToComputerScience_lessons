# Question 5: Date Converter

# Write a procedure date_converter which takes two inputs. The first is 
# a dictionary and the second a string. The string is a valid date in 
# the format month/day/year. The procedure should return
# the date written in the form <day> <name of month> <year>.
# For example , if the
# dictionary is in English,

english = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 
6:"June", 7:"July", 8:"August", 9:"September",10:"October", 
11:"November", 12:"December"}

# then  "5/11/2012" should be converted to "11 May 2012". 
# If the dictionary is in Swedish

swedish = {1:"januari", 2:"februari", 3:"mars", 4:"april", 5:"maj", 
6:"juni", 7:"juli", 8:"augusti", 9:"september",10:"oktober", 
11:"november", 12:"december"}

# then "5/11/2012" should be converted to "11 maj 2012".

Japan = {1: 'Mys Genver', 2: 'Mys Whevrel', 3: 'Mys Merth', 4: 'Mys Ebrel',
    5: 'Mys Me', 6: 'Mys Efan', 7: 'Mys Gortheren', 8: 'Mys Est',
    9: 'Mys Gwyngala', 10: 'Mys Hedra', 11: 'Mys Du', 12: 'Mys Kevardhu'}
#'7/7/05'
#7 Mys Gortheren 05 
    

#'11/3/1848'

# Hint: int('12') converts the string '12' to the integer 12.

###########Below is my answer######################

def date_converter(dict, string):
    slash = string.find('/')
    slash2 = string.find('/', slash+1)
    
    day = string[slash+1:slash2]
    year = string[slash2+1:]
    
    month_int = int(string[0:slash])
    month = dict[month_int]
    
    date = day + ' ' +  month + ' ' + year
    return date

####professor's answer##############

#def date_converter(language, date):
 #   month, day, year = date.split('/')
  #  return day + ' ' + language[int(month)] + ' ' + year


#print date_converter(english, '5/11/2012')
#>>> 11 May 2012

#print date_converter(english, '5/11/12')
#>>> 11 May 12

#print date_converter(swedish, '5/11/2012')
#>>> 11 maj 2012

#print date_converter(swedish, '12/5/1791')
#>>> 5 december 1791
print date_converter(swedish,'11/3/1848')

print date_converter(Japan,'7/7/05')

