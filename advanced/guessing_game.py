import random


print("Guess the number of seeds in papaya")
print("...................................")

mm_count = random.randint(1, 100)
attempt_limit = 5
attempts = 0

while attempts < attempt_limit:
    guess_text = input("How many seed? ")
    guess = int(guess_text)
    attempts += 1

    if mm_count == guess:
        print("You got a free lunch! It was",guess)
        break
    elif guess < mm_count:
        print("Sorry, that's too LOW!")
    else:
        print("That's too HIGH!")

print("Bye, you're done in",attempts)