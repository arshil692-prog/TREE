# ============================
# 1. Creating Strings
# ============================

s1 = "Hello"
s2 = 'Python'
s3 = """Welcome
to
Python"""

print(s1)
print(s2)
print(s3)

# ============================
# 2. Indexing
# ============================

text = "Programming"

print(text[0])      # P
print(text[3])      # g
print(text[-1])     # g
print(text[-2])     # n

# ============================
# 3. Slicing
# ============================

print(text[0:6])    # Progra
print(text[3:7])    # gram
print(text[:5])     # Progr
print(text[4:])     # ramming
print(text[:])      # Programming
print(text[::2])    # Pormig
print(text[::-1])   # gnimmargorP

# ============================
# 4. String Length
# ============================

print(len(text))

# ============================
# 5. Case Conversion Methods
# ============================

name = "python programming"

print(name.upper())
print(name.lower())
print(name.title())
print(name.capitalize())
print(name.swapcase())

# ============================
# 6. Searching Methods
# ============================

sentence = "Python Programming"

print(sentence.find("P"))
print(sentence.find("Java"))
print(sentence.rfind("P"))
print(sentence.index("Programming"))
print(sentence.count("m"))

# ============================
# 7. Checking Start & End
# ============================

filename = "notes.pdf"

print(filename.startswith("notes"))
print(filename.endswith(".pdf"))

# ============================
# 8. Replace Method
# ============================

text = "I like Java"

print(text.replace("Java", "Python"))

# ============================
# 9. Strip Methods
# ============================

name = "   Arshil   "

print(name.strip())
print(name.lstrip())
print(name.rstrip())

# ============================
# 10. Split Method
# ============================

fruits = "Apple Mango Banana"

print(fruits.split())

data = "Red,Green,Blue"

print(data.split(","))

# ============================
# 11. Join Method
# ============================

words = ["Python", "is", "easy"]

print(" ".join(words))
print("-".join(words))
print(",".join(words))

# ============================
# 12. Validation Methods
# ============================

print("Python".isalpha())
print("12345".isdigit())
print("Python123".isalnum())
print("python".islower())
print("PYTHON".isupper())
print("   ".isspace())
print("Hello World".istitle())
print("student_name".isidentifier())
print("Python".isascii())

# ============================
# 13. Membership Operators
# ============================

text = "Python Programming"

print("Python" in text)
print("Java" in text)

print("Java" not in text)

# ============================
# 14. String Comparison
# ============================

print("Apple" == "Apple")
print("Apple" != "Mango")
print("Apple" < "Banana")
print("Zoo" > "Apple")

# ============================
# 15. Escape Characters
# ============================

print("Hello\nWorld")
print("Python\tProgramming")
print("C:\\Users\\Arshil")
print("It\'s Python")
print("He said \"Hello\"")
print("ABC\bD")
print("Hello\rHi")

# ============================
# 16. String Formatting
# ============================

name = "Arshil"
age = 22

print("My name is", name)

print("My name is {} and age is {}".format(name, age))

print(f"My name is {name} and age is {age}")

print("Age = %d" % age)

# ============================
# 17. Concatenation
# ============================

first = "Hello"
second = "World"

print(first + " " + second)

# ============================
# 18. Repetition
# ============================

print("*" * 10)
print("Hi " * 5)

# ============================
# 19. Looping Through String
# ============================

word = "Python"

for ch in word:
    print(ch)

# ============================
# 20. Enumerate
# ============================

for index, ch in enumerate(word):
    print(index, ch)


# ============================
# 21. Reverse String
# ============================

print(word[::-1])

# ============================
# 22. Count Vowels
# ============================

text = "Programming"

count = 0

for ch in text.lower():
    if ch in "aeiou":
        count += 1

print(count)

# ============================
# 23. Palindrome Check
# ============================

word = "madam"

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# ============================
# 24. Remove Spaces
# ============================

text = "Python Programming"

print(text.replace(" ", ""))

# ============================
# 25. Reverse Words
# ============================

sentence = "I Love Python"

words = sentence.split()

print(words[::-1])

print(" ".join(words[::-1]))

# ============================
# 26. Find Maximum Character
# ============================

text = "python"

print(max(text))
print(min(text))

# ============================
# 27. ASCII Conversion
# ============================

print(ord("A"))
print(chr(65))

# ============================
# 28. String Immutability
# ============================

name = "Python"

# name[0] = "J"   # TypeError

name = "Jython"

print(name)

# ============================
# 29. Remove Duplicate Characters
# ============================

text = "programming"

result = ""

for ch in text:
    if ch not in result:
        result += ch

print(result)

# ============================
# 30. List Comprehension with String
# ============================

word = "python"

upper = [ch.upper() for ch in word]

print(upper)