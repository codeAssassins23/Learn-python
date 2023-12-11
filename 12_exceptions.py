### Exception Handling ###

numberOne = 4
numberTwo = 2

print(numberOne + numberTwo)
numberOne = "1"

#Criterio de aceptación
if type(numberOne) == int:
    print(numberOne + numberTwo)
else:
    print("No se cumple la condición")

#Try - Except: exception handling
numberThree = "3"
numberFour = 4
numberThree = 2
try:
    print(numberThree + numberFour)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")

#Try - Except - Else:
try:
    print(numberThree + numberFour)
    print("success")
except:
    print("Se ha producido un error")
else:
    #This code will be executed if there is no error
    print("La ejecución ha sido correcta")

#Try - Except - Else - Finally:
try:
    print(numberOne+numberTwo)
    print("success")
except:
    print("SE ha producido un error")
#optional -> else - finally
else:
    #This code will be excuted if there is no error
    print("La ejecución ha sido correcta")
finally:
    #This code will be executed always
    print("La ejecución Continua")

#Expetion handling with multiple types of errors

try:
    print(numberOne + numberTwo)
    print("success")
except NameError:
    print("Se ha producido un error de nombre")
except ValueError:
    print("Se ha producido un error de valor")
except TypeError:
    print("Se ha producido un error de tipo de dato")

print("################################")

#catching all errors
try:
    print(numberOne + numberTwo)
    print("success")
except ValueError as e:
    print(e)
except Exception as error:
    print(error)