def get_cats_info(path):
    result_list = []

    try:
        with open(path, 'r', encoding='utf-8-sig') as fh:
            for line in fh:
                fields = line.split(',')
                if len(fields) == 3: 
                    cat_info = {'id': fields[0], 'name': fields[1], 'age': fields[2]}
                    result_list.append(cat_info)
        return result_list


    except FileNotFoundError:
        return ("Файл не знайдено")
    except ValueError as e:
        return f"Помилка в рядку: {str(e)}"
            