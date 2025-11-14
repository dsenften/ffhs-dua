"""Gerichtete Kante für gewichtete Graphen.

Dieses Modul enthält die DirectedEdge-Klasse, die eine gerichtete Kante
mit Gewicht in einem gewichteten Digraph darstellt.

Beispiele:
    >>> edge = DirectedEdge(0, 1, 0.5)
    >>> edge.From()
    0
    >>> edge.To()
    1
    >>> edge.weight
    0.5
"""


class DirectedEdge:
    """Eine gerichtete Kante mit Gewicht.

    Diese Klasse repräsentiert eine gerichtete Kante von Knoten v zu Knoten w
    mit einem zugeordneten Gewicht. Sie wird in gewichteten Digraphen verwendet.

    Attribute:
        v (int): Der Startknoten der Kante
        w (int): Der Endknoten der Kante
        weight (float): Das Gewicht der Kante
    """

    def __init__(self, v: int, w: int, weight: float) -> None:
        """Initialisiert eine neue gerichtete Kante.

        Args:
            v: Der Startknoten
            w: Der Endknoten
            weight: Das Gewicht der Kante

        Raises:
            ValueError: Wenn das Gewicht negativ ist
        """
        if weight < 0:
            raise ValueError("Kantengewicht darf nicht negativ sein")
        self.v = v
        self.w = w
        self.weight = weight

    def From(self) -> int:
        """Gibt den Startknoten der Kante zurück.

        Returns:
            Der Startknoten (v)
        """
        return self.v

    def To(self) -> int:
        """Gibt den Endknoten der Kante zurück.

        Returns:
            Der Endknoten (w)
        """
        return self.w

    def __str__(self) -> str:
        """Gibt eine String-Darstellung der Kante zurück.

        Returns:
            String im Format "v->w weight"
        """
        return f"{self.v}->{self.w} {self.weight:.5f}"

    def __repr__(self) -> str:
        """Gibt eine detaillierte String-Darstellung zurück."""
        return f"DirectedEdge({self.v}, {self.w}, {self.weight})"

