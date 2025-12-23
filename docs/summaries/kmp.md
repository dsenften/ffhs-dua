# KMP String-Suchalgorithmus (Knuth-Morris-Pratt)

## Einleitung

Der KMP-Algorithmus (Knuth-Morris-Pratt) ist ein effizienter String-Suchalgorithmus, der einen Muster-String in einem Text-String sucht. Benannt nach seinen Erfindern Donald Knuth, Vaughan Pratt und James Morris (1977), ist KMP besonders bemerkenswert, weil er **garantierte lineare Laufzeit** auch im Worst-Case bietet.

**Kernvorteil**: Im Gegensatz zu naiven Ansätzen nutzt KMP eine vorberechnete Tabelle (DFA - Deterministic Finite Automaton oder Verschiebetabelle), um **Backtracking im Text zu vermeiden**. Der Text-Index läuft nur vorwärts, was zu einer garantierten O(n) Laufzeit führt, wobei n die Textlänge ist.

**Grundprinzip**: KMP verfolgt prinzipiell die gleiche Idee wie die Konstruktion eines deterministischen endlichen Automaten, vermeidet jedoch die aufwändige Konstruktion eines kompletten Automaten und beschränkt sich auf das Wesentliche: die Suche nach Präfixen des Musters innerhalb des Musters selbst.

## Hauptmerkmale

### Vorteile gegenüber naiven Algorithmen

1. **Kein Backtracking im Text**: Der Text-Index läuft nur vorwärts
2. **Worst-Case O(n) Laufzeit**: Garantierte lineare Laufzeit für die Suche
3. **Wiederverwendbar**: DFA wird einmal aufgebaut und kann für beliebig viele Suchen verwendet werden
4. **Effizient bei wiederholten Zeichen**: Gerade bei Mustern mit Wiederholungen deutlich schneller als naive Ansätze

### Typische Anwendungsfälle

- **Textsuche**: Schnelle Suche in grossen Texten (Editoren, Datenbanken)
- **DNA-Sequenzanalyse**: Suche nach genetischen Mustern
- **Netzwerk-Intrusion-Detection**: Pattern Matching in Netzwerkpaketen
- **Plagiatserkennung**: Effiziente Suche nach kopierten Textpassagen

## Algorithmus

### Naive String-Suche (zum Vergleich)

Die naive String-Suche vergleicht das Muster an jeder Position im Text:

```python
def naive_search(pattern: str, text: str) -> int:
    m = len(pattern)
    n = len(text)

    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            return i  # Gefunden an Position i
    return n  # Nicht gefunden
```

**Problem**: Bei einem Mismatch springt der Algorithmus nur um 1 Position weiter, auch wenn mehr Information verfügbar wäre. Dies führt zu O(n × m) Laufzeit im Worst-Case.

**Beispiel-Worst-Case**:
- Text: `"aaaaaaaaab"`
- Muster: `"aaab"`
- Naive Suche macht viele unnötige Vergleiche bei jedem Mismatch

### KMP-Idee: Verschiebetabelle und DFA

KMP kann auf zwei äquivalente Arten verstanden werden:

#### 1. Verschiebetabelle-Ansatz (Häberlein)

Die **Verschiebetabelle P** speichert für jede Position i im Muster die Länge des maximalen Präfixes, das sich vor Position i befindet:

- **P[i]**: Länge des längsten Präfixes des Musters, das mit den Zeichen vor Position i übereinstimmt
- **Zweck**: Bei einem Mismatch an Position i kann das Muster um `i - P[i]` Positionen weitergeschoben werden
- **Beispiel**: Für Muster `"kakaokaki"` ist P[7] = 3, weil die drei Zeichen "kak" vor Position 7 ein Präfix des Musters sind

#### 2. DFA-Ansatz (Sedgewick/Wayne)

KMP baut einen DFA auf, der für jeden Zustand (Position im Muster) und jedes mögliche Zeichen den nächsten Zustand bestimmt:

- **DFA-Dimension**: R × m Matrix (R = Alphabet-Grösse, m = Muster-Länge)
- **Zustand j**: Anzahl der bereits gematchten Zeichen (0 ≤ j < m)
- **Übergangsfunktion**: `dfa[c][j]` = nächster Zustand bei Zeichen c im Zustand j

**Kern-Prinzip**: Bei einem Mismatch springt der Algorithmus nicht zurück zum Anfang, sondern nutzt die bereits gematchten Zeichen, um den optimalen nächsten Zustand zu finden.

