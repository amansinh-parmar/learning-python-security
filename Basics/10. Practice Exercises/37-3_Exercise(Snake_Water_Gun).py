# 1.Snake, Water, Gun
# 2.Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" 
# where players use hand gestures to represent a snake, water, or a gun. 
# 3.The gun beats the snake, the water beats the gun, and the snake beats the water. Write a python program to create a Snake Water Gun game in Python using if-else statements. Do not create any fancy GUI. Use proper functions to check for win.
''' 
                 S W G
computer =      -1 0 1
            S -1 D W L
player   =  W  0 L D W
            G  1 W L D
'''
import random 

def get_usr_choice():
    print("( Snake/Water/Gun ) \nEnter your choice: ")
    user_choice = input().lower()
    while user_choice not in ['snake','water','gun']:
        print("Invalid choice!! Please enter your choice Snake, Water, Gun.")
        user_choice = input().lower()
    return user_choice

def get_computer_choice():
    return random.choice(['snake','water','gun'])

def determine_result(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's tie!"

    if (user_choice == 'snake' and computer_choice == 'water') or \
        (user_choice == 'water' and computer_choice == 'gun') or \
        (user_choice == 'gun' and computer_choice == 'snake'):
        return "You win!"
    else:
        return 'Computer win!'

def play_game():
    print("<< Welcome to Snake, Water, Gun game..!! >>")
    while True:
        user_choice = get_usr_choice()
        computer_choice = get_computer_choice()

        print(f"Your choice: {user_choice.capitalize()}")
        print(f"Computer choice: {computer_choice.capitalize()}")

        result = determine_result(user_choice, computer_choice)
        print(result)

        play_again = input("Do you want to play again?(yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    play_game()