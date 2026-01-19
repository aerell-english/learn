# Learn English day 1 using python

# I / You / We
# Is / are / do
# Focus verb: print, get, set, check

# I print "Hello World" to the console
print("Hello World")
# the output like this:
# Hello World

# I set a variable name with my name
name = "Fern Aerell"

# I print my name in variable like printed hello world before
print(name)
# Now the output like this:
# Hello World
# Fern Aerell

# You can get my name in variable name like this
name # This does not display anything because it is not inside the print function
# Note: in python if just expression it not show, but if in REPL or Jupyter it can show.

# You must put the variable into function print argument, like this:
print(name)
# The output updated like this:
# Hello World
# Fern Aerell
# Fern Aerell

# We have printed my name 2 times, you can see in console.

# We can put my name in another variable
name2 = name

# Now name2 is my name too, we check:
print(name2)
# The output:
# Hello World
# Fern Aerell
# Fern Aerell
# Fern Aerell

# If you feel this less clarity, you can add some string before argument name2 in print function, but don't forget about coma , for sparator
print("this is from name 2 variable:", name2)
# The output like this now:
# Hello World
# Fern Aerell
# Fern Aerell
# Fern Aerell
# this is from name 2 variable: Fern Aerell

# We check again, and see the different.

# Now we have printed my name  4 times.

# Let's do something different
# We add name to with name2 as print function argument
print(name + name2)
# Let see!
# The output like this:
# Hello World
# Fern Aerell
# Fern Aerell
# Fern Aerell
# this is from name 2 variable: Fern Aerell
# Fern AerellFern Aerell

# You can make the code above more readable just change +  to + " " +
print(name + " " + name2)
# Output:
# Fern Aerell Fern Aerell

# I think on python we can do this:
print(name*10)
# The output:
# Hello World
# Fern Aerell
# Fern Aerell
# Fern Aerell
# this is from name 2 variable: Fern Aerell
# Fern AerellFern Aerell
# Fern AerellFern AerellFern AerellFern AerellFern AerellFern AerellFern AerellFern AerellFern AerellFern Aerell

# Haha it's cool
# I found this feature in python, i don't know about another language, but I first found this feature in python.

# Okay, I think this enough.
# Thank you.