### Verschiebetabelle-Konstruktion (Häberlein-Ansatz)

Die Verschiebetabelle wird analog zur KMP-Suche berechnet, nur dass hier das Muster im Muster selbst gesucht wird:

```python
def VerschTab(M):
    """Berechnet die Verschiebetabelle für das Muster M."""
    q = -1
    P = [q]  # Verschiebetabelle

    for i in range(1, len(M)):
        # Suche längsten Präfix vor Position i
        while q >= 0 and M[q] != M[i]:
            q = P[q]  # Fallback über Verschiebetabelle
        q += 1
        P.append(q)

    return P
```

**Beispiel für Muster "kakaokaki"**:
- P = [-1, 0, 0, 1, 2, 0, 1, 2, 3]
- P[7] = 3: Die drei Zeichen "kak" vor Position 7 sind ein Präfix

### DFA-Konstruktion (Sedgewick/Wayne-Ansatz)

Der DFA wird in O(m × R) Zeit aufgebaut:

```python
class KMP:
    def __init__(self, pattern: str) -> None:
        self._pattern = pattern
        self._R = 256  # Extended ASCII
        m = len(pattern)

        # Initialisiere DFA (R × m Matrix)
        self._dfa = [[0] * m for _ in range(self._R)]

        # Baue DFA auf
        self._dfa[ord(pattern[0])][0] = 1  # Match im Zustand 0

        x = 0  # Restart-Zustand (Fallback bei Mismatch)
        for j in range(1, m):
            # Kopiere Mismatch-Fälle vom Restart-Zustand
            for c in range(self._R):
                self._dfa[c][j] = self._dfa[c][x]

            # Setze Match-Fall
            self._dfa[ord(pattern[j])][j] = j + 1

            # Update Restart-Zustand
            x = self._dfa[ord(pattern[j])][x]
```

**Restart-Zustand x**: Simuliert den DFA auf dem Muster selbst, um bei einem Mismatch den optimalen Fallback-Zustand zu finden.

### Suche mit Verschiebetabelle (Häberlein-Ansatz)

```python
def KMP(M, T):
    """Knuth-Morris-Pratt Suche mit Verschiebetabelle."""
    P = VerschTab(M)  # Berechne Verschiebetabelle
    erg = []
    q = -1  # Position im Muster (zuletzt erfolgreich geprüft)

    for i in range(len(T)):
        # Bei Mismatch: nutze Verschiebetabelle für Fallback
        while q >= 0 and M[q + 1] != T[i]:
            q = P[q]

        q += 1  # Nächste Position im Muster

        # Vollständiger Match gefunden
        if q == len(M) - 1:
            erg.append(i + 1 - len(M))  # Startposition des Matches
            q = P[q]  # Bereite nächste Suche vor

    return erg
```

### Suche mit DFA (Sedgewick/Wayne-Ansatz)

Die Suche läuft in O(n) Zeit:

```python
def search(self, text: str) -> int:
    n = len(text)
    m = len(self._pattern)

    i = 0  # Text-Index
    j = 0  # Muster-Index (Zustand im DFA)

    # Durchlaufe Text (nur vorwärts, kein Backtracking!)
    while i < n and j < m:
        j = self._dfa[ord(text[i])][j]  # Nächster Zustand
        i += 1  # Text-Index läuft nur vorwärts

    # Gefunden wenn j == m (Endzustand erreicht)
    if j == m:
        return i - m
    return n  # Nicht gefunden
```

**Wichtig**: Der Text-Index `i` läuft nur vorwärts. Es gibt kein Backtracking!

## Python-Implementierung

### Klasse KMP

