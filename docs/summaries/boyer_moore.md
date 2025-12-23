# Boyer-Moore String-Suchalgorithmus

## Überblick

Der Boyer-Moore-Algorithmus ist ein effizienter String-Suchalgorithmus, der 1977 von Robert S. Boyer und J Strother Moore entwickelt wurde. Er ist besonders effizient bei der Suche in grossen Texten mit langen Mustern und grossen Alphabeten. Der Algorithmus wurde einige Jahre nach dem Knuth-Morris-Pratt-Algorithmus entdeckt und ist - zumindest was die Average-Case-Komplexität betrifft - effizienter als KMP.

## Grundprinzip

Im Gegensatz zu naiven String-Suchalgorithmen, die das Muster von links nach rechts vergleichen, nutzt Boyer-Moore eine fundamentale Erkenntnis: **Mehr Informationen über Verschiebemöglichkeiten erhält man, wenn man die Musterpositionen von rechts nach links mit den aktuellen Textpositionen vergleicht**.

### Kernidee

1. **Muster läuft von links nach rechts** über den Text
2. **Vergleich erfolgt von rechts nach links** im Muster
3. **Bei Mismatch**: Muster wird um möglichst viele Positionen weitergeschoben
4. **Zwei Heuristiken** bestimmen die Verschiebung:
   - **Bad Character Rule** (Bad-Character-Heuristik)
   - **Good Suffix Rule** (Good-Suffix-Heuristik)

Der Boyer-Moore-Algorithmus schiebt das Muster um den **grösseren der beiden vorgeschlagenen Werte** weiter.

## Bad Character Rule (Bad-Character-Heuristik)

Die Bad Character Rule ist das Herzstück unserer Implementierung und die einfachere der beiden Heuristiken:

### Grundidee nach Häberlein

Die Bad-Character-Heuristik basiert **alleine auf dem Zeichen `c` des zu durchsuchenden Textes**, das den Mismatch verursacht hat - dem ersten Zeichen von rechts gesehen, das nicht mit der entsprechenden Stelle im Muster übereinstimmt.

### Zwei Fälle

1. **Zeichen `c` kommt nicht im Muster vor**:
   - Das Muster kann **an die Stelle nach dem Mismatch** weitergeschoben werden
   - Maximaler Sprung möglich

2. **Zeichen `c` kommt im Muster vor**:
   - Das Muster wird so weit nach rechts verschoben, dass das **von rechts gesehen erste Vorkommen von `c` im Muster** mit dem Mismatch-verursachenden Zeichen `c` im Text gleichauf liegt
   - **Spezialfall**: Wenn die Bad-Character-Heuristik eine Linksverschiebung vorschlagen würde, wird das Muster einfach um **eine Position** weitergerückt

### Implementierung nach Häberlein

```python
def makedelta1(M):
    """Erstellt Bad-Character-Tabelle als Dictionary"""
    delta1 = {}
    for i in range(len(M) - 1):  # Letztes Zeichen ausschliessen
        delta1[M[i]] = i
    return delta1

def badChar(delta1, c, j):
    """Berechnet Verschiebung basierend auf Bad Character"""
    if c in delta1:
        return j - delta1[c]  # Kann negativ sein!
    else:
        return j + 1  # Zeichen kommt nicht im Muster vor
```

### Unsere Implementierung (Optimiert)

```python
# Bad Character Table für alle ASCII-Zeichen
_right = [-1] * 256  # Initialisierung: Zeichen nicht im Muster

# Aufbau der Tabelle für Muster "NEEDLE":
# N: Position 0 → _right[ord('N')] = 0
# E: Position 1 → _right[ord('E')] = 1
# E: Position 2 → _right[ord('E')] = 2  (überschreibt Position 1)
# D: Position 3 → _right[ord('D')] = 3
# L: Position 4 → _right[ord('L')] = 4
# E: Position 5 → _right[ord('E')] = 5  (überschreibt Position 2)

# Ergebnis: E→5, D→3, L→4, N→0, alle anderen→-1
```

