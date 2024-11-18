def pass_(n):
    unique = ''
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                unique += str(i) + str(j)
    return f'{n} - {unique}\n Поздравляю пароль верный'

n = int(input("Привет Indiana J. введи число : "))

indiana_jones = pass_(n)
print(indiana_jones)