```python
from collections.abc import Iterator

class KMP:
    """Knuth-Morris-Pratt String-Suchalgorithmus.

    Implementiert effiziente String-Suche durch Verwendung eines
    Deterministischen Finiten Automaten (DFA). Der DFA wird einmal
    beim Konstruktor aufgebaut und kann dann für beliebig viele
    Suchen wiederverwendet werden.
    """

    def __init__(self, pattern: str) -> None:
        """Initialisiert den KMP-Algorithmus mit einem Suchmuster."""
        if pattern is None:
            raise ValueError("Muster darf nicht None sein")
        if not pattern:
            raise ValueError("Muster darf nicht leer sein")

        self._pattern = pattern
        self._R = 256  # Extended ASCII
        # ... DFA-Aufbau ...

    @property
    def pattern(self) -> str:
        """Gibt das Suchmuster zurück."""
        return self._pattern

    def search(self, text: str) -> int:
        """Sucht das Muster im gegebenen Text.

        Returns:
            Index der ersten Übereinstimmung, oder len(text) wenn nicht gefunden
        """
        # ... Suche mit DFA ...

    def search_all(self, text: str) -> Iterator[int]:
        """Findet alle Vorkommen des Musters im Text.

        Returns:
            Iterator über alle Match-Positionen
        """
        pos = 0
        while pos <= len(text) - len(self._pattern):
            remaining_text = text[pos:]
            offset = self.search(remaining_text)

            if offset < len(remaining_text):
                yield pos + offset
                pos += offset + 1  # Weiter nach erstem Match
            else:
                break

    def count(self, text: str) -> int:
        """Zählt alle Vorkommen des Musters im Text."""
        return sum(1 for _ in self.search_all(text))
```

### Verwendungsbeispiele

```python
# Einfache Suche
kmp = KMP("NEEDLE")
position = kmp.search("HAYSTACK WITH NEEDLE IN IT")
print(position)  # 14

# Nicht gefunden
kmp = KMP("xyz")
position = kmp.search("abcdef")
print(position)  # 6 (len(text))

# Alle Vorkommen finden
kmp = KMP("ab")
for pos in kmp.search_all("ababab"):
    print(pos)  # 0, 2, 4

# Vorkommen zählen
kmp = KMP("the")
count = kmp.count("the quick brown fox jumps over the lazy dog")
print(count)  # 2
```

### CLI-Nutzung

```bash
# Grundlegende Nutzung
python3 -m src.algs4.pva_5_strings.kmp abracadabra abacadabrabracabracadabrabrabracad

# Ausgabe:
# text:    abacadabrabracabracadabrabrabracad
# pattern:               abracadabra
#
# Muster gefunden an Position 14
# Insgesamt 1 Vorkommen: [14]
```

## Komplexitätsanalyse

### Laufzeitanalyse (Amortisierte Analyse)

**Kernbeobachtung**: Die Variable q (Muster-Position) kann nicht bei jedem Durchlauf der Hauptschleife um m Werte erniedrigt werden. Die while-Schleife stellt sicher, dass q nur bis zum Wert -1 erniedrigt werden kann. Um q erneut zu erniedrigen, muss es zunächst erhöht worden sein.

**Amortisierte Analyse**:
- Jede Erhöhung von q geht mit einer Erhöhung von i (Text-Index) einher
- Schlimmster Fall: q wird immer in Einerschritten erniedrigt und danach wieder erhöht
- Insgesamt: n Schritte "nach oben" + n Schritte "nach unten" = 2n Schritte
- **Resultat**: Worst-Case-Komplexität von O(2n) = O(n)

### Komplexitätstabelle

| Operation | Laufzeit | Speicher | Bemerkung |
|-----------|----------|----------|-----------|
| **Verschiebetabelle-Aufbau** | O(m) | O(m) | m = Muster-Länge |
| **DFA-Aufbau** | O(m × R) | O(m × R) | R = Alphabet-Grösse (256) |
| `search(text)` | O(n) | O(1) | n = Text-Länge, **garantiert** auch im Worst-Case! |
| `search_all(text)` | O(n) | O(1) | Bei k Matches: O(n + k × m) |
| `count(text)` | O(n) | O(1) | Bei k Matches: O(n + k × m) |

**Wichtig**:
- Die Suche hat **garantierte O(n) Laufzeit**, unabhängig vom Muster
- Kein Backtracking im Text (i läuft nur vorwärts)
- Der DFA-Speicher ist O(m × R), bei R=256 sind das 256 × m Integer
- Die Verschiebetabelle benötigt nur O(m) Speicher

### Vergleich mit naiven Algorithmen

**Worst-Case Beispiel**:
- Text: `"aaaaaaaaaaaab"` (n Zeichen)
- Muster: `"aaaab"` (m Zeichen)

| Algorithmus | Laufzeit | Vergleiche |
|-------------|----------|------------|
| Naive Suche | O(n × m) | (n - m + 1) × m |
| KMP | O(n) | n |

Bei n=1.000.000 und m=100:
- Naive: ~100.000.000 Vergleiche
- KMP: ~1.000.000 Vergleiche (100× schneller!)

## Limitierungen

### Extended ASCII (256 Zeichen)

