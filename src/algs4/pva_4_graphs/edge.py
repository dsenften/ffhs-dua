"""Ungerichtete Kante mit Gewicht.

Eine ungerichtete Kante mit Gewicht für ungerichtete gewichtete Graphen.
Wird in Minimum Spanning Tree (MST) Algorithmen verwendet.

Beispiel:
    >>> e = Edge(0, 1, 0.5)
    >>> e.either()
    0
    >>> e.other(0)
    1
    >>> e < Edge(0, 2, 0.6)
    True
"""


class Edge:
    """Eine ungerichtete Kante mit Gewicht."""

    def __init__(self, v: int, w: int, weight: float) -> None:
        """Initialisiert eine ungerichtete Kante.

        Args:
            v: Erster Knoten.
            w: Zweiter Knoten.
            weight: Kantengewicht.

        Raises:
            ValueError: Wenn das Gewicht negativ ist.
        """
        if weight < 0:
            raise ValueError("Kantengewicht darf nicht negativ sein")
        self.v = v
        self.w = w
        self.weight = weight

    def __str__(self) -> str:
        """Gibt die Kante als String zurück."""
        return f"{self.v}-{self.w} {self.weight:.5f}"

    def __lt__(self, other: "Edge") -> bool:
        """Vergleicht zwei Kanten nach Gewicht."""
        return self.weight < other.weight

    def __gt__(self, other: "Edge") -> bool:
        """Vergleicht zwei Kanten nach Gewicht."""
        return self.weight > other.weight

    def either(self) -> int:
        """Gibt einen der beiden Knoten zurück.

        Returns:
            Der erste Knoten der Kante.
        """
        return self.v

    def other(self, v: int) -> int:
        """Gibt den anderen Knoten zurück.

        Args:
            v: Ein Knoten der Kante.

        Returns:
            Der andere Knoten der Kante.

        Raises:
            ValueError: Wenn v nicht Teil der Kante ist.
        """
        if v == self.v:
            return self.w
        elif v == self.w:
            return self.v
        else:
            raise ValueError(f"Knoten {v} ist nicht Teil dieser Kante")
