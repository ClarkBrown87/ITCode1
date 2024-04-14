def print_peoples(my_set):
    for i in my_set:
        print(i, end=" ")
    print()

students = {'Schultz', 'Django', 'Brunhilde', 'Fritz'}
employees = {'Schultz', 'Django', 'Calvin', 'Butch', 'Fritz'}

all_people = students | employees
st_emp = students & employees
only_emp = employees - students
only_st = students - employees
only = only_emp | only_st

print("Все люди: ", end='')
print_peoples(all_people)

print("одновременно учится и работает: ", end='')
print_peoples(st_emp)

print("только работает, но не учится: ", end='')
print_peoples(only_emp)

print("либо учится, либо работает, но не одновременно: ", end='')
print_peoples(only)

