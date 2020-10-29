secret = "1"
guess = input("Guess the secret number...")
match = secret == guess
if match:
    print ("Congratulations, you guessed the right number!")
else:
    print("I'm sorry. This was not the correct number :(")