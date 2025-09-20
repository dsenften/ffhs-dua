"""Union-Find (Disjoint-Set) - Datenstruktur für dynamische Konnektivität

Das UF-Modul implementiert verschiedene Versionen der Union-Find-Datenstruktur
(auch bekannt als Disjoint-Sets-Datentyp). Es unterstützt die union- und find-
Operationen sowie eine connected-Operation zur Bestimmung, ob zwei Knoten in
der gleichen Komponente sind, und eine count-Operation, die die Gesamtzahl
der Komponenten zurückgibt.

Die Union-Find-Datenstruktur modelliert Konnektivität zwischen einer Menge
von n Knoten, nummeriert von 0 bis n-1. Die "ist-verbunden-mit"-Relation
muss eine Äquivalenzrelation sein:
    * Reflexiv: p ist mit p verbunden.
    * Symmetrisch: Wenn p mit q verbunden ist, dann ist q mit p verbunden.
    * Transitiv: Wenn p mit q verbunden und q mit r verbunden ist, dann
                 ist p mit r verbunden.

Implementierte Varianten:
- UF: Optimierte Version mit Weighted Quick Union by Rank und Path Compression
- QuickUnionUF: Einfache Quick Union Implementation
- WeightedQuickUnionUF: Weighted Quick Union by Size (ohne Path Compression)
- QuickFindUF: Quick Find Implementation

Basiert auf Kapitel 1.5 von "Algorithms, 4th Edition" von Robert Sedgewick und Kevin Wayne.
"""


class UF:
    """Union-Find mit Weighted Quick Union by Rank und Path Compression

    Diese Implementation verwendet Weighted Quick Union by Rank mit Path Compression
    durch Halbierung. Die Initialisierung einer Datenstruktur mit n Knoten benötigt
    lineare Zeit. Danach benötigen die union-, find- und connected-Operationen
    logarithmische Zeit (im schlechtesten Fall) und die count-Operation konstante Zeit.
    Die amortisierte Zeit pro union-, find- und connected-Operation hat inverse
    Ackermann-Komplexität.

    Diese Implementierung ist die effizienteste der verfügbaren Union-Find-Varianten.

    Zeitkomplexität:
    - Konstruktor: O(n)
    - union(p, q): O(α(n)) amortisiert
    - find(p): O(α(n)) amortisiert
    - connected(p, q): O(α(n)) amortisiert
    - count(): O(1)

    Wobei α(n) die inverse Ackermann-Funktion ist, die für praktische Zwecke
    als konstant betrachtet werden kann.
    """

    def __init__(self, n: int) -> None:
        """Initialisiert eine leere Union-Find-Datenstruktur mit n Knoten.

        Jeder Knoten (0 bis n-1) befindet sich anfangs in seiner eigenen Komponente.

        Args:
            n: Anzahl der Knoten (muss positiv sein)

        Raises:
            ValueError: wenn n <= 0
        """
        if n <= 0:
            raise ValueError("Anzahl der Knoten muss positiv sein")
        self._count = n
        self._parent: list[int] = list(range(n))
        self._rank: list[int] = [0] * n

    def _validate(self, p: int) -> None:
        """Validiert, dass p ein gültiger Knotenindex ist."""
        n = len(self._parent)
        if p < 0 or p >= n:
            raise ValueError(f"Index {p} ist nicht zwischen 0 und {n - 1}")

    def union(self, p: int, q: int) -> None:
        """Verbindet die Komponenten, die die Knoten p und q enthalten.

        Falls beide Knoten bereits in derselben Komponente sind, wird nichts getan.
        Andernfalls werden die beiden Komponenten verschmolzen, wobei der Baum
        mit kleinerem Rang unter den Baum mit grösserem Rang gehaengt wird.

        Args:
            p: Erster Knoten
            q: Zweiter Knoten

        Raises:
            ValueError: wenn p oder q ungültige Indizes sind
        """
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return

        # Haenge Wurzel mit kleinerem Rang unter Wurzel mit grösserem Rang
        if self._rank[root_p] < self._rank[root_q]:
            self._parent[root_p] = root_q
        elif self._rank[root_p] > self._rank[root_q]:
            self._parent[root_q] = root_p
        else:
            # Bei gleichem Rang: root_q unter root_p und erhöhe Rang von root_p
            self._parent[root_q] = root_p
            self._rank[root_p] += 1

        self._count -= 1

    def find(self, p: int) -> int:
        """Findet die Wurzel der Komponente, die den Knoten p enthält.

        Verwendet Path Compression durch Halbierung für bessere Performance.
        Der Komponenten-Identifier ist die Wurzel des Baums.

        Args:
            p: Knoten, dessen Komponenten-Wurzel gesucht wird

        Returns:
            int: Komponenten-Identifier (Wurzel des Baums)

        Raises:
            ValueError: wenn p ein ungültiger Index ist
        """
        self._validate(p)
        while p != self._parent[p]:
            # Path Compression durch Halbierung: jeder Knoten zeigt auf seinen Grosselternknoten
            self._parent[p] = self._parent[self._parent[p]]
            p = self._parent[p]
        return p

    def connected(self, p: int, q: int) -> bool:
        """Prüft, ob zwei Knoten in derselben Komponente sind.

        Args:
            p: Erster Knoten
            q: Zweiter Knoten

        Returns:
            bool: True wenn beide Knoten in derselben Komponente sind, False sonst

        Raises:
            ValueError: wenn p oder q ungültige Indizes sind
        """
        return self.find(p) == self.find(q)

    def count(self) -> int:
        """Gibt die Anzahl der Komponenten zurück.

        Returns:
            int: Aktuelle Anzahl der separaten Komponenten
        """
        return self._count

    def is_empty(self) -> bool:
        """Prüft, ob die Union-Find-Struktur leer ist.

        Returns:
            bool: True wenn keine Knoten vorhanden sind
        """
        return len(self._parent) == 0

    def size(self) -> int:
        """Gibt die Gesamtanzahl der Knoten zurück.

        Returns:
            int: Gesamtanzahl der Knoten in der Datenstruktur
        """
        return len(self._parent)


