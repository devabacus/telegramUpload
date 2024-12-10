import os

def create_file_list(directory):
    # Путь к файлу list_file.txt
    output_file = os.path.join(directory, 'list_file.txt')

    try:
        # Получаем список файлов в папке
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        
        # Записываем список файлов в list_file.txt
        with open(output_file, 'w') as file:
            for file_name in files:
                file.write(f"{file_name}\n")
        
        print(f"Файл 'list_file.txt' успешно создан в {directory}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Укажите путь к папке
folder_path = input("Введите путь к папке: ").strip()
create_file_list(folder_path)
