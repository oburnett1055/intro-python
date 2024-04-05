def pascode():
    code=1234
    userinput=int(input('enter a code'))
    while userinput!=code:
        print('nice try taxes')
    userinput=int(input('enter a code'))
    if userinput==code:
        print('yes')
pascode()