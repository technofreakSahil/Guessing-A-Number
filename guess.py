import random 

number = int(input("Enter a number"))
random_number = random.randrange(0,number)
count=0
while True:
    guess_number = int(input("Guess a number"))
    if guess_number == random_number:
     print("You guessed it correct")
     print("You got it correct in", count, "guesses")
     break
    else:
       count +=1
       print("You got it wrong!")
