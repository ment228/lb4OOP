numbers = [3, 7, 5]

while True:
    number = int(input('новое число: '))
    numbers.append(number)
    print('текущий список чисел:', numbers)
    for num in numbers:
        print(num ** 2, num ** 3, num ** 4)
    print()