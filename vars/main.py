name = "minispiki"  # < That's a string

# Or is it?
# Let's confirm
print("The name variable is a", type(name))
# For safety reasons, i wont use + for strings
# Upon running, im right! if i had used +
# program would go kaboom!
# To fix this
print("The name variable is a " + str(type(name)))
# ^ convert the type to string

email = "140969853+minispiki@users.noreply.github.com"  # valid email, just using it as an example, you will find this in my commits

info = ("Name: " + name + " email: " + email)  # The commas will automatically give me a space, lets use + for now tho
# My formatter keeps doing stuff. Had to disable it

# print that out
print(info)

number = 584
print(type(number)) # Is that an interger? (It is)

age = input("How old are you? ")
age = int(age) # Age is by default set to a string because of the imput function so i use typecasting
print("You are", age) # It wouldn't matter here but when doing arithmetic, it will

a = 5
a = float(a)
print (a) # Int to float should work fine but

a = 19.99
a = int(a)
print(a) # Python will truncate the decimals
