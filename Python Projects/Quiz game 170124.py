def new_game():
    
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print()
        print(key)
        for i in options[question_num-1]:
            print(i)
        while True:
            guess = input("Enter your option(A, B, C, D): ")
            guess = guess.upper()
            if guess not in ["A", "B", "C", "D"]:
                print("You have not entered a valid option. Please re-enter again.")
            else:
                guesses.append(guess)
                break

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0

def display_score(correct_guesses, guesses):
    print()
    print("RESULTS")
    print("-------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")
    
def play_again():
    
    response = input("Do you want to play again? (Yes or No): ")
    response = response.upper()

    if response != "YES":
        return False
    else:
        return True

questions = {
    "Who created Python? ": "A",
    "What year was Python created? ": "B",
    "Python is tributed to which comedy group? ": "C",
    "Is the Earth round? ": "A"
}

options = [
    ["A, Guido wan Rossum", "B, Elon Musk", "C, Bill Gates", "D, Mark Zuckerburg"],
    ["A, 1347", "B, 1991", "C, 1619", "D, 2016"],
    ["A, Lonely Island", "B, Smosh", "C, Monty Python", "D, The Beatles"],
    ["A, True", "B, False", "C, Sometimes", "D, What's Earth?"]
]

new_game()

while play_again():
    new_game()

print("Thanks for playing!")