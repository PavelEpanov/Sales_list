def main():
    days = int(input("Введите количество дней продаж: "))

    index = 0

    sales = [0] * days

    while index < days:
        sales[index] = float(
            input(f"Введите сумму продаж: за {index + 1} день: "))
        index += 1

    print("Значения, которые вы ввели: ")

    for value in sales:
        print(value)


main()
