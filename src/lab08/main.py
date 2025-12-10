from pathlib import Path

from src.lab08.models import Student
from src.lab08.serialize import students_from_json, students_to_json


def main():
    students = [
        Student(
            fio="Онищенко Светлана Николаевна",
            birthdate="2007-11-04",
            group="BIVT-25-4",
            gpa=5.00,
        ),
        Student(
            fio="Ткаченко Никита Дмитриевич",
            birthdate="2009-01-18",
            group="BIVT-25-4",
            gpa=5.0,
        ),
        Student(
            fio="Понаревская Наталия Владимировна",
            birthdate="2007-08-28",
            group="BIVT-25-4",
            gpa=5.0,
        ),
    ]

    json_path = Path("data/students.json")

    students_to_json(students, json_path)
    print(f"→ JSON сохранён в {json_path}")

    loaded_students = students_from_json(json_path)
    print("→ Загружено студентов:", len(loaded_students))

    print("\nСтуденты из JSON")
    for s in loaded_students:
        print(s)
        print()


if __name__ == "__main__":
    main()