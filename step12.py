user_str = input(str())
new_str = user_str.replace(" ", "")
if new_str[-1] == ',':
    new_str = new_str[:-1]

my_list = list(map(int, new_str.split(',')))
my_tuple = tuple(map(int, new_str.split(',')))

print(my_list, my_tuple, sep='\n')
