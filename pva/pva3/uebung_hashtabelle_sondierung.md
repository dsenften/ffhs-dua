# Übung: Hashtabellen mit quadratischem Sondieren

## Lernziele

Nach dieser Übung können Sie:

- Hashfunktionen für verschiedene Wertebereiche entwickeln und bewerten
- Quadratisches Sondieren zur Kollisionsbehandlung anwenden
- Die Eigenschaften von Hashfunktionen analysieren
- Probleme bei der Wahl von Hashfunktionen erkennen und Alternativen vorschlagen

## Hintergrund

- **Hashtabellen** sind eine der effizientesten Datenstrukturen für schnellen Zugriff auf Daten. Sie verwenden eine
- **Hashfunktion**, um Schlüssel in Array-Indizes umzuwandeln.

### Hashfunktion

Eine Hashfunktion `h(x)` bildet einen Schlüssel `x` auf einen Index im Bereich `[0, m-1]` ab, wobei `m`
die Grösse der Hashtabelle ist.

**Eigenschaften einer guten Hashfunktion:**

- **Determinismus**: Gleiche Eingabe liefert immer gleichen Hash-Wert
- **Gleichverteilung**: Schlüssel werden gleichmässig über die Tabelle verteilt
- **Effizienz**: Schnelle Berechnung
- **Minimale Kollisionen**: Verschiedene Schlüssel sollten möglichst verschiedene Hash-Werte erzeugen

### Kollisionsbehandlung

Wenn zwei Schlüssel auf denselben Index abgebildet werden, spricht man von einer **Kollision**.
Es gibt verschiedene Strategien zur Kollisionsbehandlung:

1. **Separate Chaining**: Jeder Index enthält eine verkettete Liste
2. **Linear Probing**: Bei Kollision wird linear nach dem nächsten freien Platz gesucht
3. **Quadratisches Sondieren**: Bei Kollision wird quadratisch nach einem freien Platz gesucht

### Quadratisches Sondieren

Beim quadratischen Sondieren wird bei einer Kollision nach folgendem Schema gesucht:

```python
Index = (h(x) + i²) % m
```

wobei `i = 0, 1, 2, 3, ...` die Anzahl der Versuche ist.

**Beispiel:**

- Ursprünglicher Hash-Wert: `h(x) = 5`
- 1. Versuch (i=0): Index = `(5 + 0²) % 23 = 5`
- 2. Versuch (i=1): Index = `(5 + 1²) % 23 = 6`
- 3. Versuch (i=2): Index = `(5 + 3²) % 23 = 9`
- 4. Versuch (i=3): Index = `(5 + 4²) % 23 = 14`
- usw.

## Aufgabenstellung

Sie arbeiten mit einer Hashtabelle mit **23 Plätzen** (Indizes 0 - 22) für Werte zwischen 0 und 200.

Als Hashfunktion wird verwendet:

```python
def h(x):
    return (x * x) % 23
```

**Kollisionen werden mit quadratischem Sondieren behandelt.**

### Teil a: Einfügen von Werten [7 Punkte]

Die Tabelle enthält bereits die Werte `[25, 48, 71, 94]` an den Positionen `[2, 8, 15, 20]`.

**Aufgabe:**
Fügen Sie die Werte **63** und **116** in dieser Reihenfolge ein.

**Zeigen Sie für jeden Wert:**

1. Die Berechnung des initialen Hash-Werts mit `h(x)`
2. Alle Sondierungsschritte bei Kollisionen
3. Den finalen Index, an dem der Wert eingefügt wird

**Hinweis:** Verwenden Sie die Formel `Index = (h(x) + i²) % 23` für das quadratische Sondieren.

### Teil b: Analyse der Hashfunktion [5 Punkte]

**Aufgabe:**

1. Erklären Sie, warum die gewählte Hashfunktion `h(x) = (x * x) % 23` für diesen Anwendungsfall problematisch sein könnte.
2. Schlagen Sie eine bessere Alternative vor und begründen Sie Ihre Wahl.

**Hinweise für die Analyse:**

- Untersuchen Sie die Verteilung der Hash-Werte
- Betrachten Sie verschiedene Eingabewerte und deren Hash-Werte
- Überlegen Sie, ob alle Indizes gleichmässig genutzt werden

## Python-Gerüst

Verwenden Sie die bestehende `LinearProbingHashST`-Klasse aus `src/algs4/pva_3_searching/hashing.py` als Referenz.

