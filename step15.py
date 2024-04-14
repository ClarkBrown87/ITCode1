steps = int(input("Количество ступеней: "))

for i in range(1, steps+1):
    print('X' + 'x' * (i * 2 - 2) + 'X')
