class Student:
    def __init__(self, name, note, original_position):
        self.name = name
        self.note = note
        self.original_position = original_position

    def __str__(self):
        return f"({self.name}, {self.note})"


def insertion_sort(arr):
    # Gehe durch alle Elemente ab dem zweiten Element
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1

        # Verschiebe Elemente nach rechts, solange:
        # 1. Das aktuelle Element eine bessere (kleinere) Note hat ODER
        # 2. Die Noten gleich sind UND das aktuelle Element eine frühere Originalposition hat
        while (j >= 0 and
               (arr[j].note > current.note or
                (arr[j].note == current.note and
                 arr[j].original_position > current.original_position))):
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = current

    return arr


# Testdaten erstellen
studenten = [
    Student("Maria", 2, 0),  # original_position = 0
    Student("Peter", 1, 1),  # original_position = 1
    Student("Anna", 2, 2),  # original_position = 2
    Student("Lisa", 1, 3)  # original_position = 3
]

print("Ursprüngliche Liste:")
for student in studenten:
    print(f"{student} (Original-Position: {student.original_position})")

# Liste sortieren
sortierte_liste = insertion_sort(studenten)

print("\nSortierte Liste:")
for student in sortierte_liste:
    print(f"{student} (Original-Position: {student.original_position})")

# Stabilitätstest
print("\nStabilitätstest:")
print("1. Für Note 1:", end=" ")
einser = [s for s in sortierte_liste if s.note == 1]
print("✓" if einser[0].original_position < einser[1].original_position else "✗")

print("2. Für Note 2:", end=" ")
zweier = [s for s in sortierte_liste if s.note == 2]
print("✓" if zweier[0].original_position < zweier[1].original_position else "✗")