```python
from typing import List, Tuple


class QuadraticProbingHashTable:
    """Hashtabelle mit quadratischem Sondieren."""

    def __init__(self, capacity: int = 23) -> None:
        """Initialisiert eine Hashtabelle mit gegebener Kapazität.
        
        Args:
            capacity: Grösse der Hashtabelle (Standard: 23)
        """
        self.capacity = capacity
        self.table: List[int | None] = [None] * capacity
        self.size = 0

    def hash_function(self, x: int) -> int:
        """Berechnet den Hash-Wert für einen Schlüssel.
        
        Args:
            x: Zu hashender Schlüssel
            
        Returns:
            int: Hash-Wert (Index in der Tabelle)
        """
        # TODO: Implementieren Sie die Hashfunktion h(x) = (x * x) % 23
        pass

    def quadratic_probe(self, initial_hash: int, attempt: int) -> int:
        """Berechnet den Index beim quadratischen Sondieren.
        
        Args:
            initial_hash: Initialer Hash-Wert
            attempt: Anzahl der bisherigen Versuche (i)
            
        Returns:
            int: Neuer Index zum Prüfen
        """
        # TODO: Implementieren Sie die Formel (initial_hash + i²) % capacity
        pass

    def insert(self, value: int, verbose: bool = True) -> Tuple[int, List[int]]:
        """Fügt einen Wert in die Hashtabelle ein.
        
        Args:
            value: Einzufügender Wert
            verbose: Wenn True, werden Berechnungsschritte ausgegeben
            
        Returns:
            Tuple[int, List[int]]: (finaler Index, Liste aller probierten Indizes)
        """
        # TODO: Implementieren Sie das Einfügen mit quadratischem Sondieren
        pass

    def display(self) -> None:
        """Zeigt den aktuellen Zustand der Hashtabelle an."""
        print("\nAktueller Zustand der Hashtabelle:")
        print("Index | Wert")
        print("-" * 15)
        for i in range(self.capacity):
            value = self.table[i] if self.table[i] is not None else "-"
            print(f"{i:5} | {value}")
        print()


def analyze_hash_function(hash_func, capacity: int, value_range: range) -> None:
    """Analysiert die Verteilung einer Hashfunktion.
    
    Args:
        hash_func: Zu analysierende Hashfunktion
        capacity: Grösse der Hashtabelle
        value_range: Bereich der zu testenden Werte
    """
    # TODO: Implementieren Sie eine Analyse der Hash-Verteilung
    pass


# Testfälle für Teil a
def test_part_a() -> None:
    """Test für Teil a: Einfügen von Werten."""
    print("=" * 60)
    print("Teil a: Einfügen von Werten mit quadratischem Sondieren")
    print("=" * 60)
    
    # Erstelle Hashtabelle und füge initiale Werte ein
    ht = QuadraticProbingHashTable(capacity=23)
    
    # Initiale Werte: [25, 48, 71, 94] an Positionen [2, 8, 15, 20]
    ht.table[2] = 25
    ht.table[8] = 48
    ht.table[15] = 71
    ht.table[20] = 94
    ht.size = 4
    
    print("\nInitialer Zustand:")
    ht.display()
    
    # Füge 63 ein
    print("\n" + "=" * 60)
    print("Einfügen von Wert: 63")
    print("=" * 60)
    final_index, probed_indices = ht.insert(63, verbose=True)
    print(f"\n✓ Wert 63 wurde an Index {final_index} eingefügt")
    ht.display()
    
    # Füge 116 ein
    print("\n" + "=" * 60)
    print("Einfügen von Wert: 116")
    print("=" * 60)
    final_index, probed_indices = ht.insert(116, verbose=True)
    print(f"\n✓ Wert 116 wurde an Index {final_index} eingefügt")
    ht.display()


# Testfälle für Teil b
def test_part_b() -> None:
    """Test für Teil b: Analyse der Hashfunktion."""
    print("\n" + "=" * 60)
    print("Teil b: Analyse der Hashfunktion")
    print("=" * 60)
    
    # TODO: Implementieren Sie die Analyse
    pass


if __name__ == "__main__":
    print("Hashtabellen-Übung mit quadratischem Sondieren\n")
    test_part_a()
    test_part_b()
```

## Vorgehen

### Teil a:

1. **Zeichnen Sie die Tabelle**: Skizzieren Sie die Hashtabelle mit den initialen Werten
2. **Berechnen Sie h(63)**: Wenden Sie die Hashfunktion an
3. **Prüfen Sie auf Kollisionen**: Ist der berechnete Index frei?
4. **Wenden Sie quadratisches Sondieren an**: Falls nötig, berechnen Sie weitere Indizes
5. **Wiederholen Sie für h(116)**: Führen Sie die gleichen Schritte durch

### Teil b:

1. **Testen Sie verschiedene Werte**: Berechnen Sie h(x) für mehrere Werte aus [0, 200]
2. **Analysieren Sie die Verteilung**: Welche Indizes werden häufig getroffen?
3. **Identifizieren Sie Muster**: Gibt es Symmetrien oder Cluster?
4. **Schlagen Sie Alternativen vor**: Welche Hashfunktion wäre besser?

## Bewertungskriterien

### Teil a (7 Punkte):

- Korrekte Berechnung von h(63): 2 Punkte
- Korrekte Sondierungsschritte für 63: 2 Punkte
- Korrekte Berechnung von h(116): 1 Punkt
- Korrekte Sondierungsschritte für 116: 2 Punkte

### Teil b (5 Punkte):

- Identifikation von Problemen: 2 Punkte
- Begründung der Probleme: 1 Punkt
- Vorschlag einer Alternative: 1 Punkt
- Begründung der Alternative: 1 Punkt

## Zusatzaufgaben (Optional)

1. **Visualisierung**: Erstellen Sie eine grafische Darstellung der Hash-Verteilung
2. **Vergleich**: Implementieren Sie Linear Probing und vergleichen Sie die Anzahl der Kollisionen
3. **Optimierung**: Finden Sie die optimale Tabellengrösse für den gegebenen Wertebereich
4. **Double Hashing**: Implementieren Sie Double Hashing als alternative Kollisionsstrategie

## Abgabe

Speichern Sie Ihre Lösung als `uebung_hashtabelle_sondierung_loesung.py` im selben Verzeichnis.

Viel Erfolg! 🚀