### Sprung-Berechnung

```python
skip = j - self._right[ord(text[i + j])]
if skip < 1:
    skip = 1  # Mindestens 1 Position vorwärts (verhindert Rückwärtssprünge)
```

**Parameter:**
- `j`: Position im Muster (von rechts nach links, 0-basiert)
- `text[i + j]`: Das fehlerhafte Zeichen im Text
- `_right[...]`: Rechteste Position dieses Zeichens im Muster (-1 wenn nicht vorhanden)

### Beispiel: Muster "kakaokaki"

Nach Häberlein's Beispiel aus Abbildung 7.4:

| Situation | Bad Character | delta1[c] | j | Verschiebung | Erklärung |
|-----------|---------------|-----------|---|--------------|-----------|
| 1 | 'o' | 4 | 6 | 6-4=2 | 'o' an Position 4 im Muster |
| 2 | 'x' | KeyError | 8 | 8+1=9 | 'x' kommt nicht im Muster vor |
| 3 | '-' | KeyError | 7 | 7+1=8 | '-' kommt nicht im Muster vor |
| 4 | 'o' | 4 | 8 | 8-4=4 | 'o' an Position 4 im Muster |
| 5 | 'a' | 6 | 5 | max(-1,1)=1 | Rückwärtssprung verhindert |
| 6 | 's' | KeyError | 8 | 8+1=9 | 's' kommt nicht im Muster vor |

## Good Suffix Rule (Good-Suffix-Heuristik)

Die Good-Suffix-Heuristik ist komplexer zu konstruieren, aber sehr mächtig:

### Grundidee nach Häberlein

Während die Bad-Character-Heuristik das Zeichen `c` betrachtet, das den Mismatch verursacht, zieht die Good-Suffix-Heuristik den **übereinstimmenden Teil von Muster und Text rechts des Zeichens `c`** in Betracht - das **"Good Suffix"**.

### Funktionsweise

Die Good-Suffix-Heuristik schlägt eine Verschiebung des Musters so vor, dass ein **weiter links stehender, mit diesem "Good-Suffix" übereinstimmender Teil des Musters** auf dieser Textstelle liegt.

### Beispiel: Muster "entbenennen"

| j | Good Suffix | Passender Teilstring | Verschiebung | Erklärung |
|---|-------------|---------------------|--------------|-----------|
| 0 | "n" | "e" an Position 9 | 1 | Einzelnes 'n' → 'e' passt |
| 1 | "en" | "en" an Position 7-8 | 2 | "en" → "en" passt |
| 2 | "nen" | "nen" an Position 4-6 | 5 | "nen" → "nen" passt |
| 3 | "nnen" | "nnen" an Position 5-8 | 3 | "nnen" → "nnen" passt |
| 4 | "ennen" | "···en" (virtuell) | 9 | Kein echter Match, virtueller Präfix |
| 5-9 | "nennen"+ | "···en" (virtuell) | 9 | Alle längeren Suffixe → virtueller Präfix |

### Implementierung nach Häberlein

```python
DOT = None  # Virtuelles Zeichen für Präfix-Erweiterung

def unify(pat, mismatch, suffix):
    """Prüft Kompatibilität von Muster-Teil mit Good-Suffix"""
    def eq(c1, c2): return c1 == DOT or c1 == c2
    def not_eq(c1, c2): return c1 == DOT or c1 != c2
    return not_eq(pat[0], mismatch) and all(map(eq, pat[1:], suffix))

def makedelta2(M):
    """Erstellt Good-Suffix-Tabelle"""
    m = len(M)
    delta2 = {}

    for j in range(0, m):  # Suffix der Länge j
        suffix = [] if j == 0 else M[-j:]
        mismatch = M[-j-1]

        for k in range(m-1, 0, -1):
            # Virtueller Präfix mit DOTs falls nötig
            pat = [DOT for i in range(-k + j)] + list(M[max(0, k-j): k+1])

            if unify(pat, mismatch, suffix):
                delta2[j] = m - 1 - k
                break

        if j not in delta2:
            delta2[j] = m  # Kein Match gefunden

    return delta2
```

