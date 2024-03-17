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

        guessed_letter = input("Enter your guess: ").lower()

        while not guessed_letter.isalpha():
            print("The letter/word entered is invalid. Please re-enter a letter/word!")
            guessed_letter = input("Enter your guess: ").lower()
            attempts += 1 
    
        for index, letter in enumerate(secret_word): #adds the correct letter into the current_state
            if guessed_letter == letter:
                current_state[index] = guessed_letter

        correct_guesses = 0
        if guessed_letter in secret_word:
            correct_letters_index = filter(lambda x: secret_word[x] == guessed_letter, range(len(secret_word))) 
            #filters the indices of the correct letters from the word
            for index in correct_letters_index:
                correct_guesses += 1

        wrong_guesses = 0
        for indiv_letter in guessed_letter:
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