class QuickUnionUF:
    """Quick Union - Einfache Union-Find Implementation

    Diese Implementation verwendet Quick Union ohne Optimierungen. Die Initialisierung
    einer Datenstruktur mit n Knoten benötigt lineare Zeit. Die union-, find- und
    connected-Operationen können im schlechtesten Fall lineare Zeit benötigen.

    Zeitkomplexität:
    - Konstruktor: O(n)
    - union(p, q): O(n) im schlechtesten Fall
    - find(p): O(n) im schlechtesten Fall
    - connected(p, q): O(n) im schlechtesten Fall
    - count(): O(1)
    """

    def __init__(self, n: int) -> None:
        """Initialisiert eine leere Union-Find-Datenstruktur mit n Knoten.

        Args:
            n: Anzahl der Knoten (muss positiv sein)

        Raises:
            ValueError: wenn n <= 0
        """
        if n <= 0:
            raise ValueError("Anzahl der Knoten muss positiv sein")
        self._count = n
        self._parent: list[int] = list(range(n))

    def _validate(self, p: int) -> None:
        """Validiert, dass p ein gültiger Knotenindex ist."""
        n = len(self._parent)
        if p < 0 or p >= n:
            raise ValueError(f"Index {p} ist nicht zwischen 0 und {n - 1}")

    def union(self, p: int, q: int) -> None:
        """Verbindet die Komponenten, die die Knoten p und q enthalten.

        Args:
            p: Erster Knoten
            q: Zweiter Knoten

        Raises:
            ValueError: wenn p oder q ungültige Indizes sind
        """
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return

        self._parent[root_p] = root_q
        self._count -= 1

    def find(self, p: int) -> int:
        """Findet die Wurzel der Komponente, die den Knoten p enthält.

        Args:
            p: Knoten, dessen Komponenten-Wurzel gesucht wird

        Returns:
            int: Komponenten-Identifier (Wurzel des Baums)

        Raises:
            ValueError: wenn p ein ungültiger Index ist
        """
        self._validate(p)
        while p != self._parent[p]:
            p = self._parent[p]
        return p

    def connected(self, p: int, q: int) -> bool:
        """Prüft, ob zwei Knoten in derselben Komponente sind.

        Args:
            p: Erster Knoten
            q: Zweiter Knoten

        Returns:
            bool: True wenn beide Knoten in derselben Komponente sind, False sonst

        Raises:
            ValueError: wenn p oder q ungültige Indizes sind
        """
        return self.find(p) == self.find(q)

    def count(self) -> int:
        """Gibt die Anzahl der Komponenten zurück.

        Returns:
            int: Aktuelle Anzahl der separaten Komponenten
        """
        return self._count


