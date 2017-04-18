print "Hello World!"
print "Hello, World!", "Again"

# print """Three double quotes
# ignores the new lines until
# it sees three more double quotes."""

# Variables - string, number, letters, or any other stuff you can make with a keyboard
# and you want to stash something that's not fast, into something that is fast
# There is no declaration.
#In JS... var name = "Shane";
#In Python... name = "Rob"

# the_meaning_of_life = 40 + 2
# print the_meaning_of_life
# print the_meaning_of_life / 2

first_name = "Rob"
last_name = "Bunch"
print "Hello, {} {}".format(first_name, last_name)
print "Hello, %s %s" % (first_name, last_name)

# Floats
pi_the_magic_float = 3.14
print pi_the_magic_float
print type(pi_the_magic_float)
make_me_an_interger = int(pi_the_magic_float)
print make_me_an_interger

# Raw Input
first_name = raw_input("First Name: ")
last_name = raw_input("Last Name: ")

# Conditionals
# 1 = means you want to assign something
# 2 == means you want to compare the thing on the left witht the thing on the right

if(first_name == last_name):
	print "Your first name is the same as your last name?"

age = raw_input("How old are you?")
age_as_int = int(age)
print type(age)
if(age >= 21):
	print "You can buy beer"