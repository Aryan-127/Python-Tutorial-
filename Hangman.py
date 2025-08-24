import random
print("Welcome to the Hangman Game!\nYou are supposed to guess a five letter word.\nLet's begin!")
words = ["apple", "grape", "pearl", "stone", "light", "track", "chair", "plane", "smile", "water", "earth", "bread", "brick", "flame", "music", "river", "field", "clock", "tiger", "sweet"]
while True:
  choice = random.choice(words)
  word = list("_____")
  j = 9
  set = set()
  while True:
    word = list(word)
    guess = input("Enter a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter!")
        continue
    if guess in set:
        print("You have already tried that letter!")
        continue
    for i in range(len(choice)):
      if choice[i] == guess:
          word[i] = guess
         
    word = "".join(word)
    print(word)
    if guess not in choice:
      
      if j > 0:
          print("Nope! You have", j, "turns left")
          j -= 1
          set.add(guess)
          continue    
    
      else:
          print("You lost!\nThe word was",choice)
          break
    if word == choice:
        print("Congratulations! You won.")
        break
  ask = input("Do you want to play again?\n==>")
  if ask in ["Yes", "yes", "Y", "y", "Yeah","yeah", "yup", "Yup"]:
     print("Here we go again!")
     continue
  else:
     print("Thanks for playing!")
     break
    
    
    

          
          
    
    
 