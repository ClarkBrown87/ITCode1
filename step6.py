def short_fio(user_str):
    words = user_str.split()
    if len(words) == 3:
        new_fio = words[0] + ' ' + words[1][0] + '. ' + words[2][0] + '.'
        return new_fio


user_str = str(input("Введите ФИО полностью: "))
print(short_fio(user_str))