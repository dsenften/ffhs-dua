# PVA 5 - Team 2: KMP (Knuth-Morris-Pratt)

## 🎯 Aufgabenstellung

**Zeitrahmen:** 120 Minuten
**Team-Grösse:** 3-4 Studierende
**Algorithmus:** Knuth-Morris-Pratt String-Suchalgorithmus

## 📚 Theoretische Grundlagen (30 Min)

### Buchkapitel
- **Hauptquelle:** Häberlein, Kapitel 7.3 "Der Knuth-Morris-Pratt-Algorithmus"
- **Ergänzende Quellen:** Sedgewick & Wayne, Kapitel 5.3

### Zu analysierende Aspekte
1. **Grundprinzip:** Wie vermeidet KMP das Backtracking im Text?
2. **DFA-Konstruktion:** Wie wird der Deterministische Finite Automat aufgebaut?
3. **Präfix-Funktion:** Wie berechnet man die "failure function"?
4. **Komplexität:**
   - Preprocessing: O(m) für DFA-Aufbau
   - Suche: O(n) garantiert, auch im Worst-Case
   - Raum: O(m × R) für DFA (R = Alphabet-Grösse)
5. **Vorteile:** Lineare Laufzeit garantiert, kein Backtracking
6. **Nachteile:** Komplexere Implementierung, Speicherverbrauch für DFA

## 💻 Praktische Implementierung (60 Min)

### Aufgabe 1: DFA-Konstruktion (25 Min)
Implementiert die KMP-Klasse mit DFA-Aufbau:
```python
class KMP:
    def __init__(self, pattern: str):
        self.pattern = pattern
        self.dfa = self._build_dfa()

    def _build_dfa(self):
        # Deterministischen Finiten Automaten konstruieren
        # Häberlein's Algorithmus aus Kapitel 7.3 verwenden

    def search(self, text: str) -> int:
        # Erste Fundstelle zurückgeben (-1 wenn nicht gefunden)
```

### Aufgabe 2: Erweiterte Suchfunktionen (20 Min)
```python
def search_all(self, text: str) -> list:
    # Alle Fundstellen als Liste zurückgeben

def count(self, text: str) -> int:
    # Anzahl der Vorkommen zählen

@property
def pattern(self) -> str:
    # Read-only Zugriff auf das Muster
```

### Aufgabe 3: Anwendungsbeispiele (15 Min)
Implementiert 2-3 praktische Anwendungen:
1. **Textsuche:** Suche in grossen Dokumenten
2. **DNA-Analyse:** Sequenz-Matching in Genom-Daten
3. **Log-Analyse:** Pattern-Matching in Server-Logs

## 🧪 Testing & Validierung (15 Min)

### Testfälle entwickeln
```python
# Basis-Tests
kmp = KMP("ABCDAB")
text = "ABC ABCDAB ABCDABCDABDE"

# Spezielle KMP-Testfälle
- Wiederholende Muster: "AAAA" in "AAAAAAAAA"
- Präfix-Suffix-Überlappung: "ABCAB"
- Worst-Case für naive Suche: "AAAB" in "AAAAAAAAAB"
- Kein Vorkommen: "XYZ" in "ABCDEF"
```

### Performance-Vergleich
- Messt die Laufzeit gegen naive String-Suche
- Testet mit verschiedenen Textgrössen (100, 1000, 10000 Zeichen)
- Dokumentiert die O(n)-Garantie

## 📝 Dokumentation (15 Min)

### Markdown-Zusammenfassung erstellen
1. **Algorithmus-Beschreibung:** Wie funktioniert der DFA?
2. **DFA-Konstruktion:** Schritt-für-Schritt Erklärung
3. **Laufzeit-Analyse:** Warum ist KMP linear?
4. **Vergleich:** KMP vs. naive Suche vs. Boyer-Moore
5. **KI-Unterstützung:** Welche Prompts waren hilfreich?

### KI-Prompting-Strategien dokumentieren
- Wie habt ihr die DFA-Konstruktion verstanden?
- Welche Debugging-Techniken waren erfolgreich?
- Wie habt ihr komplexe Algorithmus-Schritte erklärt bekommen?

## 🎤 Präsentation (5 Min)

### Präsentations-Struktur
1. **Algorithmus-Überblick** (1 Min): Was macht KMP besonders?
2. **DFA-Demo** (2 Min): Zeigt den Automaten für ein Beispiel
3. **Performance-Demo** (1 Min): Laufzeit-Vergleich zeigen
4. **Erkenntnisse** (1 Min): Warum ist lineare Laufzeit wichtig?

### Demo-Vorbereitung
- Visualisierung des DFA für euer Muster
- Performance-Vergleich mit messbaren Zeiten
- Beispiel mit problematischem Pattern für naive Suche

## 🎯 Bewertungskriterien

- ✅ **Funktionalität** (40%): DFA korrekt implementiert, alle Suchfunktionen
- ✅ **Code-Qualität** (20%): Sauberer, verständlicher Code
- ✅ **Dokumentation** (20%): Vollständige Markdown-Zusammenfassung
- ✅ **Präsentation** (20%): Klare Erklärung der DFA-Konstruktion

## 💡 Hilfreiche Ressourcen

- **Häberlein Buch:** Kapitel 7.3 für DFA-Konstruktion
- **Visualisierung:** Zeichnet den DFA für euer Beispielmuster
- **KI-Tools:** Nutzt ChatGPT/Claude für DFA-Verständnis
- **Testing:** Verwendet `time.perf_counter()` für Performance-Tests

## 🔍 Besondere Herausforderungen

1. **DFA-Konstruktion verstehen:** Der schwierigste Teil des Algorithmus
2. **Präfix-Funktion:** Wie berechnet man die "failure function"?
3. **Debugging:** DFA-Zustände bei der Suche verfolgen
4. **Performance-Nachweis:** O(n)-Garantie praktisch demonstrieren

**Viel Erfolg! 🚀**
