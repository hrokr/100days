# Practice with Printing in Python

# The obligatory
print('Hello World')

# With concatenation
print('Hello' + ' ' + 'World')

# Multiplication of a word
print('very ' * 5)

# Adding newlines & tabs
print("Ew\n\tWhat do you mean 'Ew'? I don't like spam.")

# Printing with arithmetic
print ( 1 + 1 )

# But can you combine strings and integers in the same print statement?
# (Yes, but only because the int is getting cast as a string)
print("The answer to life, the Universe, and everything is: " + str(42))

# Or we can do it with the newer f-strings
ans = 42
print(f"The answer to life, the Universe, and everything is (reportedly) {ans}")

# Or the legacy version
print ("The number of the {} shall be {}. No more; no less" .format("counting", 3))

# One thing new was that you can just go with a {} for an f-string with assignation
print(f"The answer to life, the Universe, and everything is (reportedly) {42}.")

# A reminder is that you can positionally index the contents inside the brackets
print("The number of the {1} shall be {0}. No more; no less.".format(3, 'counting'))



