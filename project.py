

row = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):

    for j in range(1, rows + 1):
        if j less than or equal to rows - i:
            print(' ', end = ' ')
        else:
            print('*', end= '')
    print()