def total_salary(path: str) -> tuple:
    """Calculates the total salary of all developers and returns the total and average wage.

    Args:
        path (str): The file path containing the developer salaries. Each line contains 
        a comma-separated value representing the developer's name (ignored in this function)
        and their salary.

    Returns:
        tuple: A tuple containing the total salary of all developers and the average wage.
        If an error occurs, it returns '0' as the total salary and 'unavailable' for the 
        average wage.
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total_payment = 0
            persons = 0
            for dev_payment in file:
                personal_wage = int(dev_payment.split(",")[1])
                total_payment += personal_wage
                persons += 1
            average_wage = int(total_payment) / persons
            return (total_payment, int(average_wage)) 

    except Exception as e:
        return ('0', 'unavailable')


# Test run
total, average = total_salary("task_1/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

total, average = total_salary("task_1/salary_file_1.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

total, average = total_salary("task_1/salary_file_2.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
