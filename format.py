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
