### Dictionaries ###

my_dict = dict()
print(type(my_dict))

my_other_dict = {}
print(type(my_other_dict))

my_other_dict = {'name': 'jhon','apellidos':'bravo', 'edad': 21, 1:'python', 2: 'javascript'}
print(my_other_dict)

list_skills = ['javascript', 'python', 'nodejs']
my_dict = {
    'name': 'jhon',
    'apellidos':'bravo',
    'edad': 21,
    1:'python',
    2: 'javascript',
    'skills': list_skills,
    'address': {
        'street': '50',
        'number': '30',
        'zip': '12345'
    }
}
print(my_dict)
#len
print(len(my_other_dict))
print(len(my_dict))

#access one element
skills = my_dict['skills']
print(skills)

python = my_dict[1]
print(python)

#access one element with get, the difference is that if the key doesn't exist, it doesn't generate an error
skills = my_dict.get('uwu')
print(skills)

#add new element
my_dict['uwu'] = 'owo'
print(my_dict)

#copy
my_copy_dict = my_dict.copy()
print(my_copy_dict,"copy")

#update
my_dict['uwu'] = 'uwu'
my_dict.update({'uwu': 'uwu'})#the difference is that it can add more than one element

print("\n",my_dict)

#delete
del my_dict['uwu']
print(my_dict)

#search
print('name' in my_dict)

print(my_other_dict.items())

#keys
my_keys = my_other_dict.keys()
print(my_keys)

#values
values_dict = my_other_dict.values()
print(values_dict)

#fromkeys
my_from_key = dict.fromkeys(['name','apellidos','edad','skills'])
print(my_dict)
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)
""" #delete all
my_dict.clear()
print(my_dict, "clear")
 """