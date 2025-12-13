# Tries - Effiziente String-Suchbäume

## Einleitung

Tries sind spezialisierte Baumdatenstrukturen, deren Kanten mit Buchstaben oder Zeichenteilen beschriftet sind. Der Name "Trie" leitet sich vom englischen Wort "retrieval" (Wiederfinden von Informationen) ab. Sie eignen sich besonders für die effiziente Speicherung und Suche von Schlüssel-Wert-Paaren, bei denen die Schlüssel aus Zeichenketten bestehen.

**Kernvorteil**: Die Suchzeit in einem Trie hängt **nicht** von der Gesamtzahl der Einträge ab, sondern **ausschließlich von der Länge des Suchschlüssels**. Eine Suche nach einem kurzen String benötigt immer die gleiche Anzahl Schritte, unabhängig davon, ob der Trie 1.000, 100.000 oder mehrere Milliarden Einträge enthält.

## Hauptmerkmale

### Vorteile gegenüber anderen Datenstrukturen

1. **Unabhängigkeit von der Datenmenge**: Suchzeit O(m), wobei m = Länge des Suchschlüssels
2. **Speichereffizienz**: Gemeinsame Präfixe werden nur einmal gespeichert
3. **Keine Schlüsselvergleiche**: Die Position im Baum bestimmt den Schlüssel
4. **Präfix-Operationen**: Effiziente Suche nach allen Einträgen mit gleichem Präfix

### Typische Anwendungsfälle

- **Textsuchmaschinen**: Effiziente Volltextsuche
- **Routing-Tabellen**: Lookup-Operationen im Internet
- **Autovervollständigung**: Schnelle Präfix-basierte Vorschläge
- **Rechtschreibprüfung**: Wörterbuch-Implementierungen

## Datenstruktur

### Konzept

Anders als bei binären Suchbäumen werden in Tries die Schlüssel nicht in den Knoten gespeichert. Stattdessen bestimmt die **Position des Knotens** innerhalb des Baums, welcher Schlüssel repräsentiert wird.

### Aufbau

- **Knoten**: Jeder Knoten hat ein Attribut für den Wert (`val`) und eine Menge von Kind-Knoten (`children`)
- **Kanten**: Beschriftet mit Zeichen (z.B. 'a' bis 'z')
- **Navigation**: Von der Wurzel ausgehend folgt man den mit den Zeichen des Suchschlüssels markierten Kanten
- **Werte**: Nur Knoten, die tatsächlich einen Schlüssel repräsentieren, speichern Werte

### Python-Implementierung

```python
from typing import Generic, TypeVar

V = TypeVar("V")  # Value type

class _Node(Generic[V]):
    """Knoten im Trie."""
    def __init__(self) -> None:
        self.val: V | None = None
        self.children: dict[str, _Node[V]] = {}

class TrieST(Generic[V]):
    """Trie Symbol Table - String-basierte Symbol-Tabelle."""
    def __init__(self) -> None:
        self._root: _Node[V] | None = None
        self._n: int = 0  # Anzahl der Schlüssel-Wert-Paare
```

**Designentscheidung**: Die Verwendung eines `dict` für `children` ist effizienter als eine Liste von Tupeln, da der Zugriff auf ein spezifisches Kind in O(1) erfolgt. Die Dictionary-basierte Implementierung ist flexibel für beliebige Zeichen (nicht nur ASCII) und entspricht den Python-Konventionen.

### Beispiel

Ein Trie mit den Schlüsseln 'bahn', 'bar', 'bis', 'sole', 'soll', 'tri', 'trie' und 'trip':

```
         [root]
        /   |   \
       b    s    t
      / \   |    |
     a   i  o    r
     |   |  |    |
     h   s  l    i
     |      |  / | \
     n     l e  p
           |
           e
```

Nur Knoten mit doppelter Umrandung (Endknoten) speichern tatsächlich Werte.

## Operationen

### Suche

Die Suche ist die fundamentale Operation eines Tries.

**Algorithmus**:

1. Beginne an der Wurzel
2. Wenn die Tiefe gleich der Schlüssellänge ist → Rückgabe des Wertes im aktuellen Knoten
3. Nimm das Zeichen an der aktuellen Position
4. Wenn keine Kante mit diesem Zeichen existiert → Rückgabe `None` (nicht gefunden)
5. Folge der Kante zu Kind-Knoten und fahre rekursiv fort

**Python-Implementierung**:

```python
class TrieST(Generic[V]):
    def get(self, key: str) -> V | None:
        """Gibt den Wert zurück, der mit dem Schlüssel verknüpft ist."""
        if key is None:
            raise ValueError("Schlüssel darf nicht None sein")
        node = self._get(self._root, key, 0)
        if node is None:
            return None
        return node.val

    def _get(self, node: _Node[V] | None, key: str, depth: int) -> _Node[V] | None:
        """Hilfsmethode für get - sucht rekursiv nach einem Knoten."""
        if node is None:
            return None
        if depth == len(key):
            return node
        char = key[depth]
        if char not in node.children:
            return None
        return self._get(node.children[char], key, depth + 1)
```

