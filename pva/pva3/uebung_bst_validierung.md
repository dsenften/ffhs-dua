# Übung: BST-Validierung

## Lernziele

Nach dieser Übung können Sie:

- Die BST-Eigenschaft formal definieren und überprüfen
- Rekursive Algorithmen mit Grenzwerten implementieren
- Die Zeitkomplexität von Baum-Traversierungen analysieren
- Edge Cases bei der Validierung von Datenstrukturen erkennen

## Hintergrund

Ein **Binary Search Tree (BST)** ist eine fundamentale Datenstruktur in der Informatik.
Die zentrale Eigenschaft eines BST ist die **BST-Invariante**:

> Für jeden Knoten im Baum gilt:
> - Alle Schlüssel im **linken Teilbaum** sind **kleiner** als der Schlüssel des Knotens
> - Alle Schlüssel im **rechten Teilbaum** sind **grösser** als der Schlüssel des Knotens

Diese Eigenschaft muss für **jeden Knoten** im gesamten Baum gelten, nicht nur für die direkten Kinder!

### Beispiel: Gültiger BST

```text
        8
       / \
      3   10
     / \    \
    1   6   14
       / \   /
      4   7 13
```

Hier gilt für jeden Knoten die BST-Eigenschaft.

### Beispiel: Ungültiger BST

```text
        8
       / \
      3   10
     / \    \
    1   6   14
       / \   /
      4   9 13
```

Dieser Baum ist **ungültig**, weil der Knoten mit Schlüssel `9` im linken Teilbaum der Wurzel `8` liegt,
aber grösser als `8` ist. Die BST-Eigenschaft ist verletzt!

## Aufgabenstellung

Implementieren Sie eine Methode `is_valid_bst()`, die überprüft, ob ein gegebener Binary Search Tree
die BST-Eigenschaft erfüllt.

### Anforderungen

1. **Vollständige Validierung**: Die Methode muss die BST-Eigenschaft für **alle** Knoten überprüfen,
nicht nur für direkte Eltern-Kind-Beziehungen.

2. **Effiziente Implementierung**: Die Methode sollte jeden Knoten nur einmal besuchen (Zeitkomplexität: O(n)).

3. **Korrekte Grenzwerte**: Verwenden Sie Minimal- und Maximalwerte, um sicherzustellen,
dass jeder Knoten in seinem erlaubten Wertebereich liegt.

4. **Edge Cases**: Ihre Implementierung sollte folgende Spezialfälle korrekt behandeln:
   - Leerer Baum (ist gültig)
   - Baum mit nur einem Knoten (ist gültig)
   - Baum mit duplizierten Schlüsseln (ist ungültig)

### Hinweise

- Nutzen Sie eine **rekursive Hilfsmethode**, die Minimal- und Maximalwerte als Parameter übergeben bekommt
- Der Wertebereich für die Wurzel ist zunächst unbeschränkt: `(-∞, +∞)`
- Beim Abstieg nach links wird der Maximalwert auf den Schlüssel des aktuellen Knotens gesetzt
- Beim Abstieg nach rechts wird der Minimalwert auf den Schlüssel des aktuellen Knotens gesetzt

### Zeitkomplexität

Analysieren Sie die Zeitkomplexität Ihrer Implementierung:

- **Best Case**: O(?)
- **Average Case**: O(?)
- **Worst Case**: O(?)

## Python-Gerüst

Verwenden Sie die bestehende `BST`-Klasse aus `src/algs4/pva_3_searching/bst.py` als Grundlage.

