# Starting a new quiz
def new_quiz():
    guesses = []
    points = 0 # set to 0 because the quiz has just begun (points)
    question_number = 1

    for key in questions:
        print(" ")
        print(key)
        #displaying the options with questions
        for i in choices[question_number - 1]:
            print(i)
        guess = input("Enter (A, B, C, D, or E): ")
        guess = guess.upper() # making the input upper case
        guesses.append(guess) # showing the attempted guesses

        # after attempt, the question will be checked for the answer and show the correct answer and how many guesses
        points += check_answer(questions.get(key), guess) # points will increase if the guess matches the correct answer
        question_number += 1 #adding the question number after each question

    show_score(points, guesses)

# Check if answer to question is correct or incorrect
def check_answer(answer, attempt):
    if answer == attempt:

        print("correct")
        return 1 # the point system for when their is a correct answer
    else:
        print("incorrect")
        return 0 # no point added for incorrect answer

# Displays the score as the quiz progresses
def show_score(points, guesses):
    print(" ")
    print("End score")
    print(" ")
    print("Answers: ", end="") # the correct answers
    for i in questions:
        print(questions.get(i), end=" ")
    print() #new line to look more organized

    print("Guesses: ", end="") # what the player had guessed
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((points/len(questions))*100) # calculates the score by correct number of answers / number of questions * 100 to show score as percentage
    print("Final score: "+str(score)+"%") # actually display the score

# Option to start another quiz once it has been completed
def quiz_plus():
    print(" ")
    new_game = input("Play again? (Y/N): ")
    new_game = new_game.upper()

    if new_game == "Y":
        return True
    
    else:
        return False

# making a dictionary for the questions, the answers are given as keys to the right of the question
questions = {
    "What kind of plant is a Monstera Deliciosa?: ": "E",
    "Is the Satin Pothos a Pothos or a Philodendron?: ": "D",
    "Which store has cheap plants? :": "C",
    "Are succulents deceivingly hard to take care of?: ": "B",
    "Which of these plants are toxic to pets?: ": "D"
}

# lists of all of the possible multiple choice answers to the questions
choices = [["A. Dracaena", "B. Pothos", "C. Calathea", "D. Sansevieria", "E. Philodendron"],
          ["A. It's a Pothos", "B. It's a Philodendron", "C. It's technically both", "D. It's technically neither"],
          ["A. White Oak Garden Center", "B. Benken", "C. Home Depot", "D. Burger Farm Garden Center"],
          ["A. False", "B. True"],
          ["A. ZZ Plants", "B. Philodendrons", "C. Pothos", "D. All of the above"]] 

new_quiz()

# everything containted in the new_quiz group so that the the quiz_plus will start everything again without rearranging the order

while quiz_plus():
    new_quiz()
print(" ")
print("Thanks for playing!")