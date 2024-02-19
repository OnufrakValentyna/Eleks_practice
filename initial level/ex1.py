def main():
    n = int(input("Вкажіть кількість масивів: "))

    arrays = []

    for i in range(n):
        length = int(input(f"Довжина {i + 1}-го масиву: "))

        array = []
        for j in range(length):
            number = int(input(f"{j + 1}-й елемент {i + 1}-го масиву: "))
            array.append(number)

        arrays.append(array)

    merged_array = []
    for array in arrays:
        merged_array.extend(array)

    merged_array = sorted(set(merged_array) - {i for i in merged_array if i % 5 == 0})

    print("Об'єднаний та відсортований масив:", merged_array)

if __name__ == "__main__":
    main()
