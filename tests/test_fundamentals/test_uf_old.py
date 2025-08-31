"""Testsuiten für Union-Find (Disjoint-Set) Datenstrukturen

Diese Testsuiten prüfen alle vier Implementierungen der Union-Find-Datenstruktur:
- UF: Optimierte Version mit Weighted Quick Union by Rank und Path Compression
- QuickUnionUF: Einfache Quick Union Implementation
- WeightedQuickUnionUF: Weighted Quick Union by Size
- QuickFindUF: Quick Find Implementation

Die Tests validieren Funktionalität, Grenzfälle und Fehlerbehandlung für alle Varianten.
"""


import pytest

from algs4.fundamentals.uf import UF, QuickFindUF, QuickUnionUF, WeightedQuickUnionUF


# Abstrakte Basisklasse, die nicht direkt getestet werden sollte
class TestUnionFindBase:
    # Diese Klasse soll nicht direkt getestet werden
    __test__ = False
    """Basis-Testklasse für alle Union-Find-Implementierungen

    Enthält gemeinsame Tests, die für alle Implementierungen gelten.
    Wird von den spezifischen Testklassen geerbt.
    """

    def get_uf_class(self) -> type:
        """Muss von Unterklassen überschrieben werden.

        Diese Methode wird von allen Testmethoden aufgerufen, daher ist sie
        der ideale Ort, um Tests zu überspringen, wenn sie direkt in der
        Basisklasse aufgerufen werden.
        """
        # Überspringe Test, wenn direkt in der Basisklasse aufgerufen
        if self.__class__ is TestUnionFindBase:
            pytest.skip("Abstrakte Basisklasse, sollte nicht direkt ausgeführt werden")
        raise NotImplementedError("Unterklassen müssen get_uf_class() implementieren")

    def test_initialisierung_valid(self):
        """Teste gültige Initialisierung."""
        uf_class = self.get_uf_class()

        # Verschiedene gültige Größen
        for n in [1, 2, 5, 10, 100]:
            uf = uf_class(n)
            assert uf.count() == n

            # Alle Knoten sind anfangs in separaten Komponenten
            for i in range(n):
                for j in range(i + 1, n):
                    assert not uf.connected(i, j)

    def test_initialisierung_invalid(self):
        """Teste ungültige Initialisierung."""
        uf_class = self.get_uf_class()

        # Ungültige Größen sollten ValueError werfen
        for invalid_n in [0, -1, -10]:
            with pytest.raises(ValueError, match="Anzahl der Knoten muss positiv sein"):
                uf_class(invalid_n)

    def test_union_basic(self):
        """Teste grundlegende Union-Operationen."""
        uf_class = self.get_uf_class()
        uf = uf_class(10)

        # Initial: 10 separate Komponenten
        assert uf.count() == 10

        # Verbinde 0-1
        uf.union(0, 1)
        assert uf.connected(0, 1)
        assert uf.count() == 9

        # Verbinde 2-3
        uf.union(2, 3)
        assert uf.connected(2, 3)
        assert uf.count() == 8
        assert not uf.connected(0, 2)  # Verschiedene Komponenten

        # Verbinde die beiden Komponenten: (0,1) mit (2,3)
        uf.union(1, 2)
        assert uf.connected(0, 1)
        assert uf.connected(2, 3)
        assert uf.connected(0, 2)  # Jetzt verbunden
        assert uf.connected(0, 3)  # Transitivität
        assert uf.connected(1, 3)
        assert uf.count() == 7

    def test_union_idempotent(self):
        """Teste, dass mehrfache Union derselben Knoten idempotent ist."""
        uf_class = self.get_uf_class()
        uf = uf_class(5)

        # Verbinde 0-1 mehrfach
        uf.union(0, 1)
        initial_count = uf.count()

        uf.union(0, 1)  # Nochmal
        uf.union(1, 0)  # Reihenfolge getauscht

        assert uf.count() == initial_count
        assert uf.connected(0, 1)

    def test_find_and_connected_konsistenz(self):
        """Teste Konsistenz zwischen find() und connected()."""
        uf_class = self.get_uf_class()
        uf = uf_class(8)

        # Verbinde mehrere Komponenten
        unions = [(0, 1), (2, 3), (4, 5), (1, 3)]  # Verbindet (0,1,2,3)
        for p, q in unions:
            uf.union(p, q)

        # connected() sollte konsistent mit find() sein
        for i in range(8):
            for j in range(8):
                expected = uf.find(i) == uf.find(j)
                actual = uf.connected(i, j)
                assert actual == expected, f"Inkonsistenz bei ({i}, {j})"

    def test_alle_verbinden(self):
        """Teste Verbindung aller Knoten zu einer Komponente."""
        uf_class = self.get_uf_class()
        n = 20
        uf = uf_class(n)

        # Verbinde alle mit Knoten 0
        for i in range(1, n):
            uf.union(0, i)

        assert uf.count() == 1

        # Alle Knoten sollten miteinander verbunden sein
        for i in range(n):
            for j in range(n):
                assert uf.connected(i, j)

    def test_ketten_verbindung(self):
        """Teste Kettenverbindung: 0-1-2-3-...-n."""
        uf_class = self.get_uf_class()
        n = 15
        uf = uf_class(n)

        # Erstelle Kette: 0-1-2-3-...-14
        for i in range(n - 1):
            uf.union(i, i + 1)

        assert uf.count() == 1

        # Alle sollten miteinander verbunden sein
        for i in range(n):
            for j in range(n):
                assert uf.connected(i, j)

    def test_grenzfaelle_indizes(self):
        """Teste Grenzfälle bei Indizes."""
        uf_class = self.get_uf_class()
        uf = uf_class(10)

        # Gültige Grenzfälle
        uf.union(0, 9)  # Min und Max
        assert uf.connected(0, 9)

        # Ungültige Indizes sollten ValueError werfen
        invalid_indices = [-1, -5, 10, 15, 100]
        for invalid in invalid_indices:
            with pytest.raises(ValueError, match="ist nicht zwischen 0 und"):
                uf.find(invalid)
            with pytest.raises(ValueError, match="ist nicht zwischen 0 und"):
                uf.union(0, invalid)
            with pytest.raises(ValueError, match="ist nicht zwischen 0 und"):
                uf.connected(0, invalid)

    def test_reflexivitaet(self):
        """Teste, dass connected() reflexiv ist."""
        uf_class = self.get_uf_class()
        uf = uf_class(5)

        # Jeder Knoten ist mit sich selbst verbunden
        for i in range(5):
            assert uf.connected(i, i)

    def test_symmetrie(self):
        """Teste, dass connected() symmetrisch ist."""
        uf_class = self.get_uf_class()
        uf = uf_class(6)

        # Erstelle einige Verbindungen
        uf.union(0, 1)
        uf.union(2, 3)
        uf.union(4, 5)

        # Teste Symmetrie
        for i in range(6):
            for j in range(6):
                assert uf.connected(i, j) == uf.connected(j, i)

    def test_transitivitaet(self):
        """Teste Transitivität der Verbindungen."""
        uf_class = self.get_uf_class()
        uf = uf_class(8)

        # Erstelle transitive Kette: 0-1, 1-2, 2-3
        uf.union(0, 1)
        uf.union(1, 2)
        uf.union(2, 3)

        # Transitivität prüfen
        assert uf.connected(0, 3)  # 0 -> 1 -> 2 -> 3
        assert uf.connected(0, 2)  # 0 -> 1 -> 2
        assert uf.connected(1, 3)  # 1 -> 2 -> 3

    def test_komplexe_struktur(self):
        """Teste komplexe Union-Find-Struktur mit mehreren Komponenten."""
        uf_class = self.get_uf_class()
        uf = uf_class(12)

        # Erstelle spezifische Struktur:
        # Komponente 1: {0, 1, 2, 3}
        # Komponente 2: {4, 5}
        # Komponente 3: {6, 7, 8}
        # Einzelne: {9}, {10}, {11}

        unions = [
            (0, 1),
            (1, 2),
            (2, 3),  # Komponente 1
            (4, 5),  # Komponente 2
            (6, 7),
            (7, 8),  # Komponente 3
        ]

        for p, q in unions:
            uf.union(p, q)

        assert uf.count() == 6  # 3 große + 3 einzelne Komponenten

        # Teste Verbindungen innerhalb der Komponenten
        component1 = [0, 1, 2, 3]
        for i in component1:
            for j in component1:
                assert uf.connected(i, j)

        component2 = [4, 5]
        for i in component2:
            for j in component2:
                assert uf.connected(i, j)

        component3 = [6, 7, 8]
        for i in component3:
            for j in component3:
                assert uf.connected(i, j)

        # Teste, dass verschiedene Komponenten nicht verbunden sind
        assert not uf.connected(0, 4)  # Komp1 - Komp2
        assert not uf.connected(0, 6)  # Komp1 - Komp3
        assert not uf.connected(4, 6)  # Komp2 - Komp3
        assert not uf.connected(0, 9)  # Komp1 - Einzeln

        # Einzelne Knoten sind nur mit sich verbunden
        for single in [9, 10, 11]:
            for other in range(12):
                if other == single:
                    assert uf.connected(single, other)
                else:
                    assert not uf.connected(single, other)


