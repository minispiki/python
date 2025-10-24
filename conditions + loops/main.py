while True: # Loop forever
    word = input("Give me a 3 letter word ") # str
    if len(word) == 3: # is word's length 3 letters?
        print("You did it, you gave me a 3 letter word!")
        break # exit
    elif len(word) == 0: # if condition isnt met, check this one
        print("There is no word.")
    elif len(word) == 1:
        print("I want a word not a letter")
    else:
        print(word, "is not a 3 letter word; try again.")
