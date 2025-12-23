"""Knuth-Morris-Pratt String-Suchalgorithmus

Der KMP-Algorithmus (Knuth-Morris-Pratt) ist ein effizienter String-Suchalgorithmus,
der einen Muster-String in einem Text-String sucht. Im Gegensatz zu naiven Ansätzen
nutzt KMP eine vorberechnete Tabelle (DFA - Deterministic Finite Automaton), um
Backtracking zu vermeiden.

Zeitkomplexität:
- Konstruktor (DFA-Aufbau): O(m × R), wobei m = Musterlänge, R = Alphabet-Grösse
- search(text): O(n), wobei n = Textlänge
- Garantierte lineare Laufzeit, auch im Worst-Case!

Vorteile:
- Keine Backtracking im Text (Index läuft nur vorwärts)
- Worst-Case O(n) Laufzeit für Suche
- Effizient für wiederholte Suchen mit gleichem Muster

Nachteile:
- Benötigt O(m × R) Speicher für DFA
- Initialisierung aufwändiger als bei einfachen Algorithmen

Beispiele:
    >>> kmp = KMP("NEEDLE")
    >>> kmp.search("HAYSTACK WITH NEEDLE IN IT")
    14
    >>> kmp.search("NO MATCH")
    17

    >>> # Für stdin/stdout CLI-Nutzung:
    >>> # python3 -m src.algs4.pva_5_strings.kmp <pattern> <text>
"""

from collections.abc import Iterator


class KMP:
    """Knuth-Morris-Pratt String-Suchalgorithmus.

    Implementiert effiziente String-Suche durch Verwendung eines
    Deterministischen Finiten Automaten (DFA). Der DFA wird einmal
    beim Konstruktor aufgebaut und kann dann für beliebig viele
    Suchen wiederverwendet werden.

    Attributes:
        _pattern: Das Suchmuster als String
        _R: Grösse des Alphabets (256 für extended ASCII)
        _dfa: Deterministic Finite Automaton (2D-Array)
    """

    def __init__(self, pattern: str) -> None:
        """Initialisiert den KMP-Algorithmus mit einem Suchmuster.

        Baut den DFA (Deterministic Finite Automaton) für das Muster auf.
        Der DFA wird verwendet, um die Suche ohne Backtracking durchzuführen.

        Args:
            pattern: Das Suchmuster (nicht-leerer String)

        Raises:
            ValueError: Wenn pattern None oder leer ist
        """
        if pattern is None:
            raise ValueError("Muster darf nicht None sein")
        if not pattern:
            raise ValueError("Muster darf nicht leer sein")

        self._pattern: str = pattern
        self._R: int = 256  # Extended ASCII
        m: int = len(pattern)

        # Initialisiere DFA (R × m Matrix)
        self._dfa: list[list[int]] = [[0] * m for _ in range(self._R)]

        # Baue DFA auf
        self._dfa[ord(pattern[0])][0] = 1

        x: int = 0  # Restart-Zustand
        for j in range(1, m):
            # Kopiere Mismatch-Fälle vom Restart-Zustand
            for c in range(self._R):
                self._dfa[c][j] = self._dfa[c][x]

            # Setze Match-Fall
            self._dfa[ord(pattern[j])][j] = j + 1

            # Update Restart-Zustand
            x = self._dfa[ord(pattern[j])][x]

    @property
    def pattern(self) -> str:
        """Gibt das Suchmuster zurück.

        Returns:
            str: Das Suchmuster
        """
        return self._pattern

    def search(self, text: str) -> int:
        """Sucht das Muster im gegebenen Text.

        Verwendet den vorberechneten DFA, um das Muster zu finden.
        Der Text-Index läuft nur vorwärts (kein Backtracking).

        Args:
            text: Der zu durchsuchende Text

        Returns:
            int: Index der ersten Übereinstimmung, oder len(text) wenn nicht gefunden

        Raises:
            ValueError: Wenn text None ist
        """
        if text is None:
            raise ValueError("Text darf nicht None sein")

        n: int = len(text)
        m: int = len(self._pattern)

        i: int = 0  # Text-Index
        j: int = 0  # Muster-Index

        # Durchlaufe Text (nur vorwärts, kein Backtracking!)
        while i < n and j < m:
            j = self._dfa[ord(text[i])][j]
            i += 1

        # Gefunden wenn j = m (Ende des Musters erreicht)
        if j == m:
            return i - m

        # Nicht gefunden
        return n

    def search_all(self, text: str) -> Iterator[int]:
        """Findet alle Vorkommen des Musters im Text.

        Args:
            text: Der zu durchsuchende Text

        Returns:
            Iterator[int]: Iterator über alle Match-Positionen

        Raises:
            ValueError: Wenn text None ist
        """
        if text is None:
            raise ValueError("Text darf nicht None sein")

        pos = 0
        while pos <= len(text) - len(self._pattern):
            # Suche ab aktueller Position
            remaining_text = text[pos:]
            offset = self.search(remaining_text)

            # Wenn gefunden
            if offset < len(remaining_text):
                yield pos + offset
                pos += offset + 1  # Weiter nach erstem Match
            else:
                break

    def count(self, text: str) -> int:
        """Zählt alle Vorkommen des Musters im Text.

        Args:
            text: Der zu durchsuchende Text

        Returns:
            int: Anzahl der Vorkommen

        Raises:
            ValueError: Wenn text None ist
        """
        if text is None:
            raise ValueError("Text darf nicht None sein")

        return sum(1 for _ in self.search_all(text))

    def __repr__(self) -> str:
        """Gibt eine String-Repräsentation zurück.

        Returns:
            str: String-Repräsentation
        """
        return f"KMP(pattern='{self._pattern}')"


if __name__ == "__main__":
    import sys

    # CLI-Interface für KMP String-Suche
    if len(sys.argv) != 3:
        print("Verwendung: python3 -m src.algs4.pva_5_strings.kmp <pattern> <text>")
        print("\nBeispiel:")
        print(
            "  python3 -m src.algs4.pva_5_strings.kmp abracadabra "
            "abacadabrabracabracadabrabrabracad"
        )
        sys.exit(1)

    pattern: str = sys.argv[1]
    text: str = sys.argv[2]

    # Erstelle KMP-Instanz
    kmp = KMP(pattern)

    # Suche Muster
    offset: int = kmp.search(text)

    # Gebe Ergebnis aus
    print(f"text:    {text}")
    print(f"pattern: {' ' * offset}{pattern}")

    if offset < len(text):
        print(f"\nMuster gefunden an Position {offset}")

        # Zeige alle Vorkommen
        all_matches = list(kmp.search_all(text))
        if len(all_matches) > 1:
            print(f"Insgesamt {len(all_matches)} Vorkommen: {all_matches}")
    else:
        print("\nMuster nicht gefunden")
