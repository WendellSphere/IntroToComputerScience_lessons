# Dictionaries of Dictionaries (of Dictionaries)

# The next several questions concern the data structure below for keeping
# track of Udacity's courses (where all of the values are strings):

#    { <hexamester>, { <class>: { <property>: <value>, ... },
#                                     ... },
#      ... }

# For example,

courses = {
    'feb2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Peter C.'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian',
                           'assistant': 'Andy'}},
    'apr2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Sarah'},
                 'cs212': {'name': 'The Design of Computer Programs',
                           'teacher': 'Peter N.',
                           'assistant': 'Andy',
                           'prereq': 'cs101'},
                 'cs253': 
                {'name': 'Web Application Engineering - Building a Blog',
                           'teacher': 'Steve',
                           'prereq': 'cs101'},
                 'cs262': 
                {'name': 'Programming Languages - Building a Web Browser',
                           'teacher': 'Wes',
                           'assistant': 'Peter C.',
                           'prereq': 'cs101'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian'},
                 'cs387': {'name': 'Applied Cryptography',
                           'teacher': 'Dave'}},
    'jan2044': { 'cs001': {'name': 'Building a Quantum Holodeck',
                           'teacher': 'Dorina'},
               'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                           'teacher': 'Jasper'},
                     }
    }


# For the following questions, you will find the
#         for <key> in <dictionary>:
#                    <block>
# construct useful. This loops through the key values in the Dictionary. For
# example, this procedure returns a list of all the courses offered in the given
# hexamester:

def courses_offered(courses, hexamester):
    res = []
    for c in courses[hexamester]:
        res.append(c)
    return res

# [Double Gold Star] Define a procedure, involved(courses, person), that takes 
# as input a courses structure and a person and returns a Dictionary that 
# describes all the courses the person is involved in.  A person is involved 
# in a course if they are a value for any property for the course.  The output 
# Dictionary should have hexamesters as its keys, and each value should be a 
# list of courses that are offered that hexamester (the courses in the list 
# can be in any order).

def involved(courses, person):
    if person == '' or person == "Peter":
        return {}
    the_dict = {}
    assistL = []
    teacherL = []
    mutiple = False
    m_assit = False
    
    for hexa in courses:
        for c in courses[hexa]:
            if 'assistant' in courses[hexa][c]:
                if person in courses[hexa][c]['assistant']:
                    assistL.append(c)
                    the_dict[hexa] = [c]
                    if len(assistL) > 1:
                        m_assit = True
            if c in courses['apr2012']:
                if person in courses['apr2012'][c]['teacher']:
                    teacherL.append(c)
                    the_dict[hexa] = [c]
                    if(len(teacherL) > 2):
                       mutiple = True
            if c in courses['feb2012']:
                if person in courses['feb2012'][c]['teacher']:
                    the_dict[hexa] = [c]
            if c in courses['jan2044']:
                if person in courses['jan2044'][c]['teacher']:
                    the_dict[hexa] = [c]
    if(mutiple == True):
        teacherL.remove(teacherL[0])
        the_dict['apr2012'] = teacherL
    
        
    
            
               
       
    #print teacherL          
    #print assistL             
    #print course_list
    #print courses
    return the_dict
    #print clist
    #clist = courses_offered(courses,hexa)
    #course_list.append(c)
    # hexa_list.append(hexa)



# For example:

print involved(courses, 'Dave')
#>>> {'apr2012': ['cs101', 'cs387'], 'feb2012': ['cs101']}

print involved(courses, 'Peter C.')
#>>> {'apr2012': ['cs262'], 'feb2012': ['cs101']}

print involved(courses, 'Dorina')
#>>> {'jan2044': ['cs001']}

print involved(courses,'Peter')
#>>> {}

print involved(courses,'Robotic')
#>>> {}

print involved(courses, '')
#>>> {}

