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

# Counting strings using the count() method
my_count = "counts the number of counts in this counts string that counts counts"
print(
    "My count is: ", my_count.count("count")
)  # Count the sub-string 'counts' in the string 'my_count'

# Replacing strings using the replace method()
welcome_message = "Hello World"
print(
    welcome_message.replace("Hello", "Goodbye")
)  # replaces old substring 'Hello' with new 'Goodbye'

# finding substrings in a string
print(
    "Peter akworo nomad".find("akworo")
)  # finds lowest index in the string where substring sub is found.
print(
    "Peter akworo nomad".find("John")
)  # Returns -1 if the substring is not found within the string

# Converting other types to string
print(type(80))  # type here is integer
msg = "Peter you will be " + str(
    80
)  # Making a string with an integer converted to string
print(msg)

# Comparing strings
print("Peter" == "Peter")  # true
print("Akworo" == "Peter")  # false
print("Akworo" != "Peter")  # true
print("peter" == "Peter")  # false;case sensitive

# Check on string properties.
# Check first character in a string
stringchar = "Hello Peter"
print("stringchar starts with H: ", stringchar.startswith("H"))  # evaluates to true
print("stringchar starts with h: ", stringchar.startswith("h"))  # evaluates to false

# Check last character in a string
stringchar = "Hello Peter"
print("stringchar ends with r: ", stringchar.endswith("r"))  # evaluates to true
print("stringchar ends with R: ", stringchar.endswith("R"))  # evaluates to false

# Check first letter of every sub-string is titled
stringchar = "Hello Peter"
print("stringchar is titled: ", stringchar.istitle())  # evaluates to true if titlecased
stringtitle = "hello peter"
print(
    "stringtitle is titled: ", stringtitle.istitle()
)  # evaluates to false if not titlecased

# Check every letter of every sub-string is uppercased
stringchar = "HELLO PETER"
print(
    "stringchar is uppercased: ", stringchar.isupper()
)  # evaluates to true if  uppercased
stringupper = "hello peter"
print(
    "stringupper is uppercased: ", stringupper.isupper()
)  # evaluates to false if not uppercased

# Check every letter of every sub-string is lowercased
stringchar = "hello peter"
print(
    "stringchar is lowercased: ", stringchar.islower()
)  # evaluates to true if  lowercased
stringlower = "HELLO PETER"
print(
    "stringlower is lowercased: ", stringlower.islower()
)  # evaluates to false if not lowercased

# Check is string contains alphabets
stringchar = "Peter"
print(
    "Stringchar is alphabetic: ", stringchar.isalpha()
)  # Return true if all characters in the string are alphabeti
stringnum = "12875"
print("is strinum alphabetic: ", stringnum.isalpha())  # false
stringalphanum = "Peter12875"
print("is stringalphanum alphabetic: ", stringalphanum.isalpha())  # false

# string properties conversions
# convert to uppercase
convertlower = "peter akworo"
print(
    convertlower.upper()
)  # return a copy of the string with all the cased characters converted to uppercase.

# convert to lowercase
convertupper = "PETER AKWORO"
print(
    convertupper.lower()
)  # return a copy of the string with all the cased characters converted to lowercase.

# swap cases
stringswap = "peter AKWORO"
print(
    stringswap.swapcase()
)  # Return a copy of the string with uppercase characters converted to lowercase and vice versa.

# strip leading and trailing space
stringtrail = "  peter akworo  "
print(
    stringtrail.strip()
)  # Return a copy of the string with the leading and trailing characters removed


##exercise
"""1. Explore replacing a string
Create a string with words separated by ',' and replace the commas with spaces;
for example replace all the commas in 'Denyse,Marie,Smith,21,London,UK'
with spaces. Now print out the resulting string.
"""

names = "Denyse,Marie,Smith,21,London,UK"
print(names.replace(",", " "))

"""2. Handle user input
The aim of this exercise is to write a program to ask the user for two strings and
concatenate them together, with a space between them and store them into a new
variable called new_string.
Next:
• Print out the value of new_string.
• Print out how long the contents of new_string is.
• Now convert the contents of new_string to all upper case.
• Now check to see if new_string contains the string 'Albus' as a substring
"""
value1 = input("Your first string: ")  # first input request
value2 = input("Your second string: ")  # second input request
new_string = value1 + " " + value2  # concatenate the two strings
print(new_string)  # print out the value of the new string
print(len(new_string))  # print out the length of the new vstring value
print(new_string.upper())  # convert the string value content all to uppercase
print(new_string.find("Albus"))  # if it contains Albus as a substring

num1 = 3.1463259
num2 = 10.290452

# print('num1 is', num1,' and num2 is', num2)
# print('num1 is {0} and num2 is {1}'.format(num1,num2))
# print('num1 is {0:.3} and num2 is {1:.3}'.format(num1,num2))
# print('num1 is {0:.3f} and num2 is {1:.3f}'.format(num1,num2))
# print(f'num1 is {num1} and num2 is {num2}')
# print(f'num1 is {num1:.3} and num2 is {num2:.3}')
print(f"num1 is {num1:.3f} and num2 is {num2:.3f}")

