def my_replace(our_str):
    first = our_str.find('h')
    last = our_str.rfind('h')
    if first > 0 < last: return our_str[0:first + 1] + our_str[first + 1:last].replace('h', 'H') + our_str[last:]


user_str = str(input("Введите строку: "))
print(my_replace(user_str))
