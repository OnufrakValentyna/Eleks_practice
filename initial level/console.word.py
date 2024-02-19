def count_word_occurrences(word, mode, file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            count = 0
            if mode == 1:
                count = text.lower().count(word.lower())
            elif mode == 2:
                words = text.split()
                for w in words:
                    if w.lower() == word.lower():
                        count += 1
            print(f"The word '{word}' occurs {count} times in the file.")
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")

if __name__ == "__main__":
    word = input("Enter the word to search for: ")
    mode = int(input("Enter the mode (1 for partial match, 2 for exact match): "))
    file_path = input("Enter the file path: ")
    count_word_occurrences(word, mode, file_path)
