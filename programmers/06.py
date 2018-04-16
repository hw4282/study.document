def number_generator(x,n):
    return [x * i + x for i in range(1,n+1)]

print(number_generator(3,5))