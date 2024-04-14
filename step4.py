def find_word(our_str):
    word = False
    count_word = 0
    for char in our_str:
        if char == ' ':
            if word:
                count_word += 1
                word = False
                continue
            continue
        else:
            word = True

    if word: count_word += 1

    return count_word


user_str = str(input("Введите строку: "))
print(find_word(user_str))
