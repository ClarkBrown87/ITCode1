def replace_words(our_str):
    words = our_str.split()
    if len(words) == 2:
        return words[1] + ' ' + words[0]
    else:
        print("Количество слов не 2")


user_str = input(str("Введите 2 слова: "))
print(replace_words(user_str))
