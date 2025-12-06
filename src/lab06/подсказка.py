Импорт модулей и настройка пути
python
import argparse
import sys
import argparse - импорт модуля для обработки аргументов командной строки

import sys - импорт системного модуля для работы с системными функциями

python
sys.path.append(r'C:\Users\Lucia\PycharmProjects\LabsOnishenko\src')
Добавляет путь к проекту в системный путь Python, чтобы можно было импортировать модули из этой директории

python
from lib.text import normalize, tokenize, count_freq, top_n
Импорт конкретных функций из пользовательского модуля lib.text:

normalize - нормализация текста

tokenize - разбиение на токены (слова)

count_freq - подсчет частоты слов

top_n - получение N самых частых слов

Вспомогательные функции
python
def read_text_file(file_path):
Объявление функции для чтения текстового файла

python
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
try - начало блока обработки исключений

with open(...) - открытие файла в режиме чтения с кодировкой UTF-8

return f.read() - чтение всего содержимого файла и возврат результата

python
    except FileNotFoundError:
        print(f"Ошибка: Файл {file_path} не найден")
        sys.exit(1)
Обработка исключения "файл не найден"

Вывод сообщения об ошибке и завершение программы с кодом 1 (ошибка)

python
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        sys.exit(1)
Обработка любых других исключений при чтении файла

Команда CAT
python
def cat_command(args):
Функция для команды cat (аналог Unix команды cat)

python
    try:
        with open(args.input, "r", encoding="utf-8") as f:
            for line_num, line in enumerate(f, 1):
Открытие файла и построчное чтение с нумерацией строк, начиная с 1

python
                if args.n:
                    print(f"{line_num:6} {line}", end="")
                else:
                    print(line, end="")
Если передан флаг -n, выводит строки с номерами (отформатированными на 6 символов)

Иначе выводит просто содержимое строк

end="" предотвращает добавление лишних переносов строк

Команда STATS
python
def stats_command(args):
Функция для команды статистики

python
    text = read_text_file(args.input)
    normalize_text = normalize(text)
    tokens = tokenize(normalize_text)
    frequencies = count_freq(tokens)
    top_5 = top_n(frequencies, args.top)
Чтение файла → нормализация текста → токенизация → подсчет частот → получение топ-N слов

python
    print("Топ-5:")
    for item in top_5:
        print(f"{item[0]}: {item[1]}")
Вывод заголовка и списка топ-слов в формате "слово: частота"

Основная функция и парсинг аргументов
python
def main():
    parser = argparse.ArgumentParser(
        description="CLI-утилиты для работы с текстом"
    )
Создание основного парсера аргументов с описанием

python
    subparsers = parser.add_subparsers(dest="command", help="Доступные команды")
Создание подпарсеров для разных команд с сохранением выбранной команды в args.command

Парсер для команды CAT
python
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Путь к входному файлу")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")
Создание парсера для команды "cat"

--input - обязательный аргумент с путем к файлу

-n - флаг (если присутствует, значение True) для нумерации строк

Парсер для команды STATS
python
    stats_parser = subparsers.add_parser("stats", help="Анализ частот слов")
    stats_parser.add_argument("--input", required=True, help="Путь к текстовому файлу")
    stats_parser.add_argument("--top", type=int, default=5, help="Количество топ-слов")
--top - необязательный аргумент (по умолчанию 5) для указания количества слов в топе

python
    args = parser.parse_args()
Парсинг аргументов командной строки

python
    if args.command == "cat":
        cat_command(args)
    elif args.command == "stats":
        stats_command(args)
    else:
        parser.print_help()
Вызов соответствующей функции в зависимости от команды

Если команда не указана - вывод справки

Запуск программы
python
if __name__ == "__main__":
    main()
Стандартная конструкция для запуска функции main() при непосредственном выполнении файла

Примеры использования:
python script.py cat --input file.txt -n

python script.py stats --input file.txt --top 10






Импорт модулей и настройка пути
python
import argparse
Импорт модуля для обработки аргументов командной строки

python
import sys
Импорт системного модуля для работы с системными функциями (в данном случае для выхода из программы)

python
sys.path.append(r'C:\Users\Lucia\PycharmProjects\LabsOnishenko\src')
Добавляет абсолютный путь к проекту в системный путь Python

r'' означает raw string - строка без экранирования, чтобы обратные слеши не интерпретировались специально

Это позволяет импортировать модули из указанной директории

python
from lib.convertor import csv_to_json, csv_to_xlsx, json_to_csv
Импорт конкретных функций конвертации из пользовательского модуля lib.convertor:

csv_to_json - конвертация из CSV в JSON

csv_to_xlsx - конвертация из CSV в XLSX (Excel)

json_to_csv - конвертация из JSON в CSV

Функции команд конвертации
Команда JSON в CSV
python
def json2csv_command(args):
Объявление функции для обработки команды конвертации JSON в CSV

python
    try:
Начало блока обработки исключений

python
        json_to_csv(args.infile, args.out)
Вызов импортированной функции конвертации с передачей входного и выходного файлов

python
        print(f"Успешно конвертировано: {args.infile} -> {args.out}")
Вывод сообщения об успешной конвертации с использованием f-строки

python
    except Exception as e:
Перехват любого исключения, которое может возникнуть при конвертации

python
        print(f"Ошибка при конвертации JSON в CSV: {e}")
Вывод сообщения об ошибке с деталями исключения

python
        sys.exit(1)
Завершение программы с кодом ошибки 1

Команда CSV в JSON
python
def csv2json_command(args):
Функция для конвертации CSV в JSON

python
    try:
        csv_to_json(args.infile, args.out)
        print(f"Успешно конвертировано: {args.infile} -> {args.out}")
    except Exception as e:
        print(f"Ошибка при конвертации CSV в JSON: {e}")
        sys.exit(1)
Аналогичная структура, но для конвертации CSV → JSON

Команда CSV в XLSX
python
def csv2xlsx_command(args):
Функция для конвертации CSV в XLSX (Excel)

python
    try:
        csv_to_xlsx(args.infile, args.out)
        print(f"Успешно конвертировано: {args.infile} -> {args.out}")
    except Exception as e:
        print(f"Ошибка при конвертации CSV в XLSX: {e}")
        sys.exit(1)
Аналогичная структура для конвертации CSV → XLSX

Основная функция и парсинг аргументов
python
def main():
Объявление главной функции программы

python
    parser = argparse.ArgumentParser(description="Конвертер между форматами данных")
Создание основного парсера аргументов с описанием утилиты

python
    subparsers = parser.add_subparsers(dest="command", help="Доступные команды")
Создание системы подпарсеров для разных команд

dest="command" - значение выбранной команды будет сохранено в атрибуте command

help - текст справки для подпарсеров

Парсер для команды JSON2CSV
python
    json2csv_parser = subparsers.add_parser("json2csv", help="Конвертация JSON в CSV")
Создание подпарсера для команды "json2csv" с текстом помощи

python
    json2csv_parser.add_argument(
        "--input", dest="infile", required=True, help="Входной JSON файл"
    )
Добавление аргумента для входного файла:

--input - имя аргумента в командной строке

dest="infile" - значение будет сохранено в атрибуте infile

required=True - аргумент обязателен

help - описание аргумента

python
    json2csv_parser.add_argument("--out", required=True, help="Выходной CSV файл")
Аргумент для выходного файла (обязательный)

Парсер для команды CSV2JSON
python
    csv2json_parser = subparsers.add_parser("csv2json", help="Конвертация CSV в JSON")
Создание подпарсера для команды "csv2json"

python
    csv2json_parser.add_argument(
        "--input", dest="infile", required=True, help="Входной CSV файл"
    )
    csv2json_parser.add_argument("--out", required=True, help="Выходной JSON файл")
Аналогичные аргументы для CSV → JSON конвертации

Парсер для команды CSV2XLSX
python
    csv2xlsx_parser = subparsers.add_parser("csv2xlsx", help="Конвертация CSV в XLSX")
Создание подпарсера для команды "csv2xlsx"

python
    csv2xlsx_parser.add_argument(
        "--input", dest="infile", required=True, help="Входной CSV файл"
    )
    csv2xlsx_parser.add_argument("--out", required=True, help="Выходной XLSX файл")
Аргументы для CSV → XLSX конвертации

python
    args = parser.parse_args()
Парсинг аргументов командной строки, переданных при запуске программы

Маршрутизация команд
python
    if args.command == "json2csv":
        json2csv_command(args)
Если выбрана команда "json2csv", вызываем соответствующую функцию

python
    elif args.command == "csv2json":
        csv2json_command(args)
Если выбрана команда "csv2json", вызываем соответствующую функцию

python
    elif args.command == "csv2xlsx":
        csv2xlsx_command(args)
Если выбрана команда "csv2xlsx", вызываем соответствующую функцию

python
    else:
        parser.print_help()
Если команда не указана или не распознана, выводим справку по использованию

Запуск программы
python
if __name__ == "__main__":
    main()
Стандартная конструкция Python:

name - специальная переменная, которая равна "main" когда скрипт запускается напрямую

main() - вызов главной функции программы

Примеры использования:
python script.py json2csv --input data.json --out data.csv

python script.py csv2json --input data.csv --out data.json

python script.py csv2xlsx --input data.csv --out data.xlsx

