n = [3, 5, 7]

# Existing loop: doubles n once.
for i in range(len(n)):
    n[i] = n[i] * 2


def double_list(x):
    for i in range(len(x)):
        x[i] = x[i] * 2

    return x


print(double_list(n))