### Unsere Implementierung

**Hinweis**: Unsere aktuelle Implementierung verwendet **nur die Bad Character Rule** für Einfachheit und Lehrklarheit. Die Good Suffix Rule würde die Implementierung erheblich komplexer machen, bietet aber in vielen Fällen bessere Performance.

## Komplexitätsanalyse

### Zeitkomplexität nach Häberlein

- **Best Case**: **O(n/m)** - sublinear!
  - Tritt auf wenn "viele" Zeichen des Textes gar nicht im Muster vorkommen
  - Oder wenn "viele" Suffixe kein weiteres Vorkommen im Muster haben
  - In diesen Fällen wird eine Verschiebung um `m` Positionen vorgeschlagen
  - Beispiel: Suche "ABCDEFGHIJK" in Text mit vielen 'A's

- **Average Case**: O(n) - linear
  - Bei typischen Texten und Mustern

- **Worst Case**: **O(3n)** ≈ **O(n)** - linear!
  - Mathematische Argumentation ist komplex (erst 1991 bewiesen)
  - **Nicht** O(n×m) wie oft fälschlicherweise angenommen
  - Deutlich besser als naive Algorithmen

### Speicherkomplexität

- **Bad Character Table**: O(R), wobei R = Alphabet-Grosse (256 für ASCII)
- **Good Suffix Table**: O(m), wobei m = Muster-Länge
- **Gesamt**: O(m + R), wobei m = Muster-Länge

## Implementierung

### Vollständiger Boyer-Moore nach Häberlein

```python
def boyerMoore(T, M):
    """Vollständige Boyer-Moore Implementierung mit beiden Heuristiken"""
    delta1 = makedelta1(M)  # Bad Character Table
    delta2 = makedelta2(M)  # Good Suffix Table
    m, n = len(M), len(T)
    i = m - 1  # Startposition im Text

    while i < n:
        i_old = i  # Merke Startposition für diese Iteration
        j = m - 1  # Starte am Ende des Musters

        # Vergleiche von rechts nach links
        while j >= 0 and T[i] == M[j]:
            i -= 1
            j -= 1

        if j == -1:  # Vollständiger Match gefunden
            print("Treffer:", i + 1)
            i = i_old + 1  # Suche nach weiteren Matches
        else:
            # Berechne Verschiebung mit beiden Heuristiken
            bad_char_shift = badChar(delta1, T[i], j)
            good_suffix_shift = delta2[m - 1 - j]

            # Nimm die groessere Verschiebung
            i = i_old + max(bad_char_shift, good_suffix_shift)
```

### Unsere vereinfachte Klassen-Struktur

```python
class BoyerMoore:
    def __init__(self, pattern: str) -> None:
        # Baut nur Bad Character Table auf (vereinfacht)

    def search(self, text: str) -> int:
        # Sucht erste Übereinstimmung

    def search_all(self, text: str) -> Iterator[int]:
        # Findet alle Übereinstimmungen

    def count(self, text: str) -> int:
        # Zählt alle Übereinstimmungen
```

### Unser Kern-Algorithmus (Bad Character Rule only)

```python
def search(self, text: str) -> int:
    n, m = len(text), len(self._pattern)
    i = 0  # Text-Index (Anfang des aktuellen Vergleichs)

    while i <= n - m:
        skip = 0

        # Vergleiche von rechts nach links
        for j in range(m - 1, -1, -1):
            if self._pattern[j] != text[i + j]:
                # Bad Character Rule
                skip = j - self._right[ord(text[i + j])]
                if skip < 1:
                    skip = 1  # Verhindere Rückwärtssprünge
                break

        if skip == 0:  # Vollständige Übereinstimmung
            return i

        i += skip  # Springe um berechnete Distanz

    return n  # Nicht gefunden
```

