
my_list = [1, 2, 3.25]

k = all([isinstance(item, float) | isinstance(item, int) for item in my_list])

# all(isinstance(item, int) for item in my_list)

print(k)