Die aktuelle Implementierung verwendet eine 256-Element DFA-Tabelle für Extended ASCII:

```python
self._R = 256  # Extended ASCII
```

**Limitation**: Unicode-Zeichen mit `ord() > 255` (z.B. Emojis wie 😀 mit ord=128512) führen zu einem `IndexError`.

**Lösung** (für volle Unicode-Unterstützung):
```python
# Alternative: Dictionary-basierte DFA statt Array
self._dfa = [{} for _ in range(m)]  # Speichert nur tatsächlich vorkommende Zeichen
```

### Speicherverbrauch

Bei langen Mustern (z.B. m=10.000) benötigt der DFA:
- Array-basiert: 256 × 10.000 × 4 Bytes ≈ 10 MB
- Dictionary-basiert: Deutlich weniger, abhängig vom Alphabet

Für sehr lange Muster können alternative Algorithmen wie **Boyer-Moore** effizienter sein.

## Vergleich mit anderen String-Suchalgorithmen

| Algorithmus | Preprocessing | Suche (Average) | Suche (Worst) | Speicher | Bemerkung |
|-------------|---------------|-----------------|---------------|----------|-----------|
| Naive | O(1) | O(n × m) | O(n × m) | O(1) | Einfach, aber langsam |
| **KMP** | O(m × R) | O(n) | O(n) | O(m × R) | Kein Backtracking, garantiert O(n) |
| Boyer-Moore | O(m + R) | O(n/m) | O(n × m) | O(m + R) | Oft schneller als KMP in Praxis |
| Rabin-Karp | O(m) | O(n + m) | O(n × m) | O(1) | Nutzt Hashing |

**KMP vs. Boyer-Moore**:
- KMP: Garantierte O(n) Laufzeit, kein Backtracking
- Boyer-Moore: Durchschnittlich schneller (O(n/m)), aber O(n × m) im Worst-Case

**Wann KMP nutzen**:
- Garantierte Worst-Case Performance gefordert
- Muster wird oft wiederverwendet (DFA-Aufbau amortisiert)
- Text mit vielen Wiederholungen (DNA-Sequenzen, komprimierte Daten)

## Beispiel: Verschiebetabelle-Simulation

Betrachten wir das Muster `"kakaokaki"` aus dem Häberlein-Buch:

### Verschiebetabelle für "kakaokaki"

| Position i | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|------------|---|---|---|---|---|---|---|---|---|
| Zeichen M[i] | k | a | k | a | o | k | a | k | i |
| P[i] | -1 | 0 | 0 | 1 | 2 | 0 | 1 | 2 | 3 |

**Erklärung**:
- P[7] = 3: Die drei Zeichen "kak" vor Position 7 sind ein Präfix des Musters
- P[3] = 1: Das eine Zeichen "k" vor Position 3 ist ein Präfix des Musters
- P[4] = 2: Die zwei Zeichen "ka" vor Position 4 sind ein Präfix des Musters

### Suche-Simulation

**Situation 1**: Mismatch nach "kakaoka" (q=7)
- Text: `...kakaoka?...` (? = Mismatch-Zeichen)
- Muster: `kakaokaki`
- P[7] = 3 → Springe zu q = 3
- Verschiebung: Das Muster wird so verschoben, dass die letzten 3 gematchten Zeichen "kak" mit dem Präfix "kak" des Musters übereinstimmen

**Situation 2**: Mismatch nach "kaka" (q=3)
- P[3] = 1 → Springe zu q = 1
- Verschiebung: Das letzte gematchte Zeichen "k" wird mit dem Präfix "k" des Musters ausgerichtet

## Beispiel: DFA-Simulation

Betrachten wir das Muster `"ABABC"` und wie der DFA aufgebaut wird:

### DFA-Tabelle (vereinfacht)

| Zustand (j) | 0 | 1 | 2 | 3 | 4 |
|-------------|---|---|---|---|---|
| Zeichen 'A' | 1 | 1 | 3 | 1 | - |
| Zeichen 'B' | 0 | 2 | 0 | 4 | - |
| Zeichen 'C' | 0 | 0 | 0 | 0 | 5 |
| Andere | 0 | 0 | 0 | 0 | 0 |

### Suche in Text `"ABABABABC"`

| i (Text-Index) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|----------------|---|---|---|---|---|---|---|---|---|
| text[i] | A | B | A | B | A | B | A | B | C |
| j (DFA-Zustand) | 0→1 | 1→2 | 2→3 | 3→4 | 4→? | - | - | - | - |

