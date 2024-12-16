import random
play=True
number=str(random.randiant(0,100))
print("i will generate a random which you have to guess.")
print("Guess a number 0 to 100,Guess 1 digit at a time,this might be a little challenging.")
print("The game will end when you guess the correct number")

while play:
    guess=input("Guess your best guess: ")
    if number == guess:
        print("You have won the match")
        print("the number was",number)
        print("You have won 'Guessing god' title")
        break
    else:
        print("Your guess is incorrect try again,Dont give up")