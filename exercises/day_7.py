my_dict=dict()

def character_counter(char):
    for key in char:
        if key in my_dict:
            print(my_dict.get(key), "get")
            my_dict[key] = my_dict.get(key) +1
            print(my_dict.get(key), "updat4e")
        else:
            my_dict[key]= 1        
    return my_dict


char = input("Provice one frase:")

print("Número de caracteres: " , character_counter(char))