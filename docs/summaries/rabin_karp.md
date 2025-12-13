# Rabin-Karp String-Suchalgorithmus

## Überblick

Der Rabin-Karp-Algorithmus ist ein String-Suchalgorithmus, der Rolling Hash verwendet, um Muster in Texten zu finden. Er wurde 1987 von Michael O. Rabin und Richard M. Karp entwickelt und ist besonders nützlich für Multiple-Pattern-Suche und Plagiatserkennung.

**Häberlein's Einordnung (Abschnitt 7.5):** Der Rabin-Karp-Algorithmus geht einen "ganz anderen Weg" als Boyer-Moore und KMP. Anstatt Zeichen direkt zu vergleichen, berechnet er Hash-Werte und sucht nach Hash-Übereinstimmungen. Dies macht ihn besonders geeignet für die Suche sehr langer oder mehrerer Muster, etwa in Plagiatssoftware, die mehrere längere Original-Textausschnitte in einem zu überprüfenden Text sucht.

## Grundprinzip

Der Algorithmus berechnet Hash-Werte für:
1. Das Suchmuster (einmalig)
2. Jeden Substring der gleichen Länge im Text (mit Rolling Hash)

Bei Hash-Übereinstimmung wird eine explizite Verifikation durchgeführt (Las Vegas Version).

## Zeitkomplexität

- **Bester Fall**: O(n + m) - keine Hash-Kollisionen
- **Durchschnittlicher Fall**: O(n + m) - wenige Hash-Kollisionen
- **Schlechtester Fall**: O(n × m) - viele Hash-Kollisionen

Wobei n = Textlänge, m = Musterlänge

## Raumkomplexität

O(1) - konstanter Speicherbedarf

## Rolling Hash (Häberlein 7.5.1)

**Definition nach Häberlein:** Ein rollender Hash ist eine Hashfunktion, die ihre Eingabe aus einem "Fenster" konstanter Grösse bezieht, das von links nach rechts über die Eingabe geschoben wird.

**Häberlein's Hash-Funktion:** Für einen String s wird der Hash folgendermassen berechnet:
```
h(s) = (s[0] × B^(l-1) + s[1] × B^(l-2) + ... + s[l-1] × B^0) mod M
```

**Unsere moderne Implementierung:** Der Schlüssel zur Effizienz ist der Rolling Hash:
```
hash(s[i+1..i+m]) = (hash(s[i..i+m-1]) - s[i] × R^(m-1)) × R + s[i+m]
```

**Parameter-Wahl:**
- **Häberlein**: B = Basis, M = 2^k - 1 (Zweierpotenz für Performance)
- **Unsere Implementierung**: R = 256 (Extended ASCII), q = grosse Primzahl
- **Häberlein's Begründung**: Zweierpotenz als Modul entspricht dem Abschneiden binärer Stellen, was der natürlichen Funktionsweise eines Rechners entspricht

## Implementierungsdetails

### Häberlein's Horner-Schema (7.5.1)

**Häberlein's primitive Implementierung:**
```python
def rollhash(s):
    h = 0
    for i, c in enumerate(s[::-1]):
        h += (B ** i) * ord(c)
        h = h & M
    return h
```

**Häberlein's optimierte Version (Horner-Schema):**
```python
def rollhash2(s):
    return reduce(lambda h, c: (c + B * h) & M, map(ord, s))
```

**Häberlein's Rolling Hash Update (Fenster nach rechts):**
```
h_neu = ((h_alt - B^(l-1) * s[i]) * B + s[i+l]) & M
```

### Unsere moderne Implementierung

