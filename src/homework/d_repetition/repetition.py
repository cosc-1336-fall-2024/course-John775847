

def get_factorial(num):
    total = num
    for i in range(num-1):
        total = total * (i+1)
    return total

def sum_odd_numbers(num):
    if (num%2 != 0):
        total = num
    else:
        total = num-1

    for i in range(num-1):
        if (i%2 != 0):
            total += i
    return total
