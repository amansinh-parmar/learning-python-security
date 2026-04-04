#==> Exercise 1:
import time

t = time.strftime('%H:%M:%S')
hour = int(time.strftime("%H"))
name = str(input("Enter Your Name: "))
name = name.capitalize()
hour = int(input("Enter your hour: "))
print(hour)
''' 
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
'''
# Condition Statement:
'''if (hour>= 0 and hour <12):
      print("Good Morning,", name)
elif (hour>= 12 and hour <17):
      print("Good Afternoon,", name)
elif (hour>= 17 and hour <24):
      print("Good Evening,", name)'''



#==> Exercise 2:
'''create a program capable of displaying questions to theuser like KBC.
Use list data type to store the questions and their correct answers. 
Display the final amount the person is taking home after playing the game.'''

def kbc_game():
    # List of questions, correct answers, and the prize amounts
    questions = [
        {"question": "What is the capital of India?", "answer": "New Delhi", "prize": 1000},
        {"question": "Who wrote 'Hamlet'?", "answer": "William Shakespeare", "prize": 2000},
        {"question": "Which planet is known as the Red Planet?", "answer": "Mars", "prize": 3000},
        {"question": "What is the largest ocean on Earth?", "answer": "Pacific Ocean", "prize": 5000},
        {"question": "Who invented the telephone?", "answer": "Alexander Graham Bell", "prize": 10000},
        {"question": "What is the largest mammal?", "answer": "Blue Whale", "prize": 20000},
        {"question": "In which country is the Great Barrier Reef located?", "answer": "Australia", "prize": 40000},
        {"question": "What is the speed of light?", "answer": "299792458", "prize": 80000},
        {"question": "Who was the first man to walk on the moon?", "answer": "Neil Armstrong", "prize": 160000},
        {"question": "What is the currency of Japan?", "answer": "Yen", "prize": 320000},
    ]
    
    total_prize = 0
    for i, q in enumerate(questions, start=1):
        print(f"Question {i}: {q['question']}")
        user_answer = input("Your answer: ").strip()

        # Check if the answer is correct
        if user_answer.lower() == q['answer'].lower():
            print("Correct!")
            total_prize += q['prize']
        else:
            print(f"Incorrect! The correct answer is {q['answer']}.")
            break  # End the game if the user gives an incorrect answer
        
    print(f"\nYou are taking home a total of {total_prize} rupees.")

# Run the game
kbc_game()
