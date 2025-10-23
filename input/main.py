# sometimes , well , always, we cant just guess information nor can we use a config file values as simple as a name
# But, python, like c++'s cin and getline(cin, <varname>), has a function built in.
# Its called
input("Hello! ") # Won't be saved
name = input("What's your name? " ) # Stored by string, proven by
# type(name)

print("Welcome,", name, "!") # , does the job but i can use +
# input() # you dont need text in input

print("Now, are YOU the chosen one?")
t = input() # Need a temp var

if t == "yes":
    if name == "minispiki":
        print("no")
    else:
        print("You're not special.")
elif t == "no":
    print("Have some faith in yourself.")

# math tim
money = float(input("How much money do you have? "))
print("You have ", money)
