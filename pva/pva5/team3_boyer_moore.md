# PVA 5 - Team 3: Boyer-Moore

## 🎯 Aufgabenstellung

**Zeitrahmen:** 120 Minuten
**Team-Grösse:** 3-4 Studierende
**Algorithmus:** Boyer-Moore String-Suchalgorithmus

## 📚 Theoretische Grundlagen (30 Min)

### Buchkapitel
- **Hauptquelle:** Häberlein, Kapitel 7.4 "Der Boyer-Moore-Algorithmus"
- **Ergänzende Quellen:** Sedgewick & Wayne, Kapitel 5.3

### Zu analysierende Aspekte
1. **Grundprinzip:** Warum sucht Boyer-Moore von rechts nach links?
2. **Bad Character Rule:** Wie funktioniert die Zeichen-Heuristik?
3. **Good Suffix Rule:** Wie funktioniert die Suffix-Heuristik? (optional)
4. **Komplexität:**
   - Bester Fall: O(n/m) - sublinear!
   - Durchschnitt: O(n) bei grossen Alphabeten
   - Worst-Case: O(n×m) ohne Good Suffix Rule
5. **Vorteile:** Sehr schnell bei grossen Alphabeten und langen Mustern
6. **Nachteile:** Schlechte Performance bei kleinen Alphabeten

## 💻 Praktische Implementierung (60 Min)

### Aufgabe 1: Bad Character Table (20 Min)
Implementiert die Boyer-Moore Klasse mit Bad Character Rule:
```python
class BoyerMoore:
    def __init__(self, pattern: str):
        self.pattern = pattern
        self.bad_char = self._build_bad_char_table()

    def _build_bad_char_table(self):
        # Bad Character Table nach Häberlein konstruieren
        # Für jedes Zeichen: Position im Muster speichern

    def search(self, text: str) -> int:
        # Rückwärtssuche mit Bad Character Rule
```

### Aufgabe 2: Erweiterte Suchfunktionen (25 Min)
```python
def search_all(self, text: str) -> list:
    # Alle Fundstellen mit Boyer-Moore finden

def count(self, text: str) -> int:
    # Anzahl Vorkommen zählen

def _skip_distance(self, char: str, pos: int) -> int:
    # Berechne Sprungdistanz für gegebenes Zeichen
```

### Aufgabe 3: Anwendungsbeispiele (15 Min)
Implementiert 2-3 praktische Anwendungen:
1. **Texteditor:** Suche in grossen Dokumenten
2. **Genomanalyse:** DNA-Sequenz-Suche (grosse Alphabete)
3. **Log-Mining:** Pattern-Suche in Server-Logs

## 🧪 Testing & Validierung (15 Min)

### Testfälle entwickeln
```python
# Boyer-Moore spezifische Tests
bm = BoyerMoore("NEEDLE")
text = "HAYSTACK WITH NEEDLE IN IT"

# Besondere Testfälle für Boyer-Moore
- Grosse Alphabete: Englischer Text mit vielen verschiedenen Zeichen
- Lange Muster: Teste mit Mustern verschiedener Längen
- Worst-Case: "AAAB" in "AAAAAAAAAB" (kleine Alphabete)
- Best-Case: Muster mit vielen einzigartigen Zeichen
```

### Performance-Analyse
- Messt Sprungdistanzen bei verschiedenen Texten
- Vergleicht mit naiver Suche bei grossen Alphabeten
- Dokumentiert sublineare Performance (O(n/m))

## 📝 Dokumentation (15 Min)

### Markdown-Zusammenfassung erstellen
1. **Algorithmus-Beschreibung:** Warum rückwärts suchen?
2. **Bad Character Rule:** Wie werden Sprünge berechnet?
3. **Performance-Analyse:** Wann ist Boyer-Moore optimal?
4. **Alphabet-Einfluss:** Grosse vs. kleine Alphabete
5. **KI-Unterstützung:** Welche Prompts waren hilfreich?

### KI-Prompting-Strategien dokumentieren
- Wie habt ihr die Rückwärtssuche verstanden?
- Welche Visualisierungen haben geholfen?
- Wie habt ihr die Bad Character Table debugged?

## 🎤 Präsentation (5 Min)

### Präsentations-Struktur
1. **Algorithmus-Überblick** (1 Min): Rückwärtssuche erklären
2. **Live-Demo** (2 Min): Grosse Sprünge zeigen
3. **Performance-Demo** (1 Min): Sublineare Geschwindigkeit
4. **Erkenntnisse** (1 Min): Wann Boyer-Moore verwenden?

### Demo-Vorbereitung
- Beispiel mit grossen Sprüngen (viele verschiedene Zeichen)
- Visualisierung der Bad Character Table
- Performance-Vergleich mit messbaren Unterschieden

## 🎯 Bewertungskriterien

- ✅ **Funktionalität** (40%): Bad Character Rule korrekt implementiert
- ✅ **Code-Qualität** (20%): Sauberer, verständlicher Code
- ✅ **Dokumentation** (20%): Vollständige Markdown-Zusammenfassung
- ✅ **Präsentation** (20%): Klare Erklärung der Rückwärtssuche

## 💡 Hilfreiche Ressourcen

- **Häberlein Buch:** Kapitel 7.4 für Bad Character Rule
- **Visualisierung:** Zeichnet die Muster-Verschiebungen
- **KI-Tools:** Nutzt ChatGPT/Claude für Algorithmus-Verständnis
- **Testing:** Verwendet verschiedene Alphabet-Grössen

## 🔍 Besondere Herausforderungen

1. **Rückwärtssuche verstehen:** Warum von rechts nach links?
2. **Bad Character Table:** Korrekte Berechnung der Sprungdistanzen
3. **Edge Cases:** Was passiert bei Zeichen die nicht im Muster sind?
4. **Performance-Nachweis:** Sublineare Geschwindigkeit demonstrieren

## 📊 Häberlein's Beispiele

Nutzt die Beispiele aus dem Buch:
- **Aufgabe 7.8:** Bad Character Table für "ABAAABA"
- **Aufgabe 7.9:** Alternative Implementierung mit Array
- **Beispiel:** Suche "BAABA" in "ABAAABAAABA"

**Viel Erfolg! 🚀**
