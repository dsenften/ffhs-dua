# PVA 5 - Team 1: Tries (Präfix-Bäume)

## 🎯 Aufgabenstellung

**Zeitrahmen:** 120 Minuten
**Team-Grösse:** 3-4 Studierende
**Algorithmus:** Tries (Trie Symbol Table)

## 📚 Theoretische Grundlagen (30 Min)

### Buchkapitel
- **Hauptquelle:** Häberlein, Kapitel 8.1 "Tries"
- **Ergänzende Quellen:** Sedgewick & Wayne, Kapitel 5.2

### Zu analysierende Aspekte
1. **Grundprinzip:** Wie funktioniert ein Trie als Baum-Datenstruktur?
2. **Knotenstruktur:** Wie werden Zeichen und Werte in Knoten gespeichert?
3. **Operationen:** put(), get(), delete(), keys(), keysWithPrefix()
4. **Komplexität:**
   - Zeit: O(m) für alle Operationen (m = Schlüssellänge)
   - Raum: O(ALPHABET_SIZE × N × M) im Worst-Case
5. **Vorteile:** Präfix-Operationen, keine String-Vergleiche
6. **Nachteile:** Speicherverbrauch bei grossen Alphabeten

## 💻 Praktische Implementierung (60 Min)

### Aufgabe 1: Grundstruktur (20 Min)
Implementiert eine `TrieST` Klasse mit folgenden Komponenten:
```python
class TrieST:
    def __init__(self):
        # Initialisierung

    def put(self, key: str, value):
        # Schlüssel-Wert-Paar einfügen

    def get(self, key: str):
        # Wert für Schlüssel abrufen

    def contains(self, key: str) -> bool:
        # Prüfen ob Schlüssel existiert
```

### Aufgabe 2: Erweiterte Operationen (25 Min)
```python
def keys(self) -> list:
    # Alle Schlüssel in alphabetischer Reihenfolge

def keys_with_prefix(self, prefix: str) -> list:
    # Alle Schlüssel mit gegebenem Präfix

def keys_that_match(self, pattern: str) -> list:
    # Wildcard-Suche mit '.' als Platzhalter

def longest_prefix_of(self, query: str) -> str:
    # Längster Präfix von query der im Trie existiert
```

### Aufgabe 3: Anwendungsbeispiele (15 Min)
Implementiert 2-3 praktische Anwendungen:
1. **Autovervollständigung:** Vorschläge basierend auf Präfix
2. **Wörterbuch:** Rechtschreibprüfung und Wortsuche
3. **IP-Routing:** Längster Präfix-Match (optional)

## 🧪 Testing & Validierung (15 Min)

### Testfälle entwickeln
```python
# Basis-Tests
trie = TrieST()
trie.put("she", 0)
trie.put("sells", 1)
trie.put("sea", 2)
trie.put("shells", 3)

# Edge Cases testen
- Leerer Trie
- Überschreibung existierender Schlüssel
- Präfix-Konflikte ("sea" vs "seashells")
- Wildcard-Suche mit verschiedenen Mustern
```

## 📝 Dokumentation (15 Min)

### Markdown-Zusammenfassung erstellen
1. **Algorithmus-Beschreibung:** Wie funktioniert ein Trie?
2. **Implementierungs-Details:** Wichtige Design-Entscheidungen
3. **Performance-Analyse:** Gemessene vs. theoretische Komplexität
4. **Anwendungsfälle:** Wo sind Tries besonders nützlich?
5. **KI-Unterstützung:** Welche Prompts waren hilfreich?

### KI-Prompting-Strategien dokumentieren
- Welche Prompts haben bei der Implementierung geholfen?
- Wie habt ihr komplexe Algorithmus-Teile erklärt bekommen?
- Welche Debugging-Strategien waren erfolgreich?

## 🎤 Präsentation (5 Min)

### Präsentations-Struktur
1. **Algorithmus-Überblick** (1 Min): Was ist ein Trie?
2. **Live-Demo** (2 Min): Autovervollständigung zeigen
3. **Besonderheiten** (1 Min): Präfix-Operationen hervorheben
4. **Erkenntnisse** (1 Min): Was haben wir gelernt?

### Demo-Vorbereitung
- Funktionsfähige Autovervollständigung
- Beispiel mit deutschen Wörtern
- Wildcard-Suche demonstrieren

## 🎯 Bewertungskriterien

- ✅ **Funktionalität** (40%): Alle Operationen implementiert und getestet
- ✅ **Code-Qualität** (20%): Sauberer, verständlicher Code
- ✅ **Dokumentation** (20%): Vollständige Markdown-Zusammenfassung
- ✅ **Präsentation** (20%): Klare Erklärung und Demo

## 💡 Hilfreiche Ressourcen

- **Häberlein Buch:** Kapitel 8.1 für Grundlagen
- **Visualisierung:** Zeichnet den Trie-Baum für euer Beispiel
- **KI-Tools:** Nutzt ChatGPT/Claude für Implementierungs-Details
- **Testing:** Python's `assert` für einfache Tests

**Viel Erfolg! 🚀**
