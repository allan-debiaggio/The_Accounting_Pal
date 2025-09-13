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

    while True :
        try : 
            number = int(input(user_select))
            if number < 1 or number > 6 :
                print("Give a number between 1 and 6 please")
                continue
            else : 
                break
        except ValueError :
            print("Give a number between 1 and 6 please")
            continue
        except KeyboardInterrupt :
            print("Quitting the program")
            break

    print(user_choice + str(number))

    # Need to block the using from using anything else than asked numbers



def dollars_display (dollars):
    
    for i in range(4) :
        print(dollars)

    return 0

main()

