def warmup():
    usersgrade=int(input('what is your grade'))
    if usersgrade>3000:
        print('nice score')
    else:
        print('low score')
warmup()





def gradebook(studentgrade):
    if studentgrade>=60 and studentgrade<=69:#this is the highest you can go from b
        print('b')#after this rince and repeat for more results ,you dont need to add and for the conclusion,A
    elif studentgrade>=80:
        print('a')
    else:
        print('your failing') #conclusion

gradebook() #to avoid errors find a problem in the code then make a code for that error