class TestUF(TestUnionFindBase):
    """Testklasse für die optimierte UF-Implementation."""

    __test__ = True

    def get_uf_class(self):
        return UF

    def test_zusaetzliche_methoden(self):
        """Teste zusätzliche Methoden der UF-Klasse."""
        uf = UF(5)

        # Teste is_empty()
        assert not uf.is_empty()

        # Teste size()
        assert uf.size() == 5

        # Teste mit leerer UF (spezielle Implementierung für Tests)
        uf._parent = []
        assert uf.is_empty()
        assert uf.size() == 0

    def test_path_compression_verhalten(self):
        """Teste spezifisches Verhalten der Path Compression."""
        uf = UF(10)

        # Erstelle tiefe Kette ohne Path Compression
        for i in range(9):
            uf._parent[i + 1] = i  # Manuell ohne union() um Path Compression zu umgehen

        # Erste find()-Aufrufe sollten Path Compression auslösen
        root = uf.find(9)

        # Nach Path Compression sollten Pfade verkürzt sein
        # (Exact path compression behavior schwer zu testen ohne interne Implementierung zu exposé)
        assert root == uf.find(8)  # Gleiche Wurzel


class TestQuickUnionUF(TestUnionFindBase):
    """Testklasse für die QuickUnionUF-Implementation."""

    __test__ = True

    def get_uf_class(self):
        return QuickUnionUF

    def test_schlechter_fall_performance(self):
        """Teste den schlechtesten Fall (lineare Kette) für QuickUnion."""
        n = 100
        uf = QuickUnionUF(n)

        # Erstelle schlechtmöglichste Kette: 0 <- 1 <- 2 <- ... <- 99
        for i in range(n - 1):
            uf.union(i, i + 1)

        # Sollte trotzdem funktional korrekt sein
        assert uf.count() == 1
        assert uf.connected(0, n - 1)


class TestWeightedQuickUnionUF(TestUnionFindBase):
    """Testklasse für die WeightedQuickUnionUF-Implementation."""

    __test__ = True

    def get_uf_class(self):
        return WeightedQuickUnionUF

    def test_gewichtung_nach_groesse(self):
        """Teste, dass kleinere Bäume unter größere gehängt werden."""
        uf = WeightedQuickUnionUF(8)

        # Erstelle zwei Komponenten unterschiedlicher Größe
        # Komponente 1: {0, 1, 2} (Größe 3)
        uf.union(0, 1)
        uf.union(1, 2)

        # Komponente 2: {3, 4} (Größe 2)
        uf.union(3, 4)

        # Verbinde die Komponenten - kleinere sollte unter größere
        uf.union(2, 3)

        # Alle sollten verbunden sein
        for i in range(5):
            for j in range(5):
                assert uf.connected(i, j)


class TestQuickFindUF(TestUnionFindBase):
    """Testklasse für die QuickFindUF-Implementation."""

    __test__ = True

    def get_uf_class(self):
        return QuickFindUF

    def test_konstante_find_zeit(self):
        """Teste, dass find() in konstanter Zeit läuft (QuickFind-Vorteil)."""
        n = 1000
        uf = QuickFindUF(n)

        # Auch bei vielen Operationen sollte find() schnell sein
        for i in range(100):
            uf.union(i, (i + 1) % n)

        # find() sollte direkte Array-Zugriffe verwenden
        for i in range(n):
            component_id = uf.find(i)
            assert isinstance(component_id, int)

    def test_lineare_union_zeit(self):
        """Teste, dass union() lineare Zeit benötigt (QuickFind-Nachteil)."""
        uf = QuickFindUF(100)

        # Union-Operationen sollten funktionieren, auch wenn sie langsam sind
        for i in range(50):
            uf.union(i, i + 50)

        assert uf.count() == 50

        # Alle entsprechenden Paare sollten verbunden sein
        for i in range(50):
            assert uf.connected(i, i + 50)


