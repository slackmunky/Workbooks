lst = list(range(5))
lst2 = list(range(5, 10, 1))

print(lst)
print(lst2)

lst.extend(lst2)
print(lst)