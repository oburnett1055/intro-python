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
