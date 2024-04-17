# Warm up Tuesday April 17th, 2024.

import random

# 1. In your own words, explain the difference between an Python For Loop and a
# Python While Loop. a for loop counts  a existing limit and a while loop counts a nonexisting limit a for a true statement 

# 2. Create a loop that will iterate over a list of numbers. For evey number in your loop,
cats=[1,2,3]
for cats in cats:
    if 1==1:
        cats*=3
        print(cats)
# it should multiply that number by 3. 

# 3. Use the following code snippet below to create a guessing game function. 
# The code below will generate a ran if they guess incorrectly, the program will repeat 
# itself and ask the user to guess again. The program should continue to ask them to
# guess until they've gotten it corrdom number for you. You must write a loop that will
# ask the user to input their guess,ectly. Once they guess the correct number the program
# will congratulate them and the loop will stop. 

# generates a random number between 1 and 10
#randomNumber = random.randint(1, 10)

print('Random number value is: {randomNumber}')


Guess= random.randint(1,10)
p1=int(input('whats the number'))
if p1==Guess:
    print('nice')
while p1!=Guess:
    print(p1=int(input('whats the number')))
else:
    print(Guess)


#def guess():
    #randomNumber = random.randint(1, 10)
    #print(f'what is the number'{randomNumber}')
    #i=int(input('guess')

    def aletters():
        list=['a,b,'c']
