# Async Assignment March 3rd, 2024. 

# Complete and solve the following prompts.
# With each prompt, write down the clues and keywords you found.
# This will count toward your grade. 
# Make sure to write down the clues and keywords you found.
# (Make sure to include your clues and keywords to recieve full credit)

# Commit and sync your work before the end of class. 
# This will count toward your class activity grade. 

#1. Elevator Conditional Function Execercise.
# Prompt #1- Elevator Conditional Function Execercise.

# You have been hired by a architeture firm to assist 
# with developing their elevator system. They have asked 
# you to develop a function that will accept user's input. 
# you to develop a function that will accept a user's input. 
# your program should ask the user to enter a floor number. 
# When an user enters a number they will be sent to a specific 
# floor in the building. If the user enters a floor number that does not
# exist, your program should inform the user that the floor they entered
# does not exist and to enter and to try agin. The architects have
# given you the following lists of floors for their building:
# does not exist and to enter another number and to try agin.

# The architects have given you the following 
# lists of floors for their building:

# M = 'lobby'
# B = 'basement'
'@@ -23,11 +29,14 @@'
# 3 = 'workspace'
# 4 = 'living quarters'

'(answer/clues input or function,print,elif,if,else,int,varibles,function call and check for errors these are the tools needed to complete the task)'
def elevatorSystem():
    
     floor=int(input('what is your floor'))
     if floor==1:
       print('going to floor 1')#after this use elif over and over again
     else:
        print('run')

#elevatorSystem()

#___________________________________________________________

# 2. You have been hired by an amusement park to develop a program
# that allows users to access their roller coasters by entering the age,
# height. Your client has very specific requirements for thier guests to
# ride their roller coasters and have provided you with the following 
# Prompt #2- Amusement Park Conditional Function
# You have been hired by an amusement park to develop a function
# that allows users to access their roller coasters by entering their age
# and height. Your program should take the user's height and age as parameters.
# Your client has very specific requirements for thier guests 
# to ride their roller coasters and have provided you with the following 
# conditions that they would like your program to check for. 

# user must be atleast 5.2 or taller and atleast 14 years old or older 

'(answer/clue/age,height,<>=,if,else,input or,function,function call and print)'

def rollertoaster(height,age):
    if height>=5.2 and age>=14:
        print('say cheese for roller coaster 1')
    elif height<5.2 and age>=14:
        print('run away and go to roller coaster 2')
    elif height<5.2 and age<14:
        print('go to ride 3 please')
    else:
        print('why are you that tall')


rollertoaster(5.2,14)
