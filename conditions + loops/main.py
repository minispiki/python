while True: # Loop forever
    word = input("Give me a 3 letter word ") # str
    if len(word) == 3: # is word's length 3 letters?
        print("You did it, you gave me a 3 letter word!")
        break # exit
    else:
        print(word, "is not a 3 letter word; try again.")