### Objektorientierte Implementierung nach Häberlein

Häberlein schlägt eine objektorientierte Implementierung vor:

```python
class BoyerMoore:
    def __init__(self, pattern):
        self.pattern = pattern
        self.delta1 = makedelta1(pattern)
        self.delta2 = makedelta2(pattern)

    def search(self, text):
        # Implementierung wie oben
        pass
```

**Vorteile der OOP-Variante:**
- Tabellen werden nur einmal berechnet
- Mehrfache Suchen mit demselben Muster sind effizienter
- Saubere Kapselung der Algorithmus-Daten

## Aufgaben und Übungen nach Häberlein

### Aufgabe 7.7: Best-Case Analyse
**Frage**: Angenommen alle mit `M[-1]` verglichenen Zeichen kommen nicht im Muster vor - wie viele Suchschritte benötigt Boyer-Moore?

**Antwort**: Nur **⌈n/m⌉** Schritte! Bei jedem Vergleich kann das Muster um die volle Länge `m` verschoben werden.

### Aufgabe 7.8: Worst-Case Szenarien
Mit `aⁿ` = n-malige Wiederholung von 'a':

- **(a)** Muster `ba⁹` in Text `a¹⁰⁰⁰`: **1000 Schritte** (jeder Vergleich schlägt beim letzten Zeichen fehl)
- **(b)** Muster `a⁹b` in Text `a¹⁰⁰⁰`: **≈100 Schritte** (grosse Sprünge möglich)
- **(c)** Muster `a⁹` in Text `a¹⁰⁰⁰b`: **≈100 Schritte** (Muster wird schnell gefunden)

### Aufgabe 7.9: Alternative Bad-Character Implementierung
**Optimierung**: Erstelle für jedes Alphabet-Zeichen einen Eintrag:

```python
def makedelta1_optimized(M):
    delta1 = [-1] * 256  # Für alle ASCII-Zeichen
    for i in range(len(M) - 1):
        delta1[ord(M[i])] = i
    return delta1

def badChar_optimized(delta1, c, j):
    return j - delta1[ord(c)] if delta1[ord(c)] != -1 else j + 1
```

**Vorteil**: Keine Dictionary-Lookups, direkter Array-Zugriff.

## Anwendungsbereiche

### Boyer-Moore ist besonders effizient bei:

