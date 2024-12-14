sting='hang man game'
print(f"Welcome to the {sting.title()}!")

word='apple'
def word_array(word):
    d=['-']
    arr=[]
    for i in range(len(word)):
       arr.extend(d)
    return arr

def find_all_indexes(string, char):
    return [i for i, c in enumerate(string) if c == char]

def replace_at_indexes(string, indexes, letter):
    return [letter if i in indexes else char for i, char in enumerate(string)]
def match_letters(word):
    count = 0
    guesses=6
    arr=word_array(word)
    while count < guesses: 
      letter=input('Please Enter the word: ')
      if letter in word:
         ind=find_all_indexes(word, letter)
         arr=replace_at_indexes(arr, ind, letter)
       
      else:
          count+=1
          print(f'wrong guess ,lifes will be remaing {count}/{guesses}')
        #   hangman='o/\|/\ '
        #   for c in hangman(range(count)):
              
              
             
      print(arr)
      if '-' not in arr:
          print('You Won')
          break
    else:
        print('You Lost')
match_letters(word)
print(word)
  
