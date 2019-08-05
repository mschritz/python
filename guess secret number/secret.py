
secret = 22
guess =0

print(secret)

while guess != secret:
    guess = input("Was schätzt du? ")

    print(guess)

    if secret == int(guess):
        print("Correct!")
        break
    elif int(guess) > secret:
        print("Too large, The secret number is smaller than:" + str(guess))
    elif int(guess) < secret:
        print("Too small, The secret number is larger than:" + str(guess))
    else:
        print("I do not understand:" + str(guess))