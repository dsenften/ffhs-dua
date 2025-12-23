"""Rabin-Karp String-Suchalgorithmus.

Der Rabin-Karp-Algorithmus ist ein String-Suchalgorithmus, der Rolling Hash
verwendet, um Muster in Texten zu finden. Er berechnet Hash-Werte für das
Muster und für jeden Substring der gleichen Länge im Text.

Zeitkomplexität:
- Bester Fall: O(n + m) - keine Hash-Kollisionen
- Durchschnittlicher Fall: O(n + m) - wenige Hash-Kollisionen
- Schlechtester Fall: O(n × m) - viele Hash-Kollisionen

Raumkomplexität: O(1)

Vorteile:
- Einfache Implementierung
- Gut für Multiple-Pattern-Suche
- Effizient bei wenigen Hash-Kollisionen
- Rolling Hash ermöglicht konstante Zeit pro Position

Nachteile:
- Worst-Case O(n × m) bei vielen Hash-Kollisionen
- Abhängig von guter Hash-Funktion
- Monte Carlo Version kann False Positives haben

Beispiele:
    >>> rk = RabinKarp("NEEDLE")
    >>> rk.search("HAYSTACK WITH NEEDLE IN IT")
    14
    >>> rk.search("NO MATCH")
    17

    >>> # Für stdin/stdout CLI-Nutzung:
    >>> # python3 -m src.algs4.pva_5_strings.rabin_karp <pattern> <text>
"""

import random
from collections.abc import Iterator


def _rabin_miller_test(n: int) -> bool:
    """Rabin-Miller Primzahltest.

    Args:
        n: Zu testende Zahl

    Returns:
        True wenn n wahrscheinlich prim ist, False wenn n zusammengesetzt ist
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Schreibe n-1 als d * 2^r
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    # Führe mehrere Runden des Tests durch
    for _ in range(5):  # 5 Runden für gute Genauigkeit
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True


def _generate_prime(bits: int) -> int:
    """Generiert eine Primzahl mit der gewünschten Bit-Länge.

    Args:
        bits: Gewünschte Bit-Länge der Primzahl

    Returns:
        Eine Primzahl mit der gewünschten Bit-Länge

    Raises:
        ValueError: Wenn keine Primzahl nach vielen Versuchen gefunden wird
    """
    if bits < 2:
        raise ValueError("Bit-Länge muss mindestens 2 sein")

    max_attempts = 1000
    min_val = 2 ** (bits - 1)
    max_val = 2**bits - 1

    for _ in range(max_attempts):
        candidate = random.randrange(min_val, max_val + 1)
        if candidate % 2 == 0:
            candidate += 1

        if _rabin_miller_test(candidate):
            return candidate

    raise ValueError(
        f"Konnte keine Primzahl mit {bits} Bits nach {max_attempts} Versuchen finden"
    )


class RabinKarp:
    """Rabin-Karp String-Suchalgorithmus.

    Implementiert String-Suche durch Rolling Hash. Der Algorithmus berechnet
    Hash-Werte für das Muster und für jeden Substring der gleichen Länge im Text.
    Verwendet Las Vegas Version mit expliziter Verifikation bei Hash-Kollisionen.

    Attributes:
        _pattern: Das Suchmuster als String
        _m: Länge des Musters
        _R: Grösse des Alphabets (256 für extended ASCII)
        _q: Grosse Primzahl für modulare Arithmetik
        _rm: R^(m-1) mod q für Rolling Hash
        _pattern_hash: Hash-Wert des Musters
    """

    def __init__(self, pattern: str) -> None:
        """Initialisiert den Rabin-Karp Algorithmus mit einem Muster.

        Args:
            pattern: Das zu suchende Muster

        Raises:
            ValueError: Wenn pattern None oder leer ist
        """
        if pattern is None:
            raise ValueError("Muster darf nicht None sein")
        if not pattern:
            raise ValueError("Muster darf nicht leer sein")

        self._pattern: str = pattern
        self._m: int = len(pattern)
        self._R: int = 256  # Extended ASCII
        self._q: int = _generate_prime(31)  # Grosse Primzahl für Hash

        # Berechne R^(m-1) mod q für Rolling Hash
        self._rm: int = 1
        for _ in range(1, self._m):
            self._rm = (self._R * self._rm) % self._q

        # Berechne Hash-Wert des Musters
        self._pattern_hash: int = self._hash(pattern)

    @property
    def pattern(self) -> str:
        """Gibt das Suchmuster zurück.

        Returns:
            Das Suchmuster als String
        """
        return self._pattern

    def search(self, text: str) -> int:
        """Sucht das erste Vorkommen des Musters im Text.

        Args:
            text: Der zu durchsuchende Text

        Returns:
            Index des ersten Vorkommens, oder len(text) wenn nicht gefunden

        Raises:
            ValueError: Wenn text None ist
        """
        if text is None:
            raise ValueError("Text darf nicht None sein")
        if not text:
            return len(text)
        if len(text) < self._m:
            return len(text)

        n = len(text)
        text_hash = self._hash(text[: self._m])

        # Prüfe erste Position
        if self._pattern_hash == text_hash and self._verify_match(text, 0):
            return 0

        # Rolling Hash für restliche Positionen
        for i in range(self._m, n):
            # Entferne altes Zeichen und füge neues hinzu
            text_hash = (
                text_hash + self._q - self._rm * ord(text[i - self._m]) % self._q
            ) % self._q
            text_hash = (text_hash * self._R + ord(text[i])) % self._q

            # Prüfe Hash-Match und verifiziere bei Kollision
            if self._pattern_hash == text_hash and self._verify_match(
                text, i - self._m + 1
            ):
                return i - self._m + 1

        return n

    def search_all(self, text: str) -> Iterator[int]:
        """Sucht alle Vorkommen des Musters im Text.

        Args:
            text: Der zu durchsuchende Text

        Yields:
            Indizes aller Vorkommen des Musters

        Raises:
            ValueError: Wenn text None ist
        """
        if text is None:
            raise ValueError("Text darf nicht None sein")
        if not text or len(text) < self._m:
            return

        n = len(text)
        text_hash = self._hash(text[: self._m])

        # Prüfe erste Position
        if self._pattern_hash == text_hash and self._verify_match(text, 0):
            yield 0

        # Rolling Hash für restliche Positionen
        for i in range(self._m, n):
            # Entferne altes Zeichen und füge neues hinzu
            text_hash = (
                text_hash + self._q - self._rm * ord(text[i - self._m]) % self._q
            ) % self._q
            text_hash = (text_hash * self._R + ord(text[i])) % self._q

            # Prüfe Hash-Match und verifiziere bei Kollision
            if self._pattern_hash == text_hash and self._verify_match(
                text, i - self._m + 1
            ):
                yield i - self._m + 1

    def count(self, text: str) -> int:
        """Zählt alle Vorkommen des Musters im Text.

        Args:
            text: Der zu durchsuchende Text

        Returns:
            Anzahl der Vorkommen des Musters

        Raises:
            ValueError: Wenn text None ist
        """
        return sum(1 for _ in self.search_all(text))

    def _hash(self, key: str) -> int:
        """Berechnet Hash-Wert eines Strings mit Horner's Methode.

        Args:
            key: String für den der Hash berechnet werden soll

        Returns:
            Hash-Wert modulo q
        """
        hash_value = 0
        for char in key:
            hash_value = (self._R * hash_value + ord(char)) % self._q
        return hash_value

    def _verify_match(self, text: str, pos: int) -> bool:
        """Verifiziert einen potentiellen Match durch direkten Stringvergleich.

        Args:
            text: Der Text
            pos: Position des potentiellen Matches

        Returns:
            True wenn Match verifiziert, False sonst
        """
        if pos + self._m > len(text):
            return False
        return text[pos : pos + self._m] == self._pattern

    def __repr__(self) -> str:
        """String-Repräsentation des RabinKarp-Objekts.

        Returns:
            String-Repräsentation mit Muster
        """
        return f"RabinKarp('{self._pattern}')"


def main() -> None:
    """CLI-Interface für Rabin-Karp String-Suche.

    Verwendung:
        python3 -m src.algs4.pva_5_strings.rabin_karp <muster> <text>

    Beispiele:
        python3 -m src.algs4.pva_5_strings.rabin_karp "NEEDLE" "HAYSTACK WITH NEEDLE IN IT"
        python3 -m src.algs4.pva_5_strings.rabin_karp "abc" "abcabcabc"
    """
    import sys
    import time

    if len(sys.argv) != 3:
        print(
            "Verwendung: python3 -m src.algs4.pva_5_strings.rabin_karp <muster> <text>"
        )
        print()
        print("Beispiele:")
        print(
            '  python3 -m src.algs4.pva_5_strings.rabin_karp "NEEDLE" "HAYSTACK WITH NEEDLE IN IT"'
        )
        print('  python3 -m src.algs4.pva_5_strings.rabin_karp "abc" "abcabcabc"')
        print(
            '  echo "she sells sea shells by the sea shore" | python3 -m src.algs4.pva_5_strings.rabin_karp "sea"'
        )
        sys.exit(1)

    pattern = sys.argv[1]
    text = sys.argv[2]

    # Erstelle Rabin-Karp Instanz
    start_time = time.perf_counter()
    rk = RabinKarp(pattern)
    construction_time = time.perf_counter() - start_time

    # Führe Suche durch
    start_time = time.perf_counter()
    position = rk.search(text)
    search_time = time.perf_counter() - start_time

    # Ausgabe der Ergebnisse
    print(f"Text: {text}")
    print(f"Muster: {pattern}")
    print()

    if position < len(text):
        print(f"Muster gefunden an Position {position}")

        # Zeige alle Vorkommen
        all_matches = list(rk.search_all(text))
        if len(all_matches) > 1:
            print(f"Insgesamt {len(all_matches)} Vorkommen: {all_matches}")

        # Visuelle Darstellung
        print()
        print("Visuelle Darstellung:")
        print(f"Text:    {text}")
        print(f"Muster:  {' ' * position}{pattern}")

    else:
        print("Muster nicht gefunden")

    # Performance-Informationen
    print()
    print(f"Konstruktionszeit: {construction_time * 1000:.3f} ms")
    print(f"Suchzeit: {search_time * 1000:.3f} ms")
    print(f"Gesamtzeit: {(construction_time + search_time) * 1000:.3f} ms")
    print(f"Textlänge: {len(text)} Zeichen")
    print(f"Musterlänge: {len(pattern)} Zeichen")


if __name__ == "__main__":
    main()
