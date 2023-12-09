number = int(input("Plis provide one number: "))
print(type(number))

#first exercise
def sum_number(number, count = 0,new_sum = 0):

    count += 2
    new_sum = new_sum + count

    if count > number:
        return (new_sum - count)

    else:
        return sum_number(number,count, new_sum)

result = sum_number(number)

print(result)


#the same exercise with for loop

def sum_number2(number):
    new_sum=0
    for i in range(0, number+1, 2):
        new_sum += i
    return new_sum

result2 = sum_number2(number)

print(f"La suma de klos numeros pares son: {result2}")