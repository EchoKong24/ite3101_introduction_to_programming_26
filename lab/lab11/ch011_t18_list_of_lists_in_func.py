n = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def flatten(lists):
    results = []

    for sublist in lists:
        for number in sublist:
            results.append(number)

    return results


print(flatten(n))