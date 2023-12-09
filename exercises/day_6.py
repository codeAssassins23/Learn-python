def fibonacci(number):
    
    f1 = 0
    f2 = 1
    print(f"Secuence fibonacci of {number}:\nF0={f1}\nF1={f2}")
    for i in range(1, number, 1):
        f3 = f1 + f2
        f1 = f2
        f2 = f3
        print(f"F{i+1}={f3}")

number = int(input("Plis provide one number for secuence fibonacci: "))

fibonacci(number)
