import os

# Функция для извлечения текста из бинарного файла и записи в текстовый файл
def extract_and_save_text(bin_file, txt_file, fraction=1):
    try:
        file_size = os.path.getsize(bin_file)  # Получаем размер файла
        bytes_to_read = int(file_size * fraction)  # Вычисляем, сколько байт нужно прочитать
        
        with open(bin_file, "rb") as bin_f, open(txt_file, "w", encoding="utf-8") as txt_f:
            bytes_read = 0
            while bytes_read < bytes_to_read:
                byte = bin_f.read(1)
                if not byte:
                    break
                bytes_read += 1
                if 32 <= ord(byte) <= 126:  # Печатные ASCII-символы
                    txt_f.write(byte.decode("ascii"))
                elif byte == b'\x00':  # Нулевой байт (разделитель)
                    txt_f.write(" ")
        
        print(f"Текст успешно извлечён и сохранён в файл {txt_file}.")
    except Exception as e:
        print(f"Ошибка при обработке файла {bin_file}: {e}")

# Основной код
if __name__ == "__main__":
    # Пути к исходным бинарным файлам
    input_files = [
        "C:/00Projects/Pet_project_A_Sh/dataset/cnn-dailymail/finished_files/train.bin",
        "C:/00Projects/Pet_project_A_Sh/dataset/cnn-dailymail/finished_files/val.bin",
        "C:/00Projects/Pet_project_A_Sh/dataset/cnn-dailymail/finished_files/test.bin"
    ]

    # Пути к выходным текстовым файлам
    output_files = [
        "train_text.txt",
        "val_text.txt",
        "test_text.txt"
    ]

    # Обработка всех файлов
    for input_file, output_file in zip(input_files, output_files):
        print(f"Обработка файла {input_file}...")
        
        # Извлечение текста и запись в текстовый файл (только первые 10%)
        extract_and_save_text(input_file, output_file, fraction=1)