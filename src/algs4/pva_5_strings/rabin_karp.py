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
    """
    Determine whether an integer is likely prime using the Rabin–Miller probabilistic primality test.
    
    Performs five randomized witness rounds; returns `True` when n passes all rounds (probably prime) and `False` when a witness proves n composite. Values less than 2 are considered composite.
    
    Parameters:
        n (int): Integer to test for primality.
    
    Returns:
        bool: `True` if n is probably prime, `False` if n is composite.
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
    """
    Generate a prime number with the specified bit length.
    
    Parameters:
        bits (int): Bit length of the desired prime; must be at least 2.
    
    Returns:
        int: A prime number between 2^(bits-1) and 2^bits - 1 (inclusive).
    
    Raises:
        ValueError: If `bits` is less than 2 or no prime is found after the maximum number of attempts.
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
        """
        Initialize the Rabin-Karp searcher with the given pattern.
        
        Parameters:
            pattern (str): The pattern to search for; must be a non-empty string.
        
        Raises:
            ValueError: If `pattern` is None or an empty string.
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
        """
        The search pattern stored in this RabinKarp instance.
        
        Returns:
            pattern (str): The stored pattern string.
        """
        return self._pattern

    def search(self, text: str) -> int:
        """
        Finds the first occurrence of the stored pattern in the given text.
        
        Parameters:
            text (str): The text to search.
        
        Returns:
            int: Index of the first match, or `len(text)` if no match is found.
        
        Raises:
            ValueError: If `text` is None.
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
        """
        Yield all start indices where the stored pattern occurs in the given text.
        
        Parameters:
            text (str): Text to search for the pattern.
        
        Returns:
            Iterator[int]: An iterator that yields the start index of each verified occurrence in ascending order.
        
        Raises:
            ValueError: If `text` is None.
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
        """
        Count occurrences of the stored pattern in the given text.
        
        Parameters:
            text (str): Text to search.
        
        Returns:
            int: Number of occurrences of the stored pattern in text (including overlapping matches).
        
        Raises:
            ValueError: If text is None.
        """
        return sum(1 for _ in self.search_all(text))

    def _hash(self, key: str) -> int:
        """
        Compute the rolling (polynomial) hash value of a string using the instance's alphabet size and modulus.
        
        Parameters:
            key (str): Input string to hash.
        
        Returns:
            int: Hash value of `key` in the range [0, self._q - 1] (computed modulo `self._q`).
        """
        hash_value = 0
        for char in key:
            hash_value = (self._R * hash_value + ord(char)) % self._q
        return hash_value

    def _verify_match(self, text: str, pos: int) -> bool:
        """
        Verify that the stored pattern matches the substring of `text` starting at `pos`.
        
        Parameters:
            text (str): The text to compare against.
            pos (int): Start index in `text` for the comparison.
        
        Returns:
            bool: `True` if the substring `text[pos:pos+pattern_length]` equals the pattern, `False` otherwise. Returns `False` if the comparison would extend past the end of `text`.
        """
        if pos + self._m > len(text):
            return False
        return text[pos : pos + self._m] == self._pattern

    def __repr__(self) -> str:
        """
        Return a concise string representation of the RabinKarp instance.
        
        Returns:
            repr_str (str): A string of the form "RabinKarp('<pattern>')" showing the stored pattern.
        """
        return f"RabinKarp('{self._pattern}')"


def main() -> None:
    """
    Command-line interface for running Rabin-Karp pattern search on a given pattern and text.
    
    Expects exactly two command-line arguments: the search pattern and the text to search. Prints the text, pattern, the first match position (if any), a list of all match positions when there are multiple matches, a visual alignment of the first match, and timing information for construction and search. Exits with status code 1 if the argument count is incorrect.
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