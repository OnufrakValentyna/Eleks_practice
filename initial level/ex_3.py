def calculate_pascal_row(n):

    if n == 0:
        return [1]

    previous_row = [1]
    current_row = [1]

    for i in range(1, n + 1):
        for j in range(i + 1):
            if j == 0 or j == i:
                current_row.append(1)
            else:
                current_row.append(previous_row[j - 1] + previous_row[j])

        previous_row = current_row
        current_row = []

    return previous_row

def main():
    try:
        n = int(input("Введіть номер рядка трикутника Паскаля (індекс починається з 0): "))
        if n < 0:
            print("Номер рядка повинен бути невід'ємним числом.")
            return
        print(f"{n}-й рядок трикутника Паскаля: {calculate_pascal_row(n)}")
    except ValueError:
        print("Будь ласка, введіть ціле число.")

if __name__ == "__main__":
    main()
