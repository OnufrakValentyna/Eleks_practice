import math

def find_larger_angle_segment(x1, y1, x2, y2):

    angle_a = math.atan2(y1, x1) * (180 / math.pi)
    angle_b = math.atan2(y2, x2) * (180 / math.pi)
    
    if angle_a > angle_b:
        return "Відрізок OA утворює більший кут з віссю Ox."
    elif angle_b > angle_a:
        return "Відрізок OB утворює більший кут з віссю Ox."
    else:
        return "Відрізки OA та OB утворюють однаковий кут з віссю Ox."

x1 = float(input("Введіть координату x1: "))
y1 = float(input("Введіть координату y1: "))
x2 = float(input("Введіть координату x2: "))
y2 = float(input("Введіть координату y2: "))

result = find_larger_angle_segment(x1, y1, x2, y2)
print(result)
