from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List

# Definition eines generischen Typs für vergleichbare Objekte
T = TypeVar('T')

class Comparable(ABC, Generic[T]):
    """
    Ein abstraktes Interface ähnlich zu Java's Comparable.
    Dies definiert die notwendigen Methoden für vergleichbare Objekte.
    """
    @abstractmethod
    def compare_to(self, other: T) -> int:
        """
        Vergleicht dieses Objekt mit einem anderen.
        Returns:
            - Negative Zahl wenn self < other
            - 0 wenn self == other
            - Positive Zahl wenn self > other
        """
        pass

    def __lt__(self, other: T) -> bool:
        return self.compare_to(other) < 0

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.compare_to(other) == 0

    def __gt__(self, other: T) -> bool:
        return self.compare_to(other) > 0

    def __le__(self, other: T) -> bool:
        return self.compare_to(other) <= 0

    def __ge__(self, other: T) -> bool:
        return self.compare_to(other) >= 0


# Beispielimplementierung: Eine Student-Klasse, die nach Matrikelnummer sortierbar ist
class Student(Comparable['Student']):
    def __init__(self, matrikel_nr: int, name: str):
        self.matrikel_nr = matrikel_nr
        self.name = name

    def compare_to(self, other: 'Student') -> int:
        return self.matrikel_nr - other.matrikel_nr

    def __str__(self) -> str:
        return f"Student(matrikel_nr={self.matrikel_nr}, name='{self.name}')"


# Beispielimplementierung: Eine generische sortierbare Liste
class SortedList(Generic[T]):
    def __init__(self):
        self.items: List[T] = []

    def add(self, item: T) -> None:
        """Fügt ein Element sortiert in die Liste ein."""
        self.items.append(item)
        self.items.sort(key=lambda x: x)  # Nutzt die __lt__ Methode

    def get_all(self) -> List[T]:
        return self.items.copy()


# Beispielnutzung
def main():
    # Erstellen einiger Studenten
    students = [
        Student(12345, "Max Mustermann"),
        Student(54321, "Erika Musterfrau"),
        Student(98765, "John Doe")
    ]

    # Verwendung der sortierbaren Liste
    sorted_students = SortedList[Student]()
    for student in students:
        sorted_students.add(student)

    # Ausgabe der sortierten Liste
    print("Sortierte Studentenliste:")
    for student in sorted_students.get_all():
        print(student)


if __name__ == "__main__":
    main()