class WeightedQuickUnionUF:
    """Weighted Quick Union - Union-Find nach Grösse gewichtet

    Diese Implementation verwendet Weighted Quick Union by Size (ohne Path Compression).
    Die Initialisierung einer Datenstruktur mit n Knoten benötigt lineare Zeit.
    Die union-, find- und connected-Operationen benötigen logarithmische Zeit
    im schlechtesten Fall.

    Zeitkomplexität:
    - Konstruktor: O(n)
    - union(p, q): O(log n)
    - find(p): O(log n)
    - connected(p, q): O(log n)
    - count(): O(1)
    """

    def __init__(self, n: int) -> None:
        """Initialisiert eine leere Union-Find-Datenstruktur mit n Knoten.

        Args:
            n: Anzahl der Knoten (muss positiv sein)

        Raises:
            ValueError: wenn n <= 0
        """
        if n <= 0:
            raise ValueError("Anzahl der Knoten muss positiv sein")
        self._count = n
        self._parent: list[int] = list(range(n))
        self._size: list[int] = [1] * n

    def _validate(self, p: int) -> None:
        """Validiert, dass p ein gültiger Knotenindex ist."""
        n = len(self._parent)
        if p < 0 or p >= n:
            raise ValueError(f"Index {p} ist nicht zwischen 0 und {n - 1}")

    def union(self, p: int, q: int) -> None:
        """Verbindet die Komponenten, die die Knoten p und q enthalten.

        Haengt den kleineren Baum unter den grösseren Baum.

        Args:
            p: Erster Knoten
            q: Zweiter Knoten

        Raises:
            ValueError: wenn p oder q ungültige Indizes sind
        """
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return

        # Haenge Wurzel mit kleinerer Grösse unter Wurzel mit grösserer Grösse
        if self._size[root_p] < self._size[root_q]:
            small, large = root_p, root_q
        else:
            small, large = root_q, root_p

        self._parent[small] = large
        self._size[large] += self._size[small]
        self._count -= 1

    def find(self, p: int) -> int:
        """Findet die Wurzel der Komponente, die den Knoten p enthält.

        Args:
            p: Knoten, dessen Komponenten-Wurzel gesucht wird

        Returns:
            int: Komponenten-Identifier (Wurzel des Baums)

        Raises:
            ValueError: wenn p ein ungültiger Index ist
        """
        self._validate(p)
        while p != self._parent[p]:
            p = self._parent[p]
        return p

    def connected(self, p: int, q: int) -> bool:
        """Prüft, ob zwei Knoten in derselben Komponente sind.

        Args:
            p: Erster Knoten
            q: Zweiter Knoten

        Returns:
            bool: True wenn beide Knoten in derselben Komponente sind, False sonst

        Raises:
            ValueError: wenn p oder q ungültige Indizes sind
        """
        return self.find(p) == self.find(q)

    def count(self) -> int:
        """Gibt die Anzahl der Komponenten zurück.

        Returns:
            int: Aktuelle Anzahl der separaten Komponenten
        """
        return self._count


