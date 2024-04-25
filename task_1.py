def total_salary(path: str) -> tuple:
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total = 0
            persons = 0
            for line in file:
                personal_salary = int(line.split(",")[1])
                total += personal_salary
                persons += 1
            average = int(total) / persons
            return (total, int(average)) 

    except Exception as e:
        return ('0', 'unavailable')


total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")