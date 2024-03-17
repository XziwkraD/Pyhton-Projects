while True:
    
    secret_word = input("Enter the secret word: ").lower()

    while not secret_word.isalpha():
        print("The secret word entered is invalid. Please re-enter a word that contains only letters!")
        secret_word = input("Enter the secret word: ").lower()

    attempts = input("Enter the number of attempts you are giving: ")

    while not attempts.isnumeric():
        print("The number of attempts that you have entered is invalid. please re-enter a number!")
        attempts = input("Enter the number of attempts you are giving: ")

    while attempts <= '0':
        print("The number of attempts that you have entered is invalid. please re-enter a positive number!")
        attempts = input("Enter the number of attempts you are giving: ")

    attempts = int(attempts)

    current_state = ['_'] * len(secret_word)
    current_state_str = ''.join(current_state)
    current_state_now = ' '.join(current_state)

    print(current_state_now)
    
    while attempts > 0:

        guessed_leword = input("Enter your guess: ").lower()

        while not guessed_leword.isalpha():
            print("The letter/word entered is invalid. Please re-enter a letter/word!")
            guessed_leword = input("Enter your guess: ").lower()
            attempts += 1 

        correct_guesses = 0

        if len(guessed_leword) == 1: #for single letter guesses
            for index, letter in enumerate(secret_word):
                if guessed_leword == letter:
                    current_state[index] = guessed_leword
                    correct_guesses += 1

        if len(guessed_leword) == len(secret_word): #for word guesses
            for index, letter in enumerate(secret_word):
                for num, guess in enumerate(guessed_leword):
                    if guess == letter:
                        if current_state[index] == "_":
                            current_state[index] = guess
                            correct_guesses += 1

        wrong_guesses = 0
        for indiv_letter in guessed_leword:
            if indiv_letter not in secret_word:
                wrong_guesses += 1
            attempts -= wrong_guesses

        print(f"You have {correct_guesses} correct guess(es)!")
        current_state_str = ''.join(current_state) # iterated variable
        current_state_now = ' '.join(current_state) # display variable
        print(f"Current state: {current_state_now}")
        print(f"Attempts left: {attempts}")

        if attempts == 0:
            print("You have run out of attempts! Better luck next time!")
            break

        if secret_word == current_state_str:
            print(f"Correct! The word is {secret_word}!")
            break
            
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break