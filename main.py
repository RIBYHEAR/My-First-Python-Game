import os

print("Hello, Welcome to my First Game!")
name=input("What is your name? ")
age=int(input("What is your age? "))

if age >=18:
    print(f"Hello {name}, you are old enough to play!")
    wants_to_play= input("Do you want to play? ").upper()
    if wants_to_play == "YES":
        print("Great, lets play!")
        health = 100
        print(f"You are starting with {health} health.")
        left_or_right= input("First Question... Do you want to go left or right? ").lower()
        if left_or_right == "left":
            ans = input("Good job you followed the path safely to your location you have reached a river do you swim acroos or take the boat?(swim/boat) ").lower() 
            if ans=='boat':
                print("you got across the river safely and have now reached the other side.")

            elif ans == 'swim':
                print("you managed to get across the river but got bitten by a crocodile and lost 50 health.")
                health -= 50
            else:
                print('Sorry, that is not a valid input. Please restart the program.')

            ans = input("You see a cottage and a bakery. which do you go to?(cottage/bakery) ")
            if ans == "cottage":
                print("You go to the cottage and are greeted by the owner...they don't like you very much you lose 50 health.")
                health-= 50
                if health==0:
                    print("You have zero health you have now lost the game is over...")
                else:
                    print("You have survived for now...")
            elif ans == "bakery":
                print("You go to the bakery, then you stumble uppon some croisants. You eat them and die due to poisoning.")
                print('Game Over...')
            else:
                print('Sorry, that is not a valid input. Please restart the program.')
        elif left_or_right == "right":
            print('You fall into a hole and die...')
            print('Game Over...')
        else:
            print('Sorry, that is not a valid input. Please restart the program.')
    elif wants_to_play == "NO":
        print("Sorry to see you go...")
else:
    print(f"Sorry {name}, you are not old enough to play.")
        

       

   

