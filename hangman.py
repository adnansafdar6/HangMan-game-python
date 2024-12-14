def word_array(word):
    return ['-'] * len(word)

def find_all_indexes(string, char):
    return [i for i, c in enumerate(string) if c == char]

def replace_at_indexes(string, indexes, letter):
    return [letter if i in indexes else char for i, char in enumerate(string)]

def match_letters(word):
    count = 0
    guesses = 6
    arr = word_array(word)
    hangman_parts = ['o', '/', '\\', '|', '/', '\\']
    
    while count < guesses: 
        print(f"Current word: {' '.join(arr)}")
        letter = input('Please Enter a letter: ').lower()
        
        if len(letter) != 1 or not letter.isalpha():
            print("Please enter only a single letter.")
            continue
        
        if letter in word:
            ind = find_all_indexes(word, letter)
            arr = replace_at_indexes(arr, ind, letter)
        else:
            count += 1
            print(f'Wrong guess. Lives remaining: {guesses - count}/{guesses}')
            for i in range(count):
                print(hangman_parts[i % len(hangman_parts)]) 
        
        if '-' not in arr:
            print(f"Congratulations! You've guessed the word: {''.join(arr)}")
            break
    else:
        print(f"You lost! The word was: {word}")


word = input('Please Enter a word:')
print(f"Welcome to the Hangman Game!")
match_letters(word)


  
