# Midterm quiz. 
# Create a new python document called midtermquiz.py
# Complete the following questions.
# Once you have comepleted your quiz, commit and sync your work to your GitHub. 

#RULES
# This quiz is open book; you may use your notes, google (only if you are viewing arcticles about python), W3schools only. Any other website
# is prohibitied.
# No phones are allowed during the quiz. refusal to put away a phone will result in failure.
# There is no talking during the quiz. If you complete the quiz, notify the instructor that you
# have finished. Once that is done, you are free to use your device and browse the web quitely. 

# Good Luck

# 1. In your own words, describe what the difference
# between a function arguement and a function parameter.
# Write your response using complete sentences.
'a function argument and parameter are one of the same coin. The parameter gives the argument a purpose, a name and the argument give action, a defintion to that name.'
# 2. In your own words, describe what each of the following errors means.
# Write your response using complete sentences.

# syntax error
'syntex error means your not speaking the language of the system.'
# type error
"the lack of grammer in ones writing"
# name error
" name error means You have a variable that is not defined meaning that your varible has no action to it."

# 3. What function would I use if I wanted to convert an integer data type into 
# a string data type?
'str()'

# 4. What function would I use if I wanted to change a float data type into a 
# an integer data type?
'int()'

# 5. Describe three (3) Variable naming rules. Write your response in complete sentences. 
'snake example (cheese_word) looks like a snake from a distence/cammle example (CheeseBurgar) i guess this can look like a cammle's back'
"and pascale(i forgot this one not sure if i looked it up right but couldnt find it)."

# 6. Name the operator family each of these symbols are a part of 
# and describe how each of these sybmols are used. Write your response
# useing complete sentences. 

#symbols
# = 
'assignment'
# == 
'comparison'
# =!
'comparison'

# 7. You have been hired as an engineer to develop a car speed detection system.
# the car company would like to create a function where if the user goes over a certain
# speed it will notify them to change gears. The client has provided you with the following
# guidelines on how they would like the gear system to work:
# if the driver is going over 20mph, alert the driver to shift to gear 1
# if the the driver is going over 30mph, alert the driver to shift to gear 2
# if the driver is going over 40mph, alert the driver to shift to gear 3
# if the driver is going over 70mph, alert the driver to shift back to gear 1.
# the client would like you to pass in the speed that the user is going as an argument. 
# Please provide three (3) clues/ keywords and explain why you chose them to get full credit.

#key words 
#print
#if ,else,elif
#argument
def lightspeed(speedMPH):
    if speedMPH>20:
        print('shift to gerar 1')
    elif speedMPH>30:
        print('shift to gear 2')
    elif speedMPH>40:
        print('shift to gear 3')
    elif speedMPH>70:
        print('return to gear 1')
    else:
        print('nice driving')
lightspeed()

# 8. You have been hired as an engineer to develop a fitness meal plan program. 
# your function should take in two (2) arguements; the day of the week, and the time of the day.
# depending on the time of the day; either morning or afternoon, the meal plan will change. 
# the client has provided you with the following meal plan information
# Please provide three (3) clues/ keywords and explain why you chose them to get full credit.

# monday morning= 2 eggs and an apple
# monday afternoon= bbq grilled chicken and broccoli

# tuesday morning= oatmeal with strawberries and blueberries
# tuesday afternoon= baked chicken with kale

# wednesday morning= fruit salad
# wednesday afternoon= curry goat with rice and cabbage

# thursday morning= pancakes and turkey sausage
# thursday afternoon= eggplant pasta

# friday morning= steak and eggs
# friday afternoon= cheesburger and fries

# saturday morning= oatmeal
# saturday night= baked chicken with string beans

# sunday morning = oatmeal
# sunday night = steak and spinach
    
def loseweight(time,day,feelings):
        input("good morning hows your day")
        if feelings=='bad':
            print('sorry')
        elif feelings=='good':
            print('no')
        if time=='morning' and day=='mon':
            print('2eggs and a apple')
        elif day=='mon' and time=='afternoon':
            print('chicken and veggies')
        if time=='morning' and day=='tue':
            print('oatmeal and fruit')
        elif day=='tue' and time=='afternoon':
            print('chicken and kale')
loseweight('tue','morning','good')

# 9. You have been hired as an enineer to develop a school to develop an academic honors system.
# the client would like to check if the user has gotten above an 85% overall grade or has
# has accomplished passing the SAT. The client would like you to pass this information in as
# arguements. If either of these situations are true the student has made the academic honors list
# if only passing the SAT is true, congratulate the user but inform them they did not make the list.
# if they only scored above 85%, congratulate the user but inform them they did not make the list.
# if none of the conditions are met, inform them to continue studying and try again next semester. 
# Please provide three (3) clues/ keywords and explain why you chose them to get full credit.
def honorscheck(grade,sat):
    if grade >=85 and sat:
        print('congrats you have made honors')
    elif grade <85 and sat:
        print('congrats on your sat howerver  you did not make honors ')
    elif grade >=85 and not (sat):
        print('congrats on your grade however you did not make honors')
    elif grade < 85 and not(sat):
        ('please try agian next year')
honorscheck(60,False)
# 10. Create a function that will check the temperature outside. If the user enters
# a number above 60 degrees it is warm outside, if the enter a number above 80 degrees it is hot outside.
# if the user enters a number below 50 degrees it is cold outside. and if the tempeature is above 50 degrees,
# tell the user it's not warm but it's also not too cold. 
# Please provide three (3) clues/ keywords and explain why you chose them to get full credit.

#keyword 
# conditiolns
#<>
#true/false

def tempcheck():
    temp=int(input('what is the temp outside'))
    if temp<50:
        print('its cold outside')
    elif temp >=50 and temp <60:
        print('its human')
    elif temp >=60 and temp <80:
        print('its warm outside')