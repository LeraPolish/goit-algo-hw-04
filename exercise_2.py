from pathlib import Path

def get_cats_info(path):
    cats_info = []
    try:
        with open(Path(path), 'r', encoding='utf-8') as file:
            for line in file:
                cat_data = line.strip().split(',')
                cat_dict = {"id": cat_data[0], "name": cat_data[1], "age": cat_data[2]}
                cats_info.append(cat_dict)
    except FileNotFoundError:
        print("Файл не знайдено.")
    except Exception as e:
        print("Сталася помилка під час обробки файлу:", e)
    return cats_info

cats_info = get_cats_info("cats.txt")
print(cats_info)