1. **Grossen Alphabeten** (Häberlein's Hauptargument)
   - Englische Texte (26 Buchstaben)
   - ASCII-Texte (256 Zeichen)
   - Unicode-Texte
   - **Grund**: Viele Zeichen kommen nicht im Muster vor → grosse Sprünge

2. **Langen Mustern**
   - URLs, E-Mail-Adressen
   - Dateinamen, Pfade
   - Komplexe Suchbegriffe
   - **Grund**: Groessere Sprungdistanzen möglich

3. **Grossen Texten**
   - Dokumentensuche
   - Log-Datei-Analyse
   - Genomanalyse (bei grossen Alphabeten)
   - **Grund**: Sublineare O(n/m) Performance amortisiert sich

### Boyer-Moore ist weniger effizient bei:

1. **Kleinen Alphabeten** (Häberlein's Warnung)
   - DNA-Sequenzen (4 Basen: A, T, C, G)
   - Binäre Daten (0, 1)
   - **Grund**: Wenige grosse Sprünge möglich

2. **Kurzen Mustern**
   - 1-3 Zeichen lange Muster
   - Hier ist KMP oft besser
   - **Grund**: Overhead der Tabellenerstellung

3. **Wiederholenden Mustern**
   - "AAAA", "ABAB", etc.
   - Führt zu häufigen kleinen Sprüngen
   - **Grund**: Bad Character Rule versagt oft

## Vergleich mit anderen Algorithmen

### Korrigierte Komplexitätstabelle (nach Häberlein)

| Algorithmus | Best Case | Average Case | Worst Case | Speicher | Besonderheiten |
|-------------|-----------|--------------|------------|----------|----------------|
| **Boyer-Moore** | **O(n/m)** | **O(n)** | **O(n)** | O(m+R) | **Sublinear möglich** |
| **KMP** | O(n) | O(n) | O(n) | O(m×R) | Garantiert linear |
| **Naiv** | O(n) | O(n×m) | O(n×m) | O(1) | Einfach zu implementieren |

**Wichtige Korrektur**: Boyer-Moore hat **nicht** O(n×m) Worst-Case, sondern O(n)! Dies wurde erst 1991 mathematisch bewiesen.

### Wann welchen Algorithmus verwenden?

#### Boyer-Moore (nach Häberlein)
- **Ideal für**: Grosse Alphabete, lange Muster, grosse Texte
- **Beispiele**: Textverarbeitung, Dokumentensuche, Websuche
- **Vorteil**: Kann sublinear sein (schneller als Text einmal lesen!)

#### KMP
- **Ideal für**: Kleine Alphabete, garantierte Performance
- **Beispiele**: DNA-Analyse, Binärdaten, Echtzeitanwendungen
- **Vorteil**: Vorhersagbare O(n) Laufzeit

#### Naiv
- **Ideal für**: Sehr kurze Muster, einfache Implementierung
- **Beispiele**: Prototyping, Lernzwecke
- **Vorteil**: Minimaler Speicherverbrauch

## Praktische Beispiele

### Best-Case Szenario (nach Häberlein)

```python
# Häberlein's Beispiel: Grosses Alphabet, Zeichen kommen nicht im Muster vor
bm = BoyerMoore("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
text = "A" * 10000 + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Boyer-Moore macht grosse Sprünge (26 Zeichen pro Schritt)
# Nur etwa 10000/26 ≈ 385 Vergleiche statt 10000!
# Sublineare Performance: O(n/m)
```

### Häberlein's Aufgabe 7.7 Beispiel

```python
# Alle verglichenen Zeichen kommen nicht im Muster vor
pattern = "XYZNEEDLE"  # 9 Zeichen
text = "A" * 1000 + "XYZNEEDLE"  # 1000 'A's + Muster

# Boyer-Moore benötigt nur ⌈1000/9⌉ = 112 Schritte
# Jeder Vergleich mit 'A' führt zu Sprung um 9 Positionen
```

### Worst-Case Szenario (korrigiert nach Häberlein)

```python
# Häberlein warnt: Kleines Alphabet ist problematisch
bm = BoyerMoore("AAAA")
text = "A" * 10000

# Boyer-Moore macht kleine Sprünge, aber immer noch O(n)
# NICHT O(n×m) wie oft fälschlicherweise angenommen!
# Etwa 3n Schritte im absoluten Worst-Case
```

### DNA-Sequenz Beispiel (Häberlein's Warnung)

```python
# Kleines Alphabet (nur A, T, C, G) - Boyer-Moore weniger optimal
bm = BoyerMoore("ATCGATCG")
dna_text = "AAAAAATCGATCGTTTTTT"

# Viele Zeichen kommen im Muster vor → kleine Sprünge
# KMP wäre hier effizienter
```

### Häberlein's "kakaokaki" Beispiel

```python
# Demonstriert Bad Character Rule Schritt für Schritt
bm = BoyerMoore("kakaokaki")
text = "kakaokakaokakikakaokakis"

# Zeigt verschiedene Mismatch-Situationen:
# - 'o' kommt im Muster vor → moderate Sprünge
# - 'x' kommt nicht vor → grosse Sprünge
# - 'a' würde Rückwärtssprung verursachen → Sprung um 1
```

## CLI-Verwendung

```bash
# Grundlegende Suche
python3 -m src.algs4.pva_5_strings.boyer_moore "NEEDLE" "HAYSTACK WITH NEEDLE IN IT"

# DNA-Sequenz (weniger optimal für Boyer-Moore)
python3 -m src.algs4.pva_5_strings.boyer_moore "ATCG" "ATAGATCGCATAGCGCATAGC"

# Lange Muster (Boyer-Moore Stärke)
python3 -m src.algs4.pva_5_strings.boyer_moore "algorithm" "computer science algorithm analysis"

# Vergleich mit KMP
python3 -m src.algs4.pva_5_strings.boyer_moore "pattern" "text with pattern"
python3 -m src.algs4.pva_5_strings.kmp "pattern" "text with pattern"
```

## Historische Einordnung nach Häberlein

Der Boyer-Moore-Algorithmus wurde **einige Jahre nach dem Knuth-Morris-Pratt-Algorithmus entdeckt** [Boyer & Moore, 1977]. Häberlein betont, dass Boyer-Moore - **zumindest was die Average-Case-Komplexität betrifft** - effizienter als KMP ist.

### Schlüsselerkenntnisse aus Häberlein

1. **Rückwärtsvergleich ist der Schlüssel**: Mehr Informationen über Verschiebemöglichkeiten durch Vergleich von rechts nach links
2. **Zwei Heuristiken sind besser als eine**: Bad Character + Good Suffix Rule ergänzen sich optimal
3. **Alphabet-Grosse ist entscheidend**: Bei grossen Alphabeten zeigt Boyer-Moore seine wahre Stärke
4. **Worst-Case ist besser als gedacht**: O(n) statt O(n×m), aber erst 1991 bewiesen

### Praktische Implementierungsempfehlungen

#### Für Lernzwecke (nach Häberlein)
- **Beginne mit Bad Character Rule**: Einfacher zu verstehen und implementieren
- **Erweitere um Good Suffix Rule**: Für vollständige Performance
- **Teste mit verschiedenen Alphabeten**: Verstehe den Einfluss der Alphabet-Grösse

#### Für Produktionsumgebungen
- **Verwende beide Heuristiken**: Maximale Performance
- **Objektorientierte Implementierung**: Wiederverwendbare Muster-Objekte
- **Optimierte Bad Character Table**: Array statt Dictionary für ASCII

## Fazit

Der Boyer-Moore-Algorithmus ist ein **revolutionärer String-Suchalgorithmus**, der durch seine **Rückwärts-Vergleichsstrategie** und **zwei komplementäre Heuristiken** in den richtigen Szenarien aussergewöhnliche Performance bietet:

### Häberlein's Hauptargumente:
- **Sublineare Performance möglich**: O(n/m) bei grossen Alphabeten
- **Praktisch oft schneller als KMP**: Besonders bei natürlichen Sprachen
- **Elegante mathematische Grundlage**: Zwei Heuristiken ergänzen sich optimal

### Unsere Implementierung:
- **Fokus auf Bad Character Rule**: Einfachheit für Lehrzwecke
- **Konsistente API mit KMP**: Einheitliche Nutzung
- **Umfassende Tests**: 59 Tests für alle Szenarien

### Wann Boyer-Moore verwenden:
- **Grosse Alphabete** (Englisch, ASCII, Unicode)
- **Lange Muster** (URLs, komplexe Suchbegriffe)
- **Performance-kritische Anwendungen** (Textsuche, Dokumentenanalyse)

### Wann KMP bevorzugen:
- **Kleine Alphabete** (DNA, Binärdaten)
- **Garantierte lineare Laufzeit** erforderlich
- **Echtzeitanwendungen** mit vorhersagbarer Performance

Boyer-Moore bleibt ein **Meilenstein der Algorithmik** und demonstriert, wie clevere Heuristiken und Rückwärts-Denken zu bahnbrechenden Verbesserungen führen können.