class QuickFindUF:
    """Quick Find - Union-Find mit schneller Find-Operation

    Diese Implementation verwendet Quick Find. Die Initialisierung einer Datenstruktur
    mit n Knoten benötigt lineare Zeit. Die find-, connected- und count-Operationen
    benötigen konstante Zeit, aber die union-Operation benötigt lineare Zeit.

    Zeitkomplexität:
    - Konstruktor: O(n)
    - union(p, q): O(n)
    - find(p): O(1)
    - connected(p, q): O(1)
    - count(): O(1)
    """

    def __init__(self, n: int) -> None:
        """Initialisiert eine leere Union-Find-Datenstruktur mit n Knoten.

        Args:
            n: Anzahl der Knoten (muss positiv sein)

        Raises:
            ValueError: wenn n <= 0
        """
        if n <= 0:
            raise ValueError("Anzahl der Knoten muss positiv sein")
        self._count = n
        self._id: list[int] = list(range(n))

    def _validate(self, p: int) -> None:
        """Validiert, dass p ein gültiger Knotenindex ist."""
        n = len(self._id)
        if p < 0 or p >= n:
            raise ValueError(f"Index {p} ist nicht zwischen 0 und {n - 1}")

    def union(self, p: int, q: int) -> None:
        """Verbindet die Komponenten, die die Knoten p und q enthalten.

        Ändert alle Knoten mit der ID von p zur ID von q.

        Args:
            p: Erster Knoten
            q: Zweiter Knoten

        Raises:
            ValueError: wenn p oder q ungültige Indizes sind
        """
        self._validate(p)
        self._validate(q)

        p_id = self._id[p]  # Für Korrektheit notwendig
        q_id = self._id[q]  # Um Array-Zugriffe zu reduzieren

        # p und q sind bereits in derselben Komponente
        if p_id == q_id:
            return

        # Ändere alle Knoten mit p_id zu q_id
        for i in range(len(self._id)):
            if self._id[i] == p_id:
                self._id[i] = q_id
        self._count -= 1

    def find(self, p: int) -> int:
        """Findet die Komponenten-ID des Knotens p.

        Args:
            p: Knoten, dessen Komponenten-ID gesucht wird

        Returns:
            int: Komponenten-Identifier

        Raises:
            ValueError: wenn p ein ungültiger Index ist
        """
        self._validate(p)
        return self._id[p]

    def connected(self, p: int, q: int) -> bool:
        """Prüft, ob zwei Knoten in derselben Komponente sind.

        Args:
            p: Erster Knoten
            q: Zweiter Knoten

        Returns:
            bool: True wenn beide Knoten in derselben Komponente sind, False sonst

        Raises:
            ValueError: wenn p oder q ungültige Indizes sind
        """
        self._validate(p)
        self._validate(q)
        return self._id[p] == self._id[q]

    def count(self) -> int:
        """Gibt die Anzahl der Komponenten zurück.

        Returns:
            int: Aktuelle Anzahl der separaten Komponenten
        """
        return self._count


if __name__ == "__main__":
    """Beispielprogramm für Union-Find-Datenstrukturen.

    Liest eine Folge von Knotenpaaren von der Standardeingabe und verbindet sie,
    falls sie noch nicht in derselben Komponente sind.
    """
    print("Union-Find Demo")
    print("Geben Sie die Anzahl der Knoten ein:")

    try:
        n = int(input())
        if n <= 0:
            print("Fehler: Anzahl der Knoten muss positiv sein")
            exit(1)

        uf = UF(n)
        print(f"Union-Find-Struktur mit {n} Knoten initialisiert")
        print("Geben Sie Knotenpaare ein (p q), leere Zeile zum Beenden:")

        while True:
            line = input().strip()
            if not line:
                break

            try:
                parts = line.split()
                if len(parts) != 2:
                    print("Fehler: Geben Sie genau zwei Zahlen ein")
                    continue

                p, q = int(parts[0]), int(parts[1])

                if uf.connected(p, q):
                    print(f"{p} und {q} sind bereits verbunden")
                else:
                    uf.union(p, q)
                    print(f"{p} {q} verbunden")

            except ValueError as e:
                print(f"Fehler: {e}")
            except Exception as e:
                print(f"Unerwarteter Fehler: {e}")

        print(f"Anzahl der Komponenten: {uf.count()}")

    except KeyboardInterrupt:
        print("\nProgramm beendet")
    except Exception as e:
        print(f"Fehler: {e}")
