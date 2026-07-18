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
