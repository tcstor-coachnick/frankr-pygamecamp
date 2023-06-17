import random 
target = random. randint(1, 100)
tries = 10 
while True:
    guess = input("guess a number between one and one hundred ")
    guess = int (guess)
    tries -= 1
    if guess > target :
        print("guess lower")
    elif guess < target :
        print("guess higher")
    elif guess == target:
        print("correct")
        break  
    if tries == 0:
        print("you lost boo hoo")
        break
