# Representing strings
H1 = "Hello World!"  # print hello world
print(H1)

H2 = "Hello World!"  # print hello world
print(H2)

# Quotes usage
print("It's the day")  # double quotes
print('She said "Hello" to everyone')  # single quotes
print(
    """
    Hello
        World
    """
)  # triple quotes for multiline string support

# string type
myvariable = "Bob"
print(type(myvariable))  # print myvariable item type

# string operations and functions
# string concatenation
string1 = "Good "
string2 = "Day"
string3 = string1 + string2
print(string3)

print("Hello " + "World!")

# length of a string
print(len(string3))  # finds the length(no. of characters contained in the string)

# Accessing a character
mystring = "Hello World"
print(mystring[4])  # fourth index item value(o); zero indexed.
print(mystring[8])  # eighth item value(r);zero indexed

# Accessing subset of characters
my_string = "Hello World"
print(my_string[0:3])  # print zero to third index item values
print(my_string[:5])  # print from zero to fifth index item value
print(my_string[2:])  # print from second index item value to the nth index item value

# Repeating strings
print("*" * 10)  # multiplies asterisk times ten.
print("Hi" * 10)  # multiplies Hi ten times

# Splitting Strings- using the split() method
title = "The Good, The bad, and the Ugly"
print("Source string: ", title)
print("Print using space")
print(title.split(" "))  # splits the title using the spaces in the sentence
print("Print using commas")
print(title.split(","))  # splits the title using the commas in the sentence

# Counting strings
my_count = "counts the number of counts in this counts string that counts counts"
print(
    "My count is: ", my_count.count("count")
)  # Count the sub-string 'counts' in the string 'my_count'
