def my_func(test):
    output = []
    for i in test:
        if i % 2 == 0:
            output.append(i)
    return output[::-1]

print(my_func([1, 48, 16, 2, 3, 97, 100, 15, 13]))

#completed