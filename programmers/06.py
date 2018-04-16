def number_generator(x,n):
    a = []
    for i in range(x, x*(n+1), +x):
        a.append(i)
    return a

print(number_generator(3,5))