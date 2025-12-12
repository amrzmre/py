
# 1. String Creation and Basics:

single_quote = 'Hello, World!'         # single quotes (one liner)
double_quote = "Hello, World!"         # double quotes (one liner)
triple_single_quote = """Multi-line
string"""                              # triple single quotes (multi-line string)


# 2. string indexing and slicing:

""" indexing: number(position) of each character in a string.
    slicing: extracting: grabbing multiple charaters [start:stop:step] """

text = "Python Programming"

print(text[0])       # (first character 'P' is at index 0, so index 1 is ' ')
print(text[-1])       # last character
print(text[0:4])      # slicing from index 1 to 5
print(text[:6])       # slicing from start to index 6
print(text[7:])       # slicing from index 7 to end


# 3. string methods:

name = "  Alice  "

print(len(name))                # length of the string
print(name.strip())             # remove whitespace from both ends
print(name.upper())             # convert to uppercase
print(name.lower())             # convert to lowercase
print(name.title())             # convert to title case
print(name.replace("A", "E"))   # replace 'A' with 'E'


# 4. String formatting:

name = "Bob"
age = 30

message_1 = f"My name is {name} and I am {age} years old."          # f-strings
message_2 = "My name is {} and I am {} years old".format(name, age) # str.format()
message_3 = "My name is %s and I am %d years old." % (name, age)    # %-formatting 

print(message_1)
print(message_2)    
print(message_3)    

# EXERCISES:

"""
1. build a simple text analyzer that counts the words, characters,
   and sentences in a given text."""


text = """Python is a powerful programming language. It's easy to learn 
and versatile!
You can use Python for web development, data science, and automation.
The syntax is vvclean and readable.
This make Python perfert for beginners and experts alike."""

print(len(text))                      # count characters
print(len(text.split()))              # count words
print(text.count("."))                # count sentences