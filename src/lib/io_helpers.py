"""
Вспомогательные функции для ввода-вывода
"""

import os

def ensure_directory(file_path):
    """Создает директорию для файла если она не существует"""
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

def read_text_file(file_path):
    """Чтение текстового файла"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()