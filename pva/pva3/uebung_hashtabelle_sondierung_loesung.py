"""Musterlösung: Hashtabellen mit quadratischem Sondieren

Diese Lösung demonstriert das Einfügen von Werten in eine Hashtabelle
mit quadratischem Sondieren und analysiert die Eigenschaften der verwendeten
Hashfunktion.

Autor: FFHS DUA Kurs
Datum: 2025
"""

from collections import Counter
from collections.abc import Callable


class QuadraticProbingHashTable:
    """Hashtabelle mit quadratischem Sondieren.

    Diese Implementierung verwendet die Hashfunktion h(x) = (x * x) % 23
    und quadratisches Sondieren zur Kollisionsbehandlung.

    Zeitkomplexität:
    - Best Case: O(1) - keine Kollision
    - Average Case: O(1) - bei guter Hashfunktion und niedriger Auslastung
    - Worst Case: O(n) - viele Kollisionen oder hohe Auslastung
    """

    def __init__(self, capacity: int = 23) -> None:
        """Initialisiert eine Hashtabelle mit gegebener Kapazität.

        Args:
            capacity: Grösse der Hashtabelle (Standard: 23)
        """
        self.capacity = capacity
        self.table: list[int | None] = [None] * capacity
        self.size = 0

    def hash_function(self, x: int) -> int:
        """Berechnet den Hash-Wert für einen Schlüssel.

        Verwendet die Hashfunktion h(x) = (x * x) % 23

        Args:
            x: Zu hashender Schlüssel

        Returns:
            int: Hash-Wert (Index in der Tabelle)

        Beispiele:
            >>> ht = QuadraticProbingHashTable()
            >>> ht.hash_function(25)
            2
            >>> ht.hash_function(48)
            8
        """
        return (x * x) % self.capacity

    def quadratic_probe(self, initial_hash: int, attempt: int) -> int:
        """Berechnet den Index beim quadratischen Sondieren.

        Verwendet die Formel: Index = (initial_hash + i²) % capacity

        Args:
            initial_hash: Initialer Hash-Wert
            attempt: Anzahl der bisherigen Versuche (i)

        Returns:
            int: Neuer Index zum Prüfen

        Beispiele:
            >>> ht = QuadraticProbingHashTable()
            >>> ht.quadratic_probe(5, 0)
            5
            >>> ht.quadratic_probe(5, 1)
            6
            >>> ht.quadratic_probe(5, 2)
            9
        """
        return (initial_hash + attempt * attempt) % self.capacity

    def insert(self, value: int, verbose: bool = True) -> tuple[int, list[int]]:
        """Fügt einen Wert in die Hashtabelle ein.

        Verwendet quadratisches Sondieren bei Kollisionen.

        Args:
            value: Einzufügender Wert
            verbose: Wenn True, werden Berechnungsschritte ausgegeben

        Returns:
            Tuple[int, List[int]]: (finaler Index, Liste aller probierten Indizes)

        Raises:
            RuntimeError: Wenn die Tabelle voll ist
        """
        initial_hash = self.hash_function(value)
        probed_indices = []

        if verbose:
            print(f"\nBerechnung für Wert {value}:")
            print(
                f"h({value}) = ({value} * {value}) % {self.capacity} = {value * value} % {self.capacity} = {initial_hash}"
            )

        attempt = 0
        while attempt < self.capacity:
            index = self.quadratic_probe(initial_hash, attempt)
            probed_indices.append(index)

            if verbose:
                if attempt == 0:
                    print(
                        f"\nVersuch {attempt + 1} (i={attempt}): Index = ({initial_hash} + {attempt}²) % {self.capacity} = {index}"
                    )
                else:
                    calculation = initial_hash + attempt * attempt
                    print(
                        f"Versuch {attempt + 1} (i={attempt}): Index = ({initial_hash} + {attempt}²) % {self.capacity} = {calculation} % {self.capacity} = {index}"
                    )

                if self.table[index] is None:
                    print(f"  → Index {index} ist frei ✓")
                else:
                    print(
                        f"  → Index {index} ist belegt (Wert: {self.table[index]}) ✗ Kollision!"
                    )

            if self.table[index] is None:
                self.table[index] = value
                self.size += 1
                return index, probed_indices

            attempt += 1

        raise RuntimeError("Hashtabelle ist voll - kein freier Platz gefunden")

    def display(self) -> None:
        """Zeigt den aktuellen Zustand der Hashtabelle an."""
        print("\nAktueller Zustand der Hashtabelle:")
        print("Index | Wert")
        print("-" * 15)
        for i in range(self.capacity):
            value = self.table[i] if self.table[i] is not None else "-"
            print(f"{i:5} | {value}")
        print(f"\nBelegte Plätze: {self.size}/{self.capacity}")
        print()


def analyze_hash_function(
    hash_func: Callable[[int], int], capacity: int, value_range: range
) -> None:
    """Analysiert die Verteilung einer Hashfunktion.

    Args:
        hash_func: Zu analysierende Hashfunktion
        capacity: Grösse der Hashtabelle
        value_range: Bereich der zu testenden Werte
    """
    print("\n" + "=" * 60)
    print("Analyse der Hashfunktion h(x) = (x * x) % 23")
    print("=" * 60)

    # Berechne Hash-Werte für alle Werte im Bereich
    hash_values = [hash_func(x) for x in value_range]
    hash_distribution = Counter(hash_values)

    # Zeige Verteilung
    print(f"\nWertebereich: {value_range.start} bis {value_range.stop - 1}")
    print(f"Anzahl Werte: {len(value_range)}")
    print("\nVerteilung der Hash-Werte:")
    print(f"{'Index':<10} {'Häufigkeit':<15} {'Visualisierung'}")
    print("-" * 50)

    for i in range(capacity):
        count = hash_distribution.get(i, 0)
        bar = "█" * count
        print(f"{i:<10} {count:<15} {bar}")

    # Statistiken
    used_indices = len(hash_distribution)
    unused_indices = capacity - used_indices
    max_collisions = max(hash_distribution.values()) if hash_distribution else 0

    print("\nStatistiken:")
    print(
        f"  Genutzte Indizes: {used_indices}/{capacity} ({used_indices/capacity*100:.1f}%)"
    )
    print(
        f"  Ungenutzte Indizes: {unused_indices}/{capacity} ({unused_indices/capacity*100:.1f}%)"
    )
    print(f"  Maximale Kollisionen pro Index: {max_collisions}")

    # Zeige einige Beispiele
    print("\nBeispiel-Berechnungen:")
    examples = [0, 1, 5, 10, 25, 50, 100, 150, 200]
    for x in examples:
        if x in value_range:
            h = hash_func(x)
            print(f"  h({x:3}) = ({x:3} * {x:3}) % 23 = {x*x:5} % 23 = {h:2}")


def analyze_hash_properties() -> None:
    """Analysiert mathematische Eigenschaften der Hashfunktion."""
    print("\n" + "=" * 60)
    print("Mathematische Eigenschaften von h(x) = (x * x) % 23")
    print("=" * 60)

    # Quadratische Reste modulo 23
    print("\nQuadratische Reste modulo 23:")
    print("(Welche Werte können als (x²) % 23 auftreten?)")

    squares_mod_23 = set()
    for x in range(23):
        square_mod = (x * x) % 23
        squares_mod_23.add(square_mod)

    print(f"\nMögliche Hash-Werte: {sorted(squares_mod_23)}")
    print(f"Anzahl möglicher Hash-Werte: {len(squares_mod_23)}/23")
    print(f"Nicht erreichbare Indizes: {sorted(set(range(23)) - squares_mod_23)}")

    print("\nProblem:")
    print("  Die Hashfunktion kann nur 12 von 23 möglichen Indizes erzeugen!")
    print("  Das bedeutet, dass 11 Indizes (47.8%) niemals genutzt werden.")
    print("  Dies führt zu:")
    print("    - Erhöhter Kollisionswahrscheinlichkeit")
    print("    - Ineffizienter Speichernutzung")
    print("    - Schlechterer Performance")


def suggest_better_hash_function() -> None:
    """Schlägt bessere Hashfunktionen vor und vergleicht sie."""
    print("\n" + "=" * 60)
    print("Vorschlag für bessere Hashfunktionen")
    print("=" * 60)

    capacity = 23
    value_range = range(0, 201)

    # Alternative 1: Einfache Modulo-Funktion
    def hash_simple(x: int) -> int:
        return x % capacity

    # Alternative 2: Multiplikative Hashfunktion
    def hash_multiplicative(x: int) -> int:
        A = 0.6180339887  # (√5 - 1) / 2 (goldener Schnitt)
        return int(capacity * ((x * A) % 1))

    # Alternative 3: Kombinierte Funktion
    def hash_combined(x: int) -> int:
        return (x * 31 + 17) % capacity

    print("\n1. Einfache Modulo-Funktion: h(x) = x % 23")
    print("   Vorteile:")
    print("     + Sehr einfach und schnell")
    print("     + Nutzt alle Indizes gleichmässig")
    print("     + Gute Verteilung bei sequentiellen Werten")
    print("   Nachteile:")
    print("     - Kann bei bestimmten Mustern zu Clustering führen")

    hash_values_simple = [hash_simple(x) for x in value_range]
    dist_simple = Counter(hash_values_simple)
    print(f"   Genutzte Indizes: {len(dist_simple)}/23")
    print(f"   Max. Kollisionen: {max(dist_simple.values())}")

    print("\n2. Multiplikative Hashfunktion: h(x) = ⌊23 * ((x * A) mod 1)⌋")
    print("   mit A = (√5 - 1) / 2 ≈ 0.618 (goldener Schnitt)")
    print("   Vorteile:")
    print("     + Sehr gute Verteilung")
    print("     + Unabhängig von Mustern in den Daten")
    print("     + Theoretisch fundiert")
    print("   Nachteile:")
    print("     - Etwas komplexer zu berechnen")
    print("     - Benötigt Gleitkomma-Arithmetik")

    hash_values_mult = [hash_multiplicative(x) for x in value_range]
    dist_mult = Counter(hash_values_mult)
    print(f"   Genutzte Indizes: {len(dist_mult)}/23")
    print(f"   Max. Kollisionen: {max(dist_mult.values())}")

    print("\n3. Kombinierte Funktion: h(x) = (x * 31 + 17) % 23")
    print("   Vorteile:")
    print("     + Gute Verteilung")
    print("     + Schnell zu berechnen")
    print("     + Nutzt alle Indizes")
    print("   Nachteile:")
    print("     - Parameter müssen sorgfältig gewählt werden")

    hash_values_comb = [hash_combined(x) for x in value_range]
    dist_comb = Counter(hash_values_comb)
    print(f"   Genutzte Indizes: {len(dist_comb)}/23")
    print(f"   Max. Kollisionen: {max(dist_comb.values())}")

    print("\n" + "=" * 60)
    print("EMPFEHLUNG:")
    print("=" * 60)
    print("Für den gegebenen Anwendungsfall (Werte 0-200, Tabellengrösse 23)")
    print("ist die einfache Modulo-Funktion h(x) = x % 23 am besten geeignet:")
    print()
    print("  ✓ Nutzt alle 23 Indizes gleichmässig")
    print("  ✓ Sehr schnelle Berechnung")
    print("  ✓ Einfach zu verstehen und zu implementieren")
    print("  ✓ Minimale Kollisionen bei gleichverteilten Eingabewerten")


# ============================================================================
# Testfälle
# ============================================================================


def test_part_a() -> None:
    """Test für Teil a: Einfügen von Werten."""
    print("=" * 60)
    print("TEIL A: EINFÜGEN VON WERTEN MIT QUADRATISCHEM SONDIEREN")
    print("=" * 60)

    # Erstelle Hashtabelle und füge initiale Werte ein
    ht = QuadraticProbingHashTable(capacity=23)

    # Initiale Werte: [25, 48, 71, 94] an Positionen [2, 8, 15, 20]
    print("\nInitiale Werte:")
    print("  25 → Index 2")
    print("  48 → Index 8")
    print("  71 → Index 15")
    print("  94 → Index 20")

    ht.table[2] = 25
    ht.table[8] = 48
    ht.table[15] = 71
    ht.table[20] = 94
    ht.size = 4

    print("\nInitialer Zustand:")
    ht.display()

    # Füge 63 ein
    print("\n" + "=" * 60)
    print("EINFÜGEN VON WERT: 63")
    print("=" * 60)
    final_index_63, probed_indices_63 = ht.insert(63, verbose=True)
    print(f"\n{'='*60}")
    print(f"ERGEBNIS: Wert 63 wurde an Index {final_index_63} eingefügt")
    print(f"Probierte Indizes: {probed_indices_63}")
    print(f"{'='*60}")
    ht.display()

    # Füge 116 ein
    print("\n" + "=" * 60)
    print("EINFÜGEN VON WERT: 116")
    print("=" * 60)
    final_index_116, probed_indices_116 = ht.insert(116, verbose=True)
    print(f"\n{'='*60}")
    print(f"ERGEBNIS: Wert 116 wurde an Index {final_index_116} eingefügt")
    print(f"Probierte Indizes: {probed_indices_116}")
    print(f"{'='*60}")
    ht.display()

    # Zusammenfassung
    print("\n" + "=" * 60)
    print("ZUSAMMENFASSUNG TEIL A")
    print("=" * 60)
    print("\n✓ Wert 63:")
    print(f"  - Initialer Hash: h(63) = {ht.hash_function(63)}")
    print(f"  - Finaler Index: {final_index_63}")
    print(f"  - Anzahl Versuche: {len(probed_indices_63)}")
    print("\n✓ Wert 116:")
    print(f"  - Initialer Hash: h(116) = {ht.hash_function(116)}")
    print(f"  - Finaler Index: {final_index_116}")
    print(f"  - Anzahl Versuche: {len(probed_indices_116)}")


def test_part_b() -> None:
    """Test für Teil b: Analyse der Hashfunktion."""
    print("\n" + "=" * 60)
    print("TEIL B: ANALYSE DER HASHFUNKTION")
    print("=" * 60)

    ht = QuadraticProbingHashTable(capacity=23)

    # Analysiere die Verteilung
    analyze_hash_function(ht.hash_function, 23, range(0, 201))

    # Analysiere mathematische Eigenschaften
    analyze_hash_properties()

    # Schlage bessere Alternativen vor
    suggest_better_hash_function()


def verify_initial_positions() -> None:
    """Verifiziert die initialen Positionen der gegebenen Werte."""
    print("\n" + "=" * 60)
    print("VERIFIKATION DER INITIALEN POSITIONEN")
    print("=" * 60)

    ht = QuadraticProbingHashTable(capacity=23)

    values = [25, 48, 71, 94]
    expected_positions = [2, 8, 15, 20]

    print("\nÜberprüfung der gegebenen Positionen:")
    for value, expected_pos in zip(values, expected_positions, strict=False):
        calculated_pos = ht.hash_function(value)
        match = "✓" if calculated_pos == expected_pos else "✗"
        print(
            f"  h({value:3}) = ({value:3}²) % 23 = {value*value:5} % 23 = {calculated_pos:2} (erwartet: {expected_pos:2}) {match}"
        )


def run_all_tests() -> None:
    """Führt alle Tests aus."""
    print("\n" + "=" * 70)
    print(" " * 15 + "HASHTABELLEN-ÜBUNG")
    print(" " * 10 + "Quadratisches Sondieren")
    print("=" * 70)

    # Verifiziere initiale Positionen
    verify_initial_positions()

    # Teil a
    test_part_a()

    # Teil b
    test_part_b()

    print("\n" + "=" * 70)
    print(" " * 20 + "✓ ÜBUNG ABGESCHLOSSEN")
    print("=" * 70)


# ============================================================================
# Zusätzliche Erklärungen und Lösungshinweise
# ============================================================================

"""
DETAILLIERTE LÖSUNG FÜR TEIL A:

Einfügen von Wert 63:
---------------------
1. Berechne h(63) = (63 * 63) % 23 = 3969 % 23 = 11
2. Prüfe Index 11: frei → Einfügen bei Index 11 ✓

Einfügen von Wert 116:
----------------------
1. Berechne h(116) = (116 * 116) % 23 = 13456 % 23 = 15
2. Prüfe Index 15: belegt (Wert 71) → Kollision!
3. Quadratisches Sondieren:
   - Versuch 1 (i=1): (15 + 1²) % 23 = 16 % 23 = 16 → frei ✓
4. Einfügen bei Index 16


DETAILLIERTE LÖSUNG FÜR TEIL B:

Probleme der Hashfunktion h(x) = (x * x) % 23:
-----------------------------------------------

1. EINGESCHRÄNKTER WERTEBEREICH:
   - Die Funktion kann nur 12 von 23 möglichen Indizes erzeugen
   - Mögliche Werte: {0, 1, 2, 3, 4, 6, 8, 9, 12, 13, 16, 18}
   - Nicht erreichbar: {5, 7, 10, 11, 14, 15, 17, 19, 20, 21, 22}
   - Grund: Quadratische Reste modulo 23

2. ERHÖHTE KOLLISIONSWAHRSCHEINLICHKEIT:
   - Da nur 52% der Indizes genutzt werden, sind Kollisionen häufiger
   - Bei 201 Werten (0-200) und nur 12 nutzbaren Indizes gibt es
     durchschnittlich 201/12 ≈ 16.75 Werte pro Index

3. INEFFIZIENTE SPEICHERNUTZUNG:
   - Fast die Hälfte der Tabelle bleibt ungenutzt
   - Verschwendung von Speicherplatz

4. SCHLECHTERE PERFORMANCE:
   - Mehr Kollisionen → mehr Sondierungsschritte
   - Längere Suchzeiten

BESSERE ALTERNATIVE:
--------------------
h(x) = x % 23

Vorteile:
  ✓ Nutzt alle 23 Indizes gleichmässig
  ✓ Minimale Kollisionen bei gleichverteilten Werten
  ✓ Sehr schnelle Berechnung
  ✓ Einfach zu verstehen

Bei 201 Werten (0-200) und 23 Indizes:
  - Durchschnittlich 201/23 ≈ 8.74 Werte pro Index
  - Deutlich besser als 16.75 bei der quadratischen Funktion
"""

if __name__ == "__main__":
    run_all_tests()
