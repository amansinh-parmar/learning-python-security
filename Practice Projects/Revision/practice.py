
## Game >> Snake, Water, Gun << 

import random 

def get_usr_choice():
    print("'Snake/Water/Gun'\nEnter your choice: ")
    usr_choice = input().lower()
    if usr_choice not in ['snake','water','gun']:
        print("Invalid choice..!! Please enter either 'Snake, Water, Gun'.")
        usr_choice = input().lower()
        return 
    return usr_choice

def computer_choice():
    return random.choice(['snake','water','gun'])

def choice_result(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "It's Tie"

    if (user_choice == 'snake' and comp_choice == 'water') or \
        (user_choice == 'water' and comp_choice == 'gun') or \
        (user_choice == 'gun' and comp_choice == 'sanke'):
        return "You win..!" 
    else:
        return "Computer Win....."

def play_game():
    while True:
        user_choice = get_usr_choice()
        comp_choice = computer_choice()

        print(f"Your choice: {user_choice.capitalize()}")
        print(f"Computer choice: {comp_choice.capitalize()}")

        result = choice_result(user_choice, comp_choice)
        print(f"Result is {result}.")

        play_again = input("Do you want to play again? (y/n): ") 
        if play_again != 'y':
            break

if __name__ == "__main__":
    play_game()

