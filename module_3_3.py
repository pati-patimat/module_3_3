def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(b = 25)
print_params(c = [1,2,3])

values_list = ['Hello', 123, [3, 4, 5]]
values_dict = {'a': [3, 4, 5], 'b': 'Hello', 'c': 123}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['абв', [5, 6, 7]]
print_params(*values_list_2, 42)