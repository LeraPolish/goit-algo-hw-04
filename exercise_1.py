def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if not lines:
                raise ValueError("Файл пустий")
            total_salary = 0
            num_developers = 0
            for line in lines:
                developer, salary = line.strip().split(',')
                total_salary += int(salary)
                num_developers += 1
            average_salary = total_salary // num_developers
            return total_salary, average_salary
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None, None
    except ValueError as ve:
        print(ve)
        return None, None
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return None, None

total, average = total_salary("salary_file.txt")
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
