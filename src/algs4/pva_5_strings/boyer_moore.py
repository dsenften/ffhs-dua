"""Boyer-Moore String-Suchalgorithmus

Der Boyer-Moore-Algorithmus ist ein effizienter String-Suchalgorithmus,
der einen Muster-String in einem Text-String sucht. Im Gegensatz zu naiven Ansätzen
nutzt Boyer-Moore die "Bad Character Rule", um große Sprünge im Text zu machen
und dadurch die Anzahl der Vergleiche zu reduzieren.

Zeitkomplexität:
- Konstruktor (Bad Character Table): O(m + R), wobei m = Musterlänge, R = Alphabet-Grösse
- search(text): O(n/m) im besten Fall, O(n×m) im schlechtesten Fall
- Durchschnittlich sehr effizient, besonders bei großen Alphabeten

Vorteile:
- Sehr effizient bei großen Alphabeten und langen Mustern
- Kann Text von rechts nach links überspringen
- Sublineare Laufzeit im besten Fall (O(n/m))
- Einfache Implementierung der Bad Character Rule

Nachteile:
- Worst-Case O(n×m) Laufzeit (schlechter als KMP)
- Benötigt O(R) Speicher für Bad Character Table
- Ohne Good Suffix Rule nicht optimal

Beispiele:
    >>> bm = BoyerMoore("NEEDLE")
    >>> bm.search("HAYSTACK WITH NEEDLE IN IT")
    14
    >>> bm.search("NO MATCH")
    17

    >>> # Für stdin/stdout CLI-Nutzung:
    >>> # python3 -m src.algs4.pva_5_strings.boyer_moore <pattern> <text>
"""

from collections.abc import Iterator


class BoyerMoore:
    """Boyer-Moore String-Suchalgorithmus.

    Implementiert effiziente String-Suche durch Verwendung der
    "Bad Character Rule". Die Bad Character Table wird einmal
    beim Konstruktor aufgebaut und kann dann für beliebig viele
    Suchen wiederverwendet werden.

    Diese Implementierung nutzt nur die Bad Character Rule,
    nicht die komplexere Good Suffix Rule.

    Attributes:
        _pattern: Das Suchmuster als String
        _R: Grösse des Alphabets (256 für extended ASCII)
        _right: Bad Character Table (rightmost occurrence)
    """

    def __init__(self, pattern: str) -> None:
        """Initialisiert den Boyer-Moore-Algorithmus mit einem Suchmuster.

        Baut die Bad Character Table für das Muster auf.
        Die Tabelle speichert für jedes Zeichen die rechteste Position
        im Muster (oder -1 wenn nicht vorhanden).

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

        # Initialisiere Bad Character Table
        # -1 bedeutet: Zeichen kommt nicht im Muster vor
        self._right: list[int] = [-1] * self._R

        # Baue Bad Character Table auf
        # Speichere für jedes Zeichen die rechteste Position im Muster
        for j in range(m):
            self._right[ord(pattern[j])] = j

    @property
    def pattern(self) -> str:
        """Gibt das Suchmuster zurück.

        Returns:
            str: Das Suchmuster
        """
        return self._pattern

    def search(self, text: str) -> int:
        """Sucht das Muster im gegebenen Text.

        Verwendet die Bad Character Rule, um große Sprünge im Text zu machen.
        Der Algorithmus vergleicht das Muster von rechts nach links.

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

        # Leerer Text oder Muster länger als Text
        if n == 0 or m > n:
            return n

        i: int = 0  # Text-Index (Anfang des aktuellen Vergleichs)

        # Durchlaufe Text mit variablen Sprüngen
        while i <= n - m:
            skip: int = 0

            # Vergleiche Muster von rechts nach links
            for j in range(m - 1, -1, -1):
                if self._pattern[j] != text[i + j]:
                    # Bad Character: Berechne Sprung
                    skip = j - self._right[ord(text[i + j])]
                    if skip < 1:
                        skip = 1  # Mindestens 1 Position vorwärts
                    break

            # Wenn kein Mismatch gefunden wurde, haben wir einen Match
            if skip == 0:
                return i

            # Springe um berechnete Distanz
            i += skip

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
        return f"BoyerMoore(pattern='{self._pattern}')"


if __name__ == "__main__":
    import sys

    # CLI-Interface für Boyer-Moore String-Suche
    if len(sys.argv) != 3:
        print(
            "Verwendung: python3 -m src.algs4.pva_5_strings.boyer_moore <pattern> <text>"
        )
        print("\nBeispiel:")
        print(
            "  python3 -m src.algs4.pva_5_strings.boyer_moore NEEDLE "
            '"HAYSTACK WITH NEEDLE IN IT"'
        )
        sys.exit(1)

    pattern: str = sys.argv[1]
    text: str = sys.argv[2]

    # Erstelle Boyer-Moore-Instanz
    bm = BoyerMoore(pattern)

    # Suche Muster
    offset: int = bm.search(text)

    # Gebe Ergebnis aus
    print(f"text:    {text}")
    print(f"pattern: {' ' * offset}{pattern}")

    if offset < len(text):
        print(f"\nMuster gefunden an Position {offset}")

        # Zeige alle Vorkommen
        all_matches = list(bm.search_all(text))
        if len(all_matches) > 1:
            print(f"Insgesamt {len(all_matches)} Vorkommen: {all_matches}")
    else:
        print("\nMuster nicht gefunden")
