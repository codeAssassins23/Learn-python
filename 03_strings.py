"""
name, surname, age = "victor", "bravo", 35

print(f"hola mi nombre es: {name} {surname} y tengo {age} años")

print("hola mi nombre es {} {} y tengo {} años".format(name, surname, age))

print("hola mi nombre es %s %s y tengo %d años" % (name, surname, age))

string = "hola"
string2 = "nombre "
print(len(string))
print(len(string2))
print(string + " uwu " + string2)

my_line_string = "This is a string \n with lean break"

my_tab_string = "\t this si a string with tabulación"

print(my_line_string)
print(my_tab_string)
"""
# multiline string
multiline_string = """This a string create with 
multiline break"""
multiline_string2 = """A second type of 
multiline break"""

print(multiline_string)
print(multiline_string2)

"""
The most common escape characters:
\n
\t
\\
\'
\''
examples:
"""
print("I have a new idea.\nAre you?")
print("\tone\ttwo\tthree")
print("Day 1\t5\t5")
print("this is a backslash symbol (\\)")
print('In every programming language it start whit"Hello world!"')

first_name = "victor hugo"
last_name = "bravo"
language = "python"
formated_string = "I am %s %s. I learn %s" % (first_name, last_name, language)
print(formated_string)
""""""
python_libraries = ["django", "flask", "Numpy", "Matplotlib", "pandas"]
formated_string2 = "The following are python libraries:%s" % (python_libraries)
print(formated_string2)

language = "python"
letter1 = language[-1]
letter2 = language[-2]
letter3 = language[-3]
letter4 = language[-4]
letter5 = language[-5]
letter6 = language[0]

print(letter1, letter2, letter3, letter4, letter5, letter6)
########################

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

#reverse

reversed_language = language[::-1]
print(reversed_language)

#function 

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.format())
print(language.isnumeric())
print(language.lower().isupper())
print(language.startswith("py"))

