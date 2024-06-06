questions = {
    "Who created the earth?: ": "A",
    "Who is the son of GOD? ": "B",
    "Man was made in GOD's? ": "C",
    "GOD values what most? ": "C"
}  

options =[
    ["A. GOD", "B. man", "C. satan", "D. stones"],
    ["A. Terminal", "B. Jesus Christ", "C. Ports", "D. Debug console"],
    ["A. Hate", "B. Misery", "C. Image", "D. Song"],
    ["A. Sacrifice", "B. Hate", "C. Love", "D. Anger"]
]

def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG")
        return 0


def display_score(correct_guesses, guesses):
    print("------------------")
    print("RESULTS")
    print("------------------")

    print("The Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()   

    print("Your Answers: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()   

    score = int((correct_guesses/len(questions))*100)  
    print("Your score is: " + str(score)+ "%")     

def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    #Display all questions:

    for key in questions:
        print("-----------------------------")
        print(key)

    #Display all answers for each question:

        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess) # Append to empty guesses list.

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1     # Increment to go to the next list of answers. (0, then 1, then 2)

    display_score(correct_guesses, guesses)

new_game()





    

def play_again():
    
    response = input("Do you want to play again?: (yes or no) ")

#Define the questions
