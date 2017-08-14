def begin_story(): 
    user_name = input("Please enter your name")
    print('You wake up in your math classroom at night with no one around on a stormy night.',
    'What do you do?')
    print('Enter the number that corresponds to your decision')
    user_response = int(input('1. You open the door to the classroom. \n2. You attempt to call your mother. \n3. You go back to sleep'))
    elevator(user_response, user_name)

def elevator(user_response, user_name):
    #1. You open the door to the classroom. 
    if (user_response == 1):
        print("you see what seems like a person run throught the hall")
        user_response = int(input("1. You say whos there to whatever you saw"))
        elevator(user_response, user_name)
        
    #2. You attemp to call your mother. 
    elif (user_response == 2):
        print('You call your  mother she answers but all you hear is breathing then the call ends,', user_name, ', whats going on?.')
        user_response = input("Choices TBD")

    #3. You go back to sleep'
    elif (user_response == 3):
        print('you lay down again', user_name, 'well good night.')
        user_response = input("Choices TBD")
        
    else:
        error(user_response)
        
def error(user_response):
    if(user_response == 2017):
        print("kys")
    else:
        print("Nice try! Now comply with the rules!")
        #add code to repeat gather user input

begin_story()