**Laufzeit**: O(m), wobei m = Länge des Suchschlüssels

### Einfügen

Das Einfügen navigiert zum passenden Knoten und erstellt fehlende Zwischenknoten bei Bedarf.

**Algorithmus**:

1. Wenn die Tiefe gleich der Schlüssellänge ist → Speichere den Wert im aktuellen Knoten
2. Nimm das Zeichen an der aktuellen Position
3. Wenn kein Kind mit diesem Zeichen existiert → Erstelle einen neuen Kind-Knoten
4. Folge der Kante zu Kind-Knoten und fahre rekursiv fort

**Python-Implementierung**:

```python
class TrieST(Generic[V]):
    def put(self, key: str, val: V) -> None:
        """Fügt ein Schlüssel-Wert-Paar in den Trie ein."""
        if key is None:
            raise ValueError("Schlüssel darf nicht None sein")
        self._root = self._put(self._root, key, val, 0)

    def _put(self, node: _Node[V] | None, key: str, val: V, depth: int) -> _Node[V]:
        """Hilfsmethode für put - fügt rekursiv einen Schlüssel ein."""
        if node is None:
            node = _Node[V]()
        if depth == len(key):
            if node.val is None:
                self._n += 1  # Neuer Schlüssel
            node.val = val
            return node
        char = key[depth]
        if char not in node.children:
            node.children[char] = _Node[V]()
        node.children[char] = self._put(node.children[char], key, val, depth + 1)
        return node
```

**Laufzeit**: O(m), wobei m = Länge des Schlüssels

### Löschen

Das Löschen entfernt einen Schlüssel und bereinigt unnötige Knoten.

**Algorithmus**:

1. Navigiere zum Knoten mit dem Schlüssel
2. Setze den Wert auf `None`
3. Entferne leere Knoten beim Zurücklaufen der Rekursion

**Python-Implementierung**:

```python
class TrieST(Generic[V]):
    def delete(self, key: str) -> None:
        """Löscht den Schlüssel und den zugehörigen Wert aus dem Trie."""
        if key is None:
            raise ValueError("Schlüssel darf nicht None sein")
        self._root = self._delete(self._root, key, 0)

    def _delete(self, node: _Node[V] | None, key: str, depth: int) -> _Node[V] | None:
        """Hilfsmethode für delete - löscht rekursiv einen Schlüssel."""
        if node is None:
            return None

        if depth == len(key):
            if node.val is not None:
                self._n -= 1
            node.val = None
        else:
            char = key[depth]
            if char in node.children:
                node.children[char] = self._delete(node.children[char], key, depth + 1)
                if node.children[char] is None:
                    del node.children[char]

        # Entferne Knoten ohne Wert und ohne Kinder
        if node.val is None and len(node.children) == 0:
            return None

        return node
```

**Laufzeit**: O(m), wobei m = Länge des Schlüssels

### Präfix-Operationen

Eine der Stärken von Tries ist die effiziente Unterstützung für Präfix-basierte Operationen.

**keys_with_prefix(prefix)**: Gibt alle Schlüssel zurück, die mit dem Präfix beginnen.

```python
def keys_with_prefix(self, prefix: str) -> Iterator[str]:
    """Gibt alle Schlüssel zurück, die mit dem Präfix beginnen."""
    queue: Queue[str] = Queue()
    node = self._get(self._root, prefix, 0)
    self._collect(node, prefix, queue)
    return iter(queue)

def _collect(self, node: _Node[V] | None, prefix: str, queue: Queue[str]) -> None:
    """Sammelt alle Schlüssel im Teilbaum."""
    if node is None:
        return
    if node.val is not None:
        queue.enqueue(prefix)
    for char in sorted(node.children.keys()):
        self._collect(node.children[char], prefix + char, queue)
```

**keys_that_match(pattern)**: Gibt alle Schlüssel zurück, die einem Muster entsprechen (`.` = Wildcard).

```python
def keys_that_match(self, pattern: str) -> Iterator[str]:
    """Gibt alle Schlüssel zurück, die dem Muster entsprechen."""
    queue: Queue[str] = Queue()
    self._collect_match(self._root, "", pattern, queue)
    return iter(queue)
```

**longest_prefix_of(query)**: Gibt den längsten Schlüssel zurück, der ein Präfix der Query ist.

```python
def longest_prefix_of(self, query: str) -> str:
    """Gibt den längsten Schlüssel zurück, der ein Präfix von query ist."""
    length = self._search(self._root, query, 0, 0)
    return query[:length]
```

Diese Operationen sind besonders nützlich für:
- **Autovervollständigung**: `keys_with_prefix("pr")` → ["print", "printf", "private"]
- **Wildcard-Suche**: `keys_that_match(".he.l.")` → ["shells"]
- **Routing**: `longest_prefix_of("192.168.1.100")` → findet längste IP-Präfix-Übereinstimmung

## Performance-Vergleich