```python
from typing import TypeVar, Generic
from src.algs4.pva_3_searching.bst import BST, Node

K = TypeVar("K")  # Key type (muss vergleichbar sein)
V = TypeVar("V")  # Value type


class BSTValidator(Generic[K, V]):
    """Validator für Binary Search Trees."""

    def __init__(self, bst: BST[K, V]) -> None:
        """Initialisiert den Validator mit einem BST.

        Args:
            bst: Der zu validierende Binary Search Tree
        """
        self.bst = bst

    def is_valid_bst(self) -> bool:
        """Überprüft, ob der BST die BST-Eigenschaft erfüllt.

        Returns:
            bool: True wenn der BST gültig ist, False sonst
        """
        # TODO: Implementieren Sie diese Methode
        pass

    def _is_valid_bst_helper(
        self,
        node: Node[K, V] | None,
        min_val: K | None,
        max_val: K | None
    ) -> bool:
        """Rekursive Hilfsmethode zur BST-Validierung.

        Args:
            node: Aktueller Knoten
            min_val: Minimaler erlaubter Schlüsselwert (None = unbeschränkt)
            max_val: Maximaler erlaubter Schlüsselwert (None = unbeschränkt)

        Returns:
            bool: True wenn der Teilbaum gültig ist, False sonst
        """
        # TODO: Implementieren Sie diese Methode
        pass


# Testfälle
def test_valid_bst() -> None:
    """Test: Gültiger BST."""
    bst = BST[int, str]()
    bst.put(8, "acht")
    bst.put(3, "drei")
    bst.put(10, "zehn")
    bst.put(1, "eins")
    bst.put(6, "sechs")
    bst.put(14, "vierzehn")

    validator = BSTValidator(bst)
    assert validator.is_valid_bst(), "BST sollte gültig sein"
    print("✓ Test 1 bestanden: Gültiger BST erkannt")


def test_empty_bst() -> None:
    """Test: Leerer BST."""
    bst = BST[int, str]()
    validator = BSTValidator(bst)
    assert validator.is_valid_bst(), "Leerer BST sollte gültig sein"
    print("✓ Test 2 bestanden: Leerer BST erkannt")


def test_single_node() -> None:
    """Test: BST mit nur einem Knoten."""
    bst = BST[int, str]()
    bst.put(5, "fünf")
    validator = BSTValidator(bst)
    assert validator.is_valid_bst(), "BST mit einem Knoten sollte gültig sein"
    print("✓ Test 3 bestanden: Einzelner Knoten erkannt")


def test_invalid_bst_manual() -> None:
    """Test: Manuell konstruierter ungültiger BST.

    Hinweis: Dieser Test erfordert direkten Zugriff auf die Knoten-Struktur,
    um einen ungültigen BST zu konstruieren (da die put-Methode immer einen
    gültigen BST erzeugt).
    """
    # Konstruiere manuell einen ungültigen BST:
    #       8
    #      / \
    #     3   10
    #    / \
    #   1   9  <- 9 ist grösser als 8, sollte aber im linken Teilbaum sein!

    bst = BST[int, str]()
    bst._root = Node(8, "acht", 4)
    bst._root.left = Node(3, "drei", 3)
    bst._root.right = Node(10, "zehn", 1)
    bst._root.left.left = Node(1, "eins", 1)
    bst._root.left.right = Node(9, "neun", 1)  # Verletzt BST-Eigenschaft!

    validator = BSTValidator(bst)
    assert not validator.is_valid_bst(), "BST sollte ungültig sein"
    print("✓ Test 4 bestanden: Ungültiger BST erkannt")


if __name__ == "__main__":
    print("Starte BST-Validierungs-Tests...\n")
    test_valid_bst()
    test_empty_bst()
    test_single_node()
    test_invalid_bst_manual()
    print("\n✓ Alle Tests bestanden!")
```

## Vorgehen

1. **Verstehen Sie das Problem**: Lesen Sie die Aufgabenstellung sorgfältig und zeichnen Sie Beispiele auf Papier.

2. **Entwickeln Sie einen Algorithmus**: Überlegen Sie sich, wie Sie die BST-Eigenschaft rekursiv überprüfen können.

3. **Implementieren Sie die Lösung**: Füllen Sie die beiden TODO-Methoden aus.

4. **Testen Sie Ihre Lösung**: Führen Sie die bereitgestellten Tests aus und fügen Sie eigene Testfälle hinzu.

5. **Analysieren Sie die Komplexität**: Bestimmen Sie die Zeitkomplexität Ihrer Lösung.

## Zusatzaufgaben (Optional)

1. **Iterative Lösung**: Implementieren Sie eine iterative Version der Validierung mit einem Stack.

2. **Erweiterte Validierung**: Erweitern Sie die Validierung um zusätzliche Eigenschaften:
   - Überprüfen Sie, ob die `n`-Werte (Teilbaumgrössen) korrekt sind
   - Überprüfen Sie, ob der Baum balanciert ist (AVL-Eigenschaft)

3. **Visualisierung**: Erstellen Sie eine Funktion, die einen ungültigen BST visualisiert und die Stelle markiert,
an der die BST-Eigenschaft verletzt wird.

## Abgabe

Speichern Sie Ihre Lösung als `uebung_bst_validierung_loesung.py` im selben Verzeichnis.

Viel Erfolg! 🚀
