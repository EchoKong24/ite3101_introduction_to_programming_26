def my_function(x):
    result = []

    for i in range(len(x)):
        result.append(x[i])

    return result


print(my_function(range(3)))