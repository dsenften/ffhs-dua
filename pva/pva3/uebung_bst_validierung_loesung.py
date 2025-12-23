"""Musterlösung: BST-Validierung

Diese Lösung demonstriert, wie man überprüft, ob ein Binary Search Tree
die BST-Eigenschaft erfüllt.

Autor: Daniel Senften <daniel.senften@ffhs.ch>
Datum: 2025
"""

from typing import TypeVar

from src.algs4.pva_3_searching.bst import BST, Node

K = TypeVar("K")  # Key type (muss vergleichbar sein)
V = TypeVar("V")  # Value type


class BSTValidator[K, V]:
    """Validator für Binary Search Trees.

    Diese Klasse implementiert eine Methode zur Überprüfung der BST-Eigenschaft.
    Die Validierung erfolgt rekursiv mit Hilfe von Minimal- und Maximalwerten.

    Zeitkomplexität: O(n) - jeder Knoten wird genau einmal besucht
    Platzkomplexität: O(h) - Rekursionstiefe entspricht der Baumhöhe
    """

    def __init__(self, bst: BST[K, V]) -> None:
        """Initialisiert den Validator mit einem BST.

        Args:
            bst: Der zu validierende Binary Search Tree
        """
        self.bst = bst

    def is_valid_bst(self) -> bool:
        """Überprüft, ob der BST die BST-Eigenschaft erfüllt.

        Die BST-Eigenschaft besagt, dass für jeden Knoten gilt:
        - Alle Schlüssel im linken Teilbaum sind kleiner
        - Alle Schlüssel im rechten Teilbaum sind grösser

        Returns:
            bool: True wenn der BST gültig ist, False sonst

        Beispiele:
            >>> bst = BST[int, str]()
            >>> bst.put(5, "fünf")
            >>> bst.put(3, "drei")
            >>> bst.put(7, "sieben")
            >>> validator = BSTValidator(bst)
            >>> validator.is_valid_bst()
            True
        """
        return self._is_valid_bst_helper(self.bst._root, None, None)

    def _is_valid_bst_helper(
        self, node: Node[K, V] | None, min_val: K | None, max_val: K | None
    ) -> bool:
        """Rekursive Hilfsmethode zur BST-Validierung.

        Diese Methode überprüft, ob der Teilbaum mit Wurzel 'node' die
        BST-Eigenschaft erfüllt. Dabei wird sichergestellt, dass alle
        Schlüssel im erlaubten Wertebereich [min_val, max_val] liegen.

        Args:
            node: Aktueller Knoten (None für leeren Teilbaum)
            min_val: Minimaler erlaubter Schlüsselwert (None = unbeschränkt)
            max_val: Maximaler erlaubter Schlüsselwert (None = unbeschränkt)

        Returns:
            bool: True wenn der Teilbaum gültig ist, False sonst

        Algorithmus:
            1. Basisfall: Leerer Teilbaum ist gültig
            2. Überprüfe, ob der aktuelle Schlüssel im erlaubten Bereich liegt
            3. Rekursiv: Überprüfe linken Teilbaum mit angepasstem Maximum
            4. Rekursiv: Überprüfe rechten Teilbaum mit angepasstem Minimum
        """
        # Basisfall: Ein leerer Teilbaum ist immer gültig
        if node is None:
            return True

        # Überprüfe, ob der aktuelle Schlüssel die Grenzen verletzt
        if min_val is not None and node.key <= min_val:
            return False

        if max_val is not None and node.key >= max_val:
            return False

        # Rekursiv: Überprüfe beide Teilbäume
        # Linker Teilbaum: Alle Schlüssel müssen < node.key sein
        # Rechter Teilbaum: Alle Schlüssel müssen > node.key sein
        return self._is_valid_bst_helper(
            node.left, min_val, node.key
        ) and self._is_valid_bst_helper(node.right, node.key, max_val)


class BSTValidatorIterative[K, V]:
    """Alternative iterative Implementierung der BST-Validierung.

    Diese Variante verwendet einen Stack anstelle von Rekursion.
    Sie ist nützlich, wenn die Rekursionstiefe ein Problem darstellt.
    """

    def __init__(self, bst: BST[K, V]) -> None:
        """Initialisiert den Validator mit einem BST.

        Args:
            bst: Der zu validierende Binary Search Tree
        """
        self.bst = bst

    def is_valid_bst(self) -> bool:
        """Überprüft iterativ, ob der BST die BST-Eigenschaft erfüllt.

        Returns:
            bool: True wenn der BST gültig ist, False sonst
        """
        if self.bst._root is None:
            return True

        # Stack enthält Tupel: (node, min_val, max_val)
        stack: list[tuple[Node[K, V], K | None, K | None]] = [
            (self.bst._root, None, None)
        ]

        while stack:
            node, min_val, max_val = stack.pop()

            # Überprüfe Grenzen
            if min_val is not None and node.key <= min_val:
                return False
            if max_val is not None and node.key >= max_val:
                return False

            # Füge Kindknoten zum Stack hinzu
            if node.right is not None:
                stack.append((node.right, node.key, max_val))
            if node.left is not None:
                stack.append((node.left, min_val, node.key))

        return True


# ============================================================================
# Testfälle
# ============================================================================


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

    Konstruiert einen Baum, der die BST-Eigenschaft verletzt:
           8
          / \
         3   10
        / \
       1   9  <- 9 ist grösser als 8, sollte aber im linken Teilbaum sein!
    """
    bst = BST[int, str]()
    bst._root = Node(8, "acht", 4)
    bst._root.left = Node(3, "drei", 3)
    bst._root.right = Node(10, "zehn", 1)
    bst._root.left.left = Node(1, "eins", 1)
    bst._root.left.right = Node(9, "neun", 1)  # Verletzt BST-Eigenschaft!

    validator = BSTValidator(bst)
    assert not validator.is_valid_bst(), "BST sollte ungültig sein"
    print("✓ Test 4 bestanden: Ungültiger BST erkannt")


def test_invalid_bst_right_subtree() -> None:
    """Test: Ungültiger BST mit Verletzung im rechten Teilbaum.

    Konstruiert einen Baum:
           8
          / \
         3   10
            /  \
           7   14  <- 7 ist kleiner als 8, sollte somit im linken Teilbaum sein!
    """
    bst = BST[int, str]()
    bst._root = Node(8, "acht", 5)
    bst._root.left = Node(3, "drei", 1)
    bst._root.right = Node(10, "zehn", 3)
    bst._root.right.left = Node(7, "sieben", 1)  # Verletzt BST-Eigenschaft!
    bst._root.right.right = Node(14, "vierzehn", 1)

    validator = BSTValidator(bst)
    assert not validator.is_valid_bst(), "BST sollte ungültig sein"
    print("✓ Test 5 bestanden: Ungültiger BST (rechter Teilbaum) erkannt")


def test_equal_keys() -> None:
    """Test: BST mit gleichen Schlüsseln (ungültig).

    Konstruiert einen Baum mit duplizierten Schlüsseln:
           5
          / \
         3   5  <- Duplizierter Schlüssel!
    """
    bst = BST[int, str]()
    bst._root = Node(5, "fünf", 3)
    bst._root.left = Node(3, "drei", 1)
    bst._root.right = Node(5, "fünf_dupliziert", 1)  # Gleicher Schlüssel!

    validator = BSTValidator(bst)
    assert not validator.is_valid_bst(), (
        "BST mit duplizierten Schlüsseln sollte ungültig sein"
    )
    print("✓ Test 6 bestanden: Duplizierte Schlüssel erkannt")


def test_iterative_validator() -> None:
    """Test: Iterative Implementierung."""
    # Gültiger BST
    bst = BST[int, str]()
    bst.put(8, "acht")
    bst.put(3, "drei")
    bst.put(10, "zehn")

    validator = BSTValidatorIterative(bst)
    assert validator.is_valid_bst(), "Gültiger BST sollte erkannt werden"

    # Ungültiger BST
    bst_invalid = BST[int, str]()
    bst_invalid._root = Node(8, "acht", 3)
    bst_invalid._root.left = Node(3, "drei", 2)
    bst_invalid._root.left.right = Node(9, "neun", 1)

    validator_invalid = BSTValidatorIterative(bst_invalid)
    assert not validator_invalid.is_valid_bst(), "Ungültiger BST sollte erkannt werden"
    print("✓ Test 7 bestanden: Iterative Implementierung funktioniert")


def test_large_valid_bst() -> None:
    """Test: Grosser gültiger BST."""
    bst = BST[int, int]()

    # Füge viele Elemente ein (put garantiert gültigen BST)
    for i in range(100):
        bst.put(i, i)

    validator = BSTValidator(bst)
    assert validator.is_valid_bst(), "Grosser BST sollte gültig sein"
    print("✓ Test 8 bestanden: Grosser gültiger BST erkannt")


def run_all_tests() -> None:
    """Führt alle Tests aus."""
    print("=" * 60)
    print("BST-Validierungs-Tests")
    print("=" * 60)
    print()

    test_valid_bst()
    test_empty_bst()
    test_single_node()
    test_invalid_bst_manual()
    test_invalid_bst_right_subtree()
    test_equal_keys()
    test_iterative_validator()
    test_large_valid_bst()

    print()
    print("=" * 60)
    print("✓ Alle Tests bestanden!")
    print("=" * 60)


# ============================================================================
# Komplexitätsanalyse
# ============================================================================

"""
ZEITKOMPLEXITÄT:
- Best Case: O(n) - auch bei einem balancierten Baum müssen alle Knoten besucht werden
- Average Case: O(n) - jeder Knoten wird genau einmal besucht
- Worst Case: O(n) - bei einem degenerierten Baum (Linked List)

PLATZKOMPLEXITÄT:
- Rekursive Version: O(h) - Rekursionstiefe entspricht der Baumhöhe h
  - Best Case (balancierter Baum): O(log n)
  - Worst Case (degenerierter Baum): O(n)
- Iterative Version: O(h) - Stack-Grösse entspricht der Baumhöhe

WARUM IST DIE LÖSUNG KORREKT?

1. Vollständige Überprüfung:
   Die Methode überprüft nicht nur direkte Eltern-Kind-Beziehungen,
   sondern stellt sicher, dass jeder Knoten in seinem erlaubten
   Wertebereich liegt.

2. Korrekte Grenzwerte:
   - Beim Abstieg nach links wird max_val auf den aktuellen Schlüssel gesetzt
   - Beim Abstieg nach rechts wird min_val auf den aktuellen Schlüssel gesetzt
   - Dies garantiert, dass alle Nachkommen die BST-Eigenschaft erfüllen

3. Basisfall:
   Ein leerer Teilbaum (None) ist immer gültig, was die Rekursion korrekt beendet

4. Strikte Ungleichungen:
   Die Verwendung von <= und >= stellt sicher, dass keine duplizierten
   Schlüssel erlaubt sind, was der BST-Definition entspricht.
"""


if __name__ == "__main__":
    run_all_tests()
