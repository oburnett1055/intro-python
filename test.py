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
        elif time=='morning' and day=='tue':
            print('oatmeal and fruit')
        elif day=='tue' and time=='afternoon':
            print('chicken and kale')
loseweight('tue','morning')
