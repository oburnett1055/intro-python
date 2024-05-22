#$import random

#adj=['big','little', 'hot', 'cool']

#vowels=['a','e','i','o','u']
#cons=['b','c','d','f','g','j','k','l','m','n','p','s','t','v','z']

#def cats():
    #randomnumber=random.randint(2,4)
    #name=''
    #for x in range(randomnumber):
     #   randomvowel=random.choice(vowels)
      #  randomcons=random.choice(cons)
       # name=name+randomvowel+randomcons
    #return name

#print(cats())




#test
#generates a nick name based off of 4 traits
#1 pops up 4 optional traits


# PRIMARY OBJECTIVE - create a program that will ask the user 4 identifying questions based on traits. These traits will be used to generate a nickname.
# HOW TO/ INSTRUCTIONS
# - my function should ask the user a series of questions, their responses will be stored for later.
# example - question for user: which of the following foods do you enjoy most : a. pizza, b. sandwiches, c. nachos
# example - question for user: which of the following activities do you enjoy the least: a. sports, b. reading, c. video games

# once the user has answered all the questions. their response data will be passed into another function that will
# generate the nickname.  
#test 2



#print('hello please pick 4 personal traits to begin')
#pizza=input('what is your favorite pizza')
#bob=input('do you like bob')
#color=input('what is your color')
#cheese=pizza+bob+color
#print(cheese)


#poop=len(input('what is the color of poop'))
#print(poop)

#word=[1,2,3]
#print(word[poop])

import random


startname1=['b','t','k','z','o','p','ch','p','z','r','a','sh','l','w']
startname2=['ap','i','u','e','ro','ui','ar','ee','io','lo','er','oa','le','iu','up','am']
startname3=['chu','yu','co','d','x','ma','bing','y','t','tra','f','s','w','p','k','v','','','','']
start=input('would you like to start your nick name yes or no')

def warriornickname():
    pizza=len(input('what is your favorite pizza topping?'))
    animal=len(input('what is your favorite animal?'))
    hobby=len(input('what is your favorite hobby?'))
    random.shuffle(startname1)
    random.shuffle(startname2)
    random.shuffle(startname3)
    name=startname1[pizza]+startname2[animal]+startname3[hobby]
    print((name))
    retry=input('would you like to start again')
    if retry=='yes':
        print(warriornickname())
while start=='yes':
    print(warriornickname())
if start=='no':
    print('bye have a great day')











