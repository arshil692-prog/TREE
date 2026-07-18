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
