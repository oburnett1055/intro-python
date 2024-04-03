#i#is a loop /iterator
i=1
while i<6:
    print(i)
    i+=1

inventory_hangers=0
while inventory_hangers <1:
    purchase=(input('would you like a hanger'))
    if purchase=='yes':
    inventory_hangers -=1
    print('hanger count:{hangers left}')