### Tries vs. Binäre Suchbäume

**Vergleichsaufwand**:
- **Trie mit 1 Mio. Einträgen** (Schlüssellänge ≤ 14): Maximal 14 Zeichenvergleiche
- **Balancierter BST mit 1 Mio. Einträgen**: Etwa log₂(1.000.000) ≈ 20 Vergleiche, wobei jeder Vergleich bis zu 14 Zeichen vergleichen kann

Tries vermeiden teure String-Vergleiche durch zeichenweise Navigation.

### Tries vs. Python dict

Laufzeitmessungen für das Suchen von 1000 Wörtern der Länge 100 zeigen, dass Tries trotz Python-Implementierung mit der in C implementierten `dict`-Struktur mithalten können. Dies deutet darauf hin, dass Tries für diesen Anwendungsfall **prinzipiell die effizientere Methode** sind.

## Komplexitätsanalyse

| Operation | Laufzeit | Bemerkung |
|-----------|----------|-----------|
| Suche     | O(m)     | m = Schlüssellänge, unabhängig von n |
| Einfügen  | O(m)     | m = Schlüssellänge, unabhängig von n |
| Löschen   | O(m)     | m = Schlüssellänge |
| Speicher  | O(ALPHABET_SIZE × n × m) | Worst Case, bei vielen gemeinsamen Präfixen deutlich besser |

**Wichtig**: Im Gegensatz zu Hash-Tabellen (O(1) durchschnittlich) und BSTs (O(log n)) hängt die Laufzeit bei Tries nicht von der Anzahl der Einträge n ab!

## Übungsaufgaben

### Aufgabe 1: Trie zeichnen

Zeichnen Sie einen Trie mit folgenden Schlüsseln:

- gans, ganz, galle, leber, lesen, lesezeichen, zeichnen, zeilenweise, adam, aaron

Fragen:

- Wie viele Schritte benötigt eine Suche minimal?
- Wie viele Schritte benötigt eine Suche maximal?

### Aufgabe 2: keys() Methode

Implementieren Sie eine Methode `keys()`, die eine Liste aller im Trie befindlichen Schlüsselwerte zurückliefert.

**Hinweis**: Verwenden Sie eine rekursive Tiefensuche und sammeln Sie Schlüssel nur bei Knoten mit `val != None`.

## Patricia-Tries (Optimierung)

### Motivation

Standard-Tries können ineffizient werden, wenn viele Einträge einen langen gemeinsamen Präfix teilen. Dies führt zu langen Ketten von Knoten mit jeweils nur einem Kind.

**Beispiel**: Wenn alle Wörter mit 'bau' beginnen, entstehen drei unnötige Knoten für 'b', 'a', 'u'.

### Patricia-Konzept

**Patricia** (auch Patricia-Trie genannt) ist eine kompaktere Variante des Tries:
- **Optimierung**: Knoten mit Grad 1 (nur ein Kind) ohne Informationen werden mit dem Kind-Knoten verschmolzen
- **Speicherung**: Die verbleibenden Knoten speichern den gemeinsamen Präfix aller Einträge im Teilbaum
- **Trade-off**: Kompaktere Speicherung gegen etwas langsamere Einfüge- und Löschoperationen

### Datenstruktur

```python
class Patricia(object):
    def __init__(self):
        self.children = {}  # Identisch zu Trie
        self.val = None
```

Die Implementierung ist komplexer als bei Standard-Tries, da beim Einfügen und Löschen geprüft werden muss, ob Knoten verschmolzen oder aufgeteilt werden müssen.

### Anwendung

Patricia-Tries werden häufig in Routing-Tabellen und Netzwerkanwendungen eingesetzt, wo Speichereffizienz wichtig ist und die zusätzliche Implementierungskomplexität gerechtfertigt werden kann.

## Zusammenfassung

**Tries** sind hocheffiziente Datenstrukturen für String-basierte Schlüssel mit folgenden Charakteristika:

**Stärken**:

- Suchzeit unabhängig von Anzahl der Einträge (nur von Schlüssellänge)
- Keine teuren String-Vergleiche nötig
- Natürliche Unterstützung für Präfix-Operationen
- Gemeinsame Präfixe werden effizient gespeichert

**Zu beachten**:

- Speicherverbrauch kann hoch sein bei kleinem Alphabet und wenig gemeinsamen Präfixen
- Implementierung ist etwas komplexer als BSTs
- Patricia-Tries bieten kompaktere Speicherung bei etwas höherem Implementierungsaufwand

**Einsatzempfehlung**: Tries sind die beste Wahl für Anwendungen mit String-Schlüsseln, bei denen schnelle Suche und Präfix-Operationen im Vordergrund stehen, wie Textsuchmaschinen, Autovervollständigung und Netzwerk-Routing.

---

## Quelle

Diese Zusammenfassung basiert auf:

- **Praktische Algorithmik mit Python** von Tobias Häberlein, Abschnitt 3.7 "Tries" und 3.8 "Patricia-Tries"
