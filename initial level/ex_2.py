def reverse_words(input_file, output_file):
    try:
        # Відкриття вхідного файлу для читання
        with open(input_file, 'r') as f:
            # Читання тексту з файлу
            text = f.read()
        
        # Розділення тексту на слова
        words = text.split()

        # Перевертання кожного слова
        reversed_words = [word[::-1] for word in words]

        # Відкриття вихідного файлу для запису
        with open(output_file, 'w') as f:
            # Запис перевернутих слів у файл
            f.write(' '.join(reversed_words))

        print("Слова було успішно записано у файл '{}' у зворотньому порядку.".format(output_file))
    except FileNotFoundError:
        print("Помилка: Файл '{}' не знайдено.".format(input_file))
    except Exception as e:
        print("Під час виконання програми виникла помилка:", e)

# Приклад використання
if __name__ == "__main__":
    input_file = input("Введіть шлях до вхідного файлу: ")
    output_file = input("Введіть шлях до вихідного файлу: ")
    reverse_words(input_file, output_file)
