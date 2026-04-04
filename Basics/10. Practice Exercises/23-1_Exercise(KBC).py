
questions = [
    [
        "What is the capital state of India? ",
        "Chennai","Gujarat","Delhi","Punjab","None",3
    ],
    [
        "How many players are playing in one team in cricket game? ",
        "10","14","12","11","None",4
    ],
    [
        "Cleanest city in India?",
        "Punjab","Surat","Mumbai","Kerala",2
    ],
    [
        "First world highest goal scorer player in the world?",
        "C.Ronaldo","L.Messi","Mbappe","Neymar JR",1
    ],
    [
        "World richest person name?",
        "M.Ambani","A.Adani","E.Musk","W.Buffett",3
    ],
    [
        "What is the gaming laptop company name?",
        "Apple","Asus","Android","Microsoft",2
    ],
    [
        "How many days comes in leap month?",
        "30","28","29","31",3
    ]
]

levels = [5000,10000,20000,50000,100000,200000,500000]
money = 0

for i in range(0, len(questions)):
    question = questions[i]

    print(f"\nQuestion for ₹{levels[i]}")
    print(f"\n{question[0]}")
    print(f"A.{question[1]}                               B.{question[2]}")
    print(f"C.{question[3]}                               D.{question[4]}")

    # using "try" syntax to avoid any error and run program 
    try:
        reply = int(input("Enter your answer(1-4) or 0 for quit the game: "))
        # for quit the program   
        if reply == 0:
            money = levels[i-1]
            print(f"CONGRATULATIONS, You have won ₹{money}")
            break
        # for answers are true
        if reply == question[-1]:
            print(f"Correct Answer,\n You have won ₹{levels[i]}")
            # for set the levels if any answer wrong jump down to the levels
            if i == 1:
                money = 10000
            elif i == 3:
                money = 50000
            elif i == 6:
                money = 500000
        else:
            print("WRONG ANSWER.....!!!!")
            break
        # put "errors names" to avoid any specific error
    except (ValueError,IndexError,KeyError):
        print("Invalid choice, GAME OVER!!!!!!!")
        # print(f'Your final score is: ₹{money}')
        break
