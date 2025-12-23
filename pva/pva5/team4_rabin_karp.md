# PVA 5 - Team 4: Rabin-Karp

## 🎯 Aufgabenstellung

**Zeitrahmen:** 120 Minuten
**Team-Grösse:** 3-4 Studierende
**Algorithmus:** Rabin-Karp String-Suchalgorithmus

## 📚 Theoretische Grundlagen (30 Min)

### Buchkapitel
- **Hauptquelle:** Häberlein, Kapitel 7.5 "Der Rabin-Karp-Algorithmus"
- **Ergänzende Quellen:** Sedgewick & Wayne, Kapitel 5.3

### Zu analysierende Aspekte
1. **Grundprinzip:** Wie funktioniert Hash-basierte String-Suche?
2. **Rolling Hash:** Wie wird der Hash effizient aktualisiert?
3. **Horner-Schema:** Wie optimiert man die Hash-Berechnung?
4. **Komplexität:**
   - Bester Fall: O(n + m) - lineare Laufzeit
   - Durchschnitt: O(n + m) bei guter Hash-Funktion
   - Worst-Case: O(n×m) bei vielen Kollisionen
5. **Vorteile:** Einfach zu implementieren, gut für Multiple-Pattern-Suche
6. **Nachteile:** Hash-Kollisionen, numerische Stabilität

## 💻 Praktische Implementierung (60 Min)

### Aufgabe 1: Rolling Hash (25 Min)
Implementiert die Rabin-Karp Klasse mit Rolling Hash:
```python
class RabinKarp:
    def __init__(self, pattern: str):
        self.pattern = pattern
        self.pattern_hash = self._hash(pattern)
        self.R = 256  # Alphabet-Grösse
        self.q = self._large_prime()  # Grosse Primzahl

    def _hash(self, s: str) -> int:
        # Hash-Wert mit Horner-Schema berechnen

    def _large_prime(self) -> int:
        # Grosse Primzahl für Modulo-Operation
```

### Aufgabe 2: Effiziente Suche (20 Min)
```python
def search(self, text: str) -> int:
    # Rolling Hash für effiziente Suche
    # Bei Hash-Match: explizite Verifikation!

def _update_hash(self, old_hash: int, old_char: str, new_char: str) -> int:
    # Rolling Hash Update nach Häberlein

def search_all(self, text: str) -> list:
    # Alle Fundstellen finden
```

### Aufgabe 3: Multiple-Pattern-Suche (15 Min)
Implementiert Häberlein's Hauptanwendung:
```python
def rabin_karp_multiple(patterns: list, text: str) -> dict:
    # Mehrere Muster gleichzeitig suchen
    # Hash-Set für alle Pattern-Hashes verwenden
```

## 🧪 Testing & Validierung (15 Min)

### Testfälle entwickeln
```python
# Rabin-Karp spezifische Tests
rk = RabinKarp("abc")
text = "abcabcabc"
```

**Besondere Testfälle:**
- Hash-Kollisionen: Verschiedene Strings mit gleichem Hash
- Rolling Hash: Korrekte Update-Berechnung
- Multiple Patterns: Gleichzeitige Suche mehrerer Muster
- Numerische Stabilität: Sehr lange Texte und Muster

### Hash-Qualität prüfen
- Testet die Hash-Verteilung bei verschiedenen Eingaben
- Messt die Anzahl Hash-Kollisionen
- Vergleicht verschiedene Primzahlen für Modulo

## 📝 Dokumentation (15 Min)

### Markdown-Zusammenfassung erstellen
1. **Algorithmus-Beschreibung:** Hash-basierte vs. Zeichen-basierte Suche
2. **Rolling Hash:** Wie funktioniert die effiziente Update-Formel?
3. **Kollisionsbehandlung:** Las Vegas vs. Monte Carlo Version
4. **Multiple-Pattern-Stärke:** Hauptvorteil nach Häberlein
5. **KI-Unterstützung:** Welche Prompts waren hilfreich?

### KI-Prompting-Strategien dokumentieren
- Wie habt ihr das Rolling Hash verstanden?
- Welche Hilfe bei der Modulo-Arithmetik?
- Wie habt ihr Hash-Kollisionen debugged?

## 🎤 Präsentation (5 Min)

### Präsentations-Struktur
1. **Algorithmus-Überblick** (1 Min): Hash-basierte Suche erklären
2. **Rolling Hash Demo** (2 Min): Effiziente Hash-Updates zeigen
3. **Multiple-Pattern Demo** (1 Min): Gleichzeitige Suche mehrerer Muster
4. **Erkenntnisse** (1 Min): Wann Rabin-Karp verwenden?

### Demo-Vorbereitung
- Visualisierung des Rolling Hash
- Multiple-Pattern-Suche mit 3-4 Mustern
- Hash-Kollision und Verifikation zeigen

## 🎯 Bewertungskriterien

- ✅ **Funktionalität** (40%): Rolling Hash korrekt implementiert
- ✅ **Code-Qualität** (20%): Sauberer, verständlicher Code
- ✅ **Dokumentation** (20%): Vollständige Markdown-Zusammenfassung
- ✅ **Präsentation** (20%): Klare Erklärung des Rolling Hash

## 💡 Hilfreiche Ressourcen

- **Häberlein Buch:** Kapitel 7.5 für Rolling Hash und Horner-Schema
- **Visualisierung:** Zeichnet die Hash-Berechnung Schritt für Schritt
- **KI-Tools:** Nutzt ChatGPT/Claude für Modulo-Arithmetik
- **Testing:** Verwendet grosse Primzahlen für bessere Hash-Verteilung

## 🔍 Besondere Herausforderungen

1. **Rolling Hash verstehen:** Effiziente Hash-Update-Formel
2. **Numerische Stabilität:** Overflow vermeiden mit Modulo-Arithmetik
3. **Hash-Kollisionen:** Explizite Verifikation implementieren
4. **Parameter-Wahl:** Gute Primzahl und Basis finden

## 📊 Häberlein's Schwerpunkte

Fokussiert auf Häberlein's Hauptargumente:
- **Multiple-Pattern-Suche:** Der Hauptvorteil von Rabin-Karp
- **Plagiatssoftware:** Praktische Anwendung aus dem Buch
- **Parameter-Wahl:** B = 256, M = 2^k - 1 für Performance
- **Horner-Schema:** Optimierte Hash-Berechnung

**Viel Erfolg! 🚀**
