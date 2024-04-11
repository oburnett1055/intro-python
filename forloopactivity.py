#for loop - construct that will will repeat data


birdGame=['duck,duck,gooseduck,duck,goose']
for x in birdGame:
    print(x)

birdGame=['duck,duck,gooseduck,duck,goose']
for x in birdGame:
    if x=='goose':
        print(f'goose'{birdGame.index('goose')}'')
        continue#for loops are not infinite but they do prinht a result for each listing or index effectivliy scanning the list for the value/index

def costumerReturn():
    userreturns=input('what would you like to return')
    reciept=('drugs , coke , that good stuff')
    for item in reciept:
        if item==userreturns:
            reciept.remove(userreturns)
            print('your refund is done ')
            print(reciept)
            #insert is a addition function for a list