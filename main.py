import os, colorama
from colorama import Fore, init
init(autoreset=True)
os.system('title Choices - Live or Die')
print(f"{Fore.GREEN}Hello, Welcome to Choices - Live or Die!")
name=input(f"{Fore.GREEN}What is your name? ")
age=int(input(f"{Fore.GREEN}What is your age? "))

if age >=13:
    print(f"{Fore.GREEN}[AGE VERIFICATION]{Fore.RESET}Hello {name}, you are old enough to play!")
    wants_to_play= input(f"{Fore.GREEN}[GAME]{Fore.RESET}Do you want to play? ").upper()
    if wants_to_play == "YES":
        print(f"{Fore.GREEN}Great, lets play!")
        health = 100
        print(f"{Fore.GREEN}[HEALTH]{Fore.RESET}You are starting with {health} health.")
        left_or_right= input(f"{Fore.GREEN}First Question... Do you want to go left or right? ").lower()
        if left_or_right == "left":
            ans = input(f"{Fore.GREEN}[GAME]{Fore.RESET}Good job you followed the path safely to your location you have reached a river do you swim acroos or take the boat?(swim/boat) ").lower() 
            if ans=='boat':
                print(f"{Fore.GREEN}[GAME]{Fore.RESET}you got across the river safely and have now reached the other side.")

            elif ans == 'swim':
                print(f"{Fore.RED}[GAME]{Fore.RESET}you managed to get across the river but got bitten by a crocodile and lost 50 health.")
                health -= 50
            else:
                print(f'{Fore.RED}Sorry, that is not a valid input. Please restart the program.')

            ans = input(f"{Fore.GREEN}[QUESTION]{Fore.RESET}You see a cottage and a bakery. which do you go to?(cottage/bakery) ")
            if ans == "cottage":
                print(f"{Fore.RED}[GAME]{Fore.RESET}You go to the cottage and are greeted by the owner...they don't like you very much you lose 50 health.")
                health-= 50
                if health==0:
                    print(f"{Fore.RED}You have zero health you have now lost the game is over...")
                else:
                    print(f"{Fore.RED}[GAME]{Fore.RESET}You have survived for now...")
            elif ans == "bakery":
                print(f"{Fore.RED}[GAME]{Fore.RESET}You go to the bakery, then you stumble uppon some croisants. You eat them and die due to poisoning.")
                print(f'{Fore.RED}Game Over...')
            else:
                print(f'{Fore.RED}Sorry, that is not a valid input. Please restart the program.')
        elif left_or_right == "right":
            print(f'{Fore.RED}[GAME]{Fore.RESET}You fell into a hole and died...')
            print(f'{Fore.RED}[GAME]{Fore.RESET}Game Over...')
        else:
            print(f'{Fore.RED}Sorry, that is not a valid input. Please restart the program.')
    elif wants_to_play == "NO":
        print(f"{Fore.RED}Sorry to see you go...")
else:
    print(f"{Fore.RED}Sorry {name}, you are not old enough to play.")
