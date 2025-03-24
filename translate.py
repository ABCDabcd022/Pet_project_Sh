from deep_translator import GoogleTranslator

def get_all_sentences(file_path, max_sentences=None):
    """Извлекает все предложения из файла, разделённые точками."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()  # Читаем весь файл
            sentences = text.split('.')  # Разделяем текст по точкам
            sentences = [s.strip() for s in sentences if s.strip()]  # Убираем пустые строки
            if max_sentences:
                sentences = sentences[:max_sentences]  # Ограничиваем количество предложений
            return sentences
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return []
    except Exception as e:
        print(f"Ошибка при чтении файла {file_path}: {e}")
        return []

def translate_text(text, source='en', target='ru'):
    """Переводит текст с помощью GoogleTranslator."""
    try:
        translated = GoogleTranslator(source=source, target=target).translate(text)
        return translated
    except Exception as e:
        print(f"Ошибка при переводе текста: {e}")
        return text  # Возвращаем оригинальный текст в случае ошибки

def save_translation(file_path, translated_sentences):
    """Сохраняет переведённые предложения в новый файл."""
    try:
        # Создаем имя для нового файла
        new_file_path = file_path.replace('.txt', '_ru.txt')
        with open(new_file_path, 'w', encoding='utf-8') as new_file:
            for sentence in translated_sentences:
                new_file.write(sentence + '.\n')  # Добавляем точку и перенос строки
        print(f"Перевод сохранён в файл: {new_file_path}")
    except Exception as e:
        print(f"Ошибка при сохранении перевода в файл {file_path}: {e}")

# Файлы для обработки и ограничения на количество предложений
files = {
    'train_text.txt': 30000,  # Ограничение для train
    'val_text.txt': 1365,     # Ограничение для val
    'test_text.txt': 1180     # Ограничение для test
}

# Переводим предложения из каждого файла с ограничением
for file, max_sentences in files.items():
    sentences = get_all_sentences(file, max_sentences)
    if not sentences:
        continue  # Пропускаем файл, если не удалось извлечь предложения

    translated_sentences = []
    for i, sentence in enumerate(sentences):
        translated = translate_text(sentence)
        translated_sentences.append(translated)

        # Выводим число после каждых 100 переведённых предложений
        if (i + 1) % 100 == 0:
            print(f"Файл: {file}, переведено предложений: {i + 1}")

    # Сохраняем перевод в новый файл
    save_translation(file, translated_sentences)