**Hash-Funktion (Horner's Methode):**
```python
def _hash(self, key: str) -> int:
    hash_value = 0
    for char in key:
        hash_value = (self._R * hash_value + ord(char)) % self._q
    return hash_value
```

**Rolling Hash Update:**
```python
# Entferne altes Zeichen, füge neues hinzu
text_hash = (text_hash + self._q - self._rm * ord(text[i - self._m]) % self._q) % self._q
text_hash = (text_hash * self._R + ord(text[i])) % self._q
```

**Las Vegas Verifikation:**
```python
def _verify_match(self, text: str, pos: int) -> bool:
    if pos + self._m > len(text):
        return False
    return text[pos:pos + self._m] == self._pattern
```

## Häberlein's Multiple-Pattern-Implementierung (7.5.2)

**Häberlein's Ansatz:** Der Algorithmus kann gleichzeitig nach mehreren Mustern gleicher Länge suchen:

```python
def rabinKarp(Ms, T):
    hashs = set(map(rollhash, Ms))  # Hash-Werte aller Muster
    l = len(Ms[0])
    h = rollhash(T[:l])
    i = 0
    if h in hashs:
        if T[i:i+l] in Ms: print "Treffer bei", i
    while i + l < len(T) - 1:
        h = (h - ord(T[i]) * B**(l-1)) * B + ord(T[i+l]) & M
        i += 1
        if h in hashs:
            if T[i:i+l] in Ms: print "Treffer bei", i
```

**Häberlein's Schlüsselerkenntnisse:**
- Verwendung eines `set` für Hash-Werte (Performance-optimiert)
- Explizite Verifikation: `T[i:i+l] in Ms` nach Hash-Match
- "Wurden Basis B und Modul M geschickt gewählt, so sollte es sehr selten vorkommen, dass 'h in hashs' jedoch nicht 'T[i:i+l] in Ms' gilt"

## Vorteile

1. **Multiple-Pattern-Suche** - Häberlein's Hauptanwendung: gleichzeitige Suche mehrerer Muster
2. **Plagiatserkennung** - Häberlein's Beispiel: Software zur automatischen Plagiatsprüfung
3. **Einfache Implementierung** - konzeptionell leicht verständlich
4. **Gute durchschnittliche Performance** - O(n + m) bei wenigen Kollisionen
5. **Konstanter Speicherbedarf** - O(1) Raumkomplexität pro Muster
6. **Parallelisierbar** - Hash-Berechnungen können parallelisiert werden

## Nachteile

1. **Performance-Nachteile** - Häberlein: "in vielen Fällen dem Boyer-Moore-Algorithmus unterlegen"
2. **Worst-Case O(n × m)** - bei vielen Hash-Kollisionen
3. **Abhängig von Hash-Funktion** - Qualität der Parameter B und M ist entscheidend
4. **Keine Garantien** - im Gegensatz zu KMP's garantiertem O(n)
5. **Numerische Stabilität** - grosse Zahlen können Overflow verursachen

## Anwendungen

### Häberlein's Hauptanwendungsgebiete:
1. **Plagiatssoftware** - "Software, die Dokumente automatisch nach Plagiaten überprüft, indem sie mehrere längere (Original-)Textausschnitte in dem zu überprüfenden Text sucht"
2. **Multiple-Pattern-Suche** - gleichzeitige Suche nach mehreren Mustern gleicher Länge
3. **Sehr lange Muster** - besonders geeignet für die Suche sehr langer Muster

### Weitere praktische Anwendungen:
4. **DNA-Sequenzanalyse** - Suche nach genetischen Mustern
5. **Textverarbeitung** - allgemeine String-Suche
6. **Kryptographie** - Hash-basierte Verfahren
7. **Dokumentenvergleich** - Ähnlichkeitsanalyse zwischen Texten

## Vergleich mit anderen Algorithmen

| Algorithmus | Bester Fall | Durchschnitt | Schlechtester Fall | Speicher |
|-------------|-------------|--------------|-------------------|----------|
| Rabin-Karp  | O(n + m)    | O(n + m)     | O(n × m)          | O(1)     |
| KMP         | O(n + m)    | O(n + m)     | O(n + m)          | O(m)     |
| Boyer-Moore | O(n/m)      | O(n)         | O(n × m)          | O(m + R) |
| Naive       | O(n + m)    | O(n × m)     | O(n × m)          | O(1)     |

## Optimierungen und Parameter-Wahl

### Häberlein's Optimierungsstrategien:

1. **Horner-Schema** - deutlich schnellere Hash-Berechnung durch Ausklammern der B-Werte
2. **Zweierpotenz als Modul** - M = 2^k - 1 für Performance-Gründe
   - Entspricht dem Abschneiden binärer Stellen ab Position k
   - Nutzt natürliche Rechner-Funktionsweise (Overflow-Verhalten)
   - In Python: `h & M` statt aufwändiger Modulo-Operation
3. **Set für Hash-Speicherung** - Performance-optimierter Enthaltensein-Test
4. **Geschickte Parameter-Wahl** - B und M so wählen, dass Hash-Kollisionen selten sind

### Unsere modernen Optimierungen:

5. **Grosse Primzahl wählen** - grosse Primzahl reduziert Kollisionen
6. **Rabin-Miller Test** - für sichere Primzahl-Generierung
7. **Modulare Arithmetik** - verhindert Integer-Overflow
8. **Las Vegas statt Monte Carlo** - explizite Verifikation eliminiert False Positives

### Häberlein's Parameter-Beispiele:
```python
B = 256  # Basis für Extended ASCII
M = 2**32 - 1  # Zweierpotenz minus 1
```

## Implementierung in diesem Projekt

Unsere Implementierung bietet:

- **Las Vegas Version** mit expliziter Verifikation
- **Konsistente API** mit `search()`, `search_all()`, `count()`
- **Deutsche Dokumentation** und Fehlerbehandlung
- **Type-Hints** für alle Methoden
- **CLI-Interface** für einfache Nutzung
- **Umfassende Tests** (63 Tests, 100% bestanden)

### Verwendung

```python
from src.algs4.pva_5_strings import RabinKarp

# Erstelle Rabin-Karp Instanz
rk = RabinKarp("NEEDLE")

# Suche im Text
position = rk.search("HAYSTACK WITH NEEDLE IN IT")
print(position)  # 14

# Alle Vorkommen finden
matches = list(rk.search_all("needle in needle stack"))
print(matches)  # [0, 10] (case-sensitive)

# Vorkommen zählen
count = rk.count("test test test")
print(count)  # 3
```

### Vergleich: Häberlein vs. Unsere Implementierung

| Aspekt | Häberlein (2018) | Unsere Implementierung (2024) |
|--------|------------------|--------------------------------|
| **Zielgruppe** | Multiple-Pattern-Suche | Single + Multiple Pattern |
| **Parameter** | B=256, M=2^k-1 | R=256, q=grosse Primzahl |
| **Hash-Update** | `h & M` (Bitwise AND) | `h % q` (Modulo) |
| **Verifikation** | `T[i:i+l] in Ms` | `text[pos:pos+m] == pattern` |
| **API** | Funktional | Objektorientiert |
| **Ausgabe** | Print-Statements | Return-Werte + CLI |
| **Fehlerbehandlung** | Minimal | Umfassend (deutsch) |
| **Tests** | Keine erwähnt | 63 Tests, 100% Coverage |
| **Dokumentation** | Englisch | Deutsch + Type-Hints |

### CLI-Nutzung

```bash
python3 -m src.algs4.pva_5_strings.rabin_karp "NEEDLE" "HAYSTACK WITH NEEDLE IN IT"
```

## Theoretische Fundierung vs. Praktische Umsetzung

### Häberlein's Theoretische Erkenntnisse:
- **Hash-basierter Ansatz**: "ganz anderer Weg" als Zeichen-basierte Algorithmen
- **Multiple-Pattern-Stärke**: Hauptvorteil liegt in der gleichzeitigen Suche mehrerer Muster
- **Performance-Einordnung**: "in vielen Fällen dem Boyer-Moore-Algorithmus unterlegen"
- **Spezielle Anwendungsgebiete**: Plagiatserkennung und sehr lange Muster
- **Laufzeit-Erwartung**: O(n) bei geschickter Parameter-Wahl

### Unsere moderne Implementierung:
- **Las Vegas Version**: Explizite Verifikation eliminiert False Positives
- **Konsistente API**: Einheitliche Schnittstelle mit KMP und Boyer-Moore
- **Robuste Parameter-Wahl**: Rabin-Miller Test für sichere Primzahlen
- **Deutsche Dokumentation**: Vollständige Lokalisierung für akademischen Gebrauch
- **Umfassende Tests**: 63 Tests decken alle Szenarien ab

### Gewinnbringende Zusammenführung:
1. **Theoretische Basis**: Häberlein's Rolling Hash und Horner-Schema
2. **Praktische Robustheit**: Moderne Primzahl-Generierung und Fehlerbehandlung
3. **Anwendungsverständnis**: Klare Einordnung der Stärken und Schwächen
4. **Implementierungsqualität**: Konsistente API und umfassende Tests

## Fazit

Rabin-Karp ist ein vielseitiger String-Suchalgorithmus, der besonders für Multiple-Pattern-Suche und Anwendungen mit vielen verschiedenen Mustern geeignet ist. Häberlein's theoretische Fundierung zeigt klar die Nischenstärken auf (Plagiatserkennung, sehr lange Muster), während unsere moderne Implementierung diese Erkenntnisse in eine robuste, gut getestete und konsistente API umsetzt. Obwohl er keine Worst-Case-Garantien wie KMP bietet, ist er in seinen spezifischen Anwendungsgebieten sehr effizient und konzeptionell elegant.
