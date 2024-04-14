def my_replace(our_str):
    our_str = str(our_str)
    return our_str[0] + our_str[1:-1].replace('h', 'H') + our_str[-1]


user_str = input(str("Введите строку: "))
print(my_replace(user_str))