Bei i=4 (text[4]='A', j=4): Mismatch (erwarte 'C')
- Restart-Zustand: j=3 (nutze DFA, kein Backtracking!)
- Weiter bei i=5...

Finale Match an Position 4: `"ABABC"`

## Übungsaufgaben

### Aufgabe 1: Verschiebetabelle konstruieren (nach Häberlein)

Erstellen Sie die Verschiebetabelle für die folgenden Muster:

1. `"ananas"` - Beachten Sie die sich wiederholenden Präfixe
2. `"010011001001111"` - Binärmuster mit komplexen Überlappungen
3. `"ababcabab"` - Mischung aus Wiederholungen und eindeutigen Zeichen

**Tipp**: Verwenden Sie die Formel P[i] = max{k | k < i und M[0:k] == M[i-k+1:i+1]}

### Aufgabe 2: DFA-Konstruktion (nach Sedgewick/Wayne)

Konstruieren Sie den DFA für das Muster `"AACAA"`:

1. Zeichnen Sie die DFA-Tabelle für Zeichen 'A' und 'C'
2. Simulieren Sie die Suche in Text `"AAACAAAAACAA"`
3. Welcher Restart-Zustand wird bei einem Mismatch nach "AAC" verwendet?

### Aufgabe 3: Implementierung erweitern

Erweitern Sie die KMP-Implementierung um:

1. Eine Methode `search_last(text)`, die die **letzte** Position des Musters zurückgibt
2. Eine Methode `replace_all(text, replacement)`, die alle Vorkommen ersetzt
3. Unicode-Unterstützung durch Dictionary-basierte DFA

### Aufgabe 4: Performance-Analyse

Implementieren Sie beide Algorithmen (naiv und KMP) und messen Sie die Laufzeit für:

1. Text: 1 Million 'a's + 'b', Muster: 10.000 'a's + 'b'
2. DNA-Sequenz aus `data/strings/genomeVirus.txt`, Muster: `"ATCGATCG"`

Vergleichen Sie die Anzahl der Zeichenvergleiche und verwenden Sie Pythons `timeit`-Modul.

## Zusammenfassung

**KMP (Knuth-Morris-Pratt)** ist ein fundamentaler String-Suchalgorithmus mit folgenden Charakteristika:

**Stärken**:
- Garantierte O(n) Laufzeit, auch im Worst-Case
- Kein Backtracking im Text (i läuft nur vorwärts)
- Wiederverwendbarer DFA für mehrfache Suchen
- Effizient bei Mustern mit selbst-überlappenden Präfixen

**Zu beachten**:
- Preprocessing benötigt O(m × R) Zeit und Speicher
- Bei kleinen Alphabeten (DNA: A,C,G,T) sehr speichereffizient
- Bei grossen Alphabeten (Unicode) kann Dictionary-basierte DFA besser sein
- Boyer-Moore ist in der Praxis oft schneller, aber ohne Worst-Case Garantie

**Einsatzempfehlung**: KMP ist die beste Wahl für Anwendungen, die **garantierte lineare Laufzeit** benötigen, wie Echtzeitsysteme, Netzwerk-Intrusion-Detection oder DNA-Sequenzanalyse. Für allgemeine Textsuche kann Boyer-Moore schneller sein.

---

## Quellen

Diese Zusammenfassung basiert auf:

- **Praktische Algorithmik mit Python** von Tobias Häberlein, Abschnitt 7.3 "Der Knuth-Morris-Pratt-Algorithmus"
- **Algorithms, 4th Edition** von Robert Sedgewick und Kevin Wayne, Abschnitt 5.3 "Substring Search"
- **Introduction to Algorithms** (CLRS), Kapitel 32 "String Matching"
- Original-Paper: Knuth, Morris, Pratt (1977) "Fast Pattern Matching in Strings"

### Unterschiede der Darstellungen

**Häberlein-Ansatz**:
- Verwendet Verschiebetabelle P[i] mit Längen der Präfixe
- Einfachere Implementierung mit O(m) Speicherverbrauch
- Fokus auf praktische Umsetzung und Amortisationsanalyse

**Sedgewick/Wayne-Ansatz**:
- Verwendet vollständigen DFA mit R×m Matrix
- Theoretisch eleganter, aber höherer Speicherverbrauch O(m×R)
- Fokus auf formale Automatentheorie

Beide Ansätze sind äquivalent und führen zur gleichen O(n) Laufzeit.
