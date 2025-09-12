import os
import time

def main(): 
    title = "I"*6 + "x"*3 + "===~~~~--- THE ACCOUNTING PAL ---~~~~===" +"x"*3 + "I"*6
    dollars = "I"*6 + "x"*3 + "===~~~~--- $$$ $$$$$$$$$$ $$$ ---~~~~===" + "x"*3 + "I"*6
    user_select = "Choose between 1 to 6 ? "
    user_choice = "Here's "

    dollars_display(dollars)
    print(title)
    dollars_display(dollars)

    time.sleep(3)
    os.system('cls') # Cleans the terminal screen
    number = input(user_select)

    print(user_choice + number)

    # Need to block the using from using anything else than asked numbers



def dollars_display (dollars):
    
    for i in range(4) :
        print(dollars)

    return 0

main()

