def total_salary(path):
    try:
        total_sum = 0
        worker_count = 0

        with open(path, 'r', encoding='utf-8-sig') as fh:
            for line in fh:
                worker_count += 1
                name, salary = line.split(',')
                total_sum += int(salary)

        if worker_count == 0:
            return 0, 0 

        avg_salary = total_sum/worker_count
        return total_sum, avg_salary
        
    
    except FileNotFoundError:
        return ("Файл не знайдено")  
    except ValueError as e:
        return f"Помилка в рядку: {str(e)}"