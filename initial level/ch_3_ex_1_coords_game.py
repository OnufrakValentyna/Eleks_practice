from datetime import datetime

def max_people(events):
    events.sort(key=lambda x: x[3], reverse=True)  
    total_people = 0
    end_time = datetime.strptime(events[0][1], '%H:%M')  # Час завершення першої події
    for event in events:
        start, end, travel_time, people = event
        start_time = datetime.strptime(start, '%H:%M')
        if start_time >= end_time:  # Якщо поточна подія починається після закінчення попередньої
            total_people += people
            end_time = datetime.strptime(end, '%H:%M')
        elif datetime.strptime(end, '%H:%M') <= end_time:  # Якщо поточна подія закінчується раніше, ніж попередня
            continue
        else:  
            overlap_time = (end_time - start_time).total_seconds() / 1800  # Тривалість перекриття у напівгодинах
            total_people += overlap_time * people  # Додаємо пропорційну кількість учасників
            end_time = datetime.strptime(end, '%H:%M')
    return total_people

if __name__ == "__main__":
    wake_up_time = input("Час коли підліток проснувся (hh:mm): ")
    n = int(input("Кількість подій: "))
    events = []
    for _ in range(n):
        start, end, travel_time, people = input().split()
        events.append((start, end, travel_time, int(people)))
    
    print("Максимальна кількість людей, яких може зустріти підліток:", max_people(events))
