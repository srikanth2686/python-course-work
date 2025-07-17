# 1. UPPERCASE
text="srikanth"
print(text.upper())  #SRIKANTH

#.2.LOWERCASE
text="SRIKANTH"
print(text.lower())  # output=srikanth


#.3.SWAPCASE
text="rajashekar is GOOD BOY"
print(text.swapcase())      #output=RAJASHEKAR IS good boy


#____________#example
str1 ="hello"                 #output=hello
str2 ="world"                         # world
str3 ="hii mawa"                      # hii mawa
print(str1)
print(str2)
print(str3)



# Concatenation
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)              # Output: Hello World

# Repetition
print("Python! " * 3)      # Output: Python! Python! Python!

# Indexing
text = "Python"
print(text[0])             # Output: P 
print(text[-1])            # Output: n 

# Slicing
print(text[0:3])           # Output: Pyt 
print(text[:4])            # Output: Pyth 
print(text[2:])        # Output: thon 


# Membership
print('Pyt' in text)       # Output: True
print('Java' not in text)  # Output: True


# 1. len()
text = "Hello World"
print(len(text))                # Output: 11

# 2. max() and min()
print(max("abcXYZ"))             # Output: 'c' 
print(min("abcXYZ"))             # Output: 'X' 

# 3. sorted()
print(sorted("python"))          # Output: ['h', 'n', 'o', 'p', 't',"y"]


# 4. chr() and ord()
print(ord('A'))                    # Output: 65 
print(chr(97))                     # Output: 'a' 