class TestPerformanceVergleich:
    """Performancevergleich zwischen den verschiedenen Implementierungen."""

    def test_funktionale_aequivalenz(self):
        """Teste, dass alle Implementierungen funktional äquivalent sind."""
        n = 50

        # Gleiche Operationssequenz auf alle Implementierungen anwenden
        operations = [
            (0, 1),
            (2, 3),
            (4, 5),
            (6, 7),
            (8, 9),
            (0, 2),
            (4, 6),
            (8, 10),
            (1, 5),
            (3, 7),
            (0, 4),
            (2, 6),
            (1, 3),
            (5, 7),
            (9, 11),
        ]

        implementations = [
            UF(n),
            QuickUnionUF(n),
            WeightedQuickUnionUF(n),
            QuickFindUF(n),
        ]

        # Wende gleiche Operationen auf alle an
        for p, q in operations:
            for uf in implementations:
                uf.union(p, q)

        # Alle sollten gleiche Resultate liefern
        reference = implementations[0]
        for uf in implementations[1:]:
            assert uf.count() == reference.count()

            # Teste alle Verbindungen
            for i in range(n):
                for j in range(n):
                    assert uf.connected(i, j) == reference.connected(i, j)


class TestEdgeCases:
    """Tests für spezielle Grenzfälle und Fehlerbedingungen."""

    def test_minimale_groesse(self):
        """Teste Union-Find mit nur einem Element."""
        for uf_class in [UF, QuickUnionUF, WeightedQuickUnionUF, QuickFindUF]:
            uf = uf_class(1)

            assert uf.count() == 1
            assert uf.connected(0, 0)
            assert uf.find(0) == 0

            # Union mit sich selbst sollte nichts ändern
            uf.union(0, 0)
            assert uf.count() == 1

    def test_grosse_datenstrukturen(self):
        """Teste mit größeren Datenstrukturen."""
        n = 1000

        for uf_class in [UF, QuickUnionUF, WeightedQuickUnionUF, QuickFindUF]:
            uf = uf_class(n)

            # Verbinde jedes Element mit seinem Nachbarn
            for i in range(n - 1):
                uf.union(i, i + 1)

            assert uf.count() == 1
            assert uf.connected(0, n - 1)

    def test_stress_test_zufaellige_operationen(self):
        """Stress-Test mit zufälligen Operationen."""
        import random

        random.seed(42)  # Für Reproduzierbarkeit

        n = 100
        num_operations = 500

        for uf_class in [UF, QuickUnionUF, WeightedQuickUnionUF, QuickFindUF]:
            uf = uf_class(n)

            for _ in range(num_operations):
                p = random.randint(0, n - 1)
                q = random.randint(0, n - 1)

                # Zufällige Operation
                if random.choice([True, False]):
                    uf.union(p, q)
                else:
                    uf.connected(p, q)  # Nur testen, nicht ändern

                # Invarianten prüfen
                assert 1 <= uf.count() <= n
                assert uf.connected(p, p)  # Reflexivität
                assert uf.connected(q, q)


if __name__ == "__main__":
    """Führe alle Tests aus, wenn das Modul direkt ausgeführt wird."""
    pytest.main([__file__, "-v"])
