def list_extender(lst):
    lst.append(9)
    return lst


n = [3, 5, 7]

print(list_extender(n))