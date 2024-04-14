def unique_numbers(our_str):
    for i in our_str:
        if i.isdecimal() and our_str.count(i) == 1:
            continue
        else:
            return False
    return True

user_str = str(input("Введите строку: "))
if unique_numbers(user_str):
    print("Все числа в строке уникальны")
else:
    print("В строке есть не уникальные числа")