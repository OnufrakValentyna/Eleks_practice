def find_exit(matrix, start):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
    current_direction = (0, 1)  
    x, y = start

    while True:
        if not (0 <= x < len(matrix) and 0 <= y < len(matrix[0])):
            return "Куля вилетіла за межі поля"
        cell = matrix[x][y]

        if cell == '.':
            x += current_direction[0]
            y += current_direction[1]
        elif cell == '/':
            if current_direction == (0, 1):  
                current_direction = (-1, 0) 
            elif current_direction == (1, 0):  
                current_direction = (0, -1)  
            elif current_direction == (0, -1):  
                current_direction = (1, 0) 
            elif current_direction == (-1, 0): 
                current_direction = (0, 1)  
            x += current_direction[0]
            y += current_direction[1]
        elif cell == '\\':
            if current_direction == (0, 1):  
                current_direction = (1, 0) 
            elif current_direction == (1, 0): 
                current_direction = (0, 1)  
            elif current_direction == (0, -1):  
                current_direction = (-1, 0)  
            elif current_direction == (-1, 0): 
                current_direction = (0, -1) 
            x += current_direction[0]
            y += current_direction[1]
        elif cell == '|':
            current_direction = (-current_direction[0], current_direction[1]) 
            x += current_direction[0]
            y += current_direction[1]
        elif cell == '_':
            current_direction = (current_direction[0], -current_direction[1])  
            x += current_direction[0]
            y += current_direction[1]

        if (x, y) == start:  
            return "Куля застрягла у циклі"


# Приклад використання:
N = int(input("Введіть розмір матриці: "))
start = tuple(map(int, input("Введіть координати точки входу: ").split()))

matrix = []
print("Введіть матрицю-поле:")
for _ in range(N):
    row = input().split()
    matrix.append(row)

exit_point = find_exit(matrix, start)
print("Координати точки виходу:", exit_point)
