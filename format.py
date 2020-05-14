# Value conversion
Number1 = "One"
Number2 = "Two"

Sentence2 = f"First two numbers are {Number1} {Number2}"  # Simple positional formatting
print(Sentence2)

# Aligning
test = "test"
Sentence2 = f"{test:>10}"  # Align left
print(Sentence2)

test2 = "test2"
sentence3 = f"{test2:_<10}"  # Align right
print(sentence3)

test3 = "test3"
sentence4 = f"{test3:^10}"  # Align centre
print(sentence4)

# Truncating
xylophone = "xylophone"
sentence5 = (
    f"{xylophone:.5}"  # number after . specifies precision length. Trancation length.
)
print(sentence5)

# Truncating and padding
Xylophone2 = "xylophone"
sentence6 = f"{Xylophone2:10.5}"  # Trauncating at 5 and padded 10
print(sentence6)

# Simple number value conversion
num1 = 42
number1 = f"{num1:d}"  # integers
print(number1)

pi = 3.141592653589793
number2 = f"{pi:f}"  # floats
print(number2)

# padding numbers
num3 = 42
number3 = f"{num3:4d}"
print(number3)

# padding and truncating numbers
pi2 = 3.141592653589793
number4 = f"{pi2:06.2f}"  # six characters with two decimal points
print(number4)

# signed numbers
num4 = 42
number5 = f"{num4:+d}"  # positive integer
print(number5)

num5 = -42
number6 = f"{num5: d}"  # negative integer
print(number6)
