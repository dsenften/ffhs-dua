Erstelle die Aufgabenstellungen für die Praktische Vertiefungsaufgabe (PVA) 5 zum Thema String-Algorithmen.

## Kontext

PVA 5 findet heute statt. Die Studierenden (BSc Informatik, 3. Semester) arbeiten in 4 Teams an unterschiedlichen String-Algorithmen. Im Gegensatz zu PVA 4 wird KEIN fertiger Quellcode bereitgestellt - die Studierenden sollen die Algorithmen selbst aus dem Häberlein-Buch und mit KI-Unterstützung implementieren.

**Zeitrahmen:** 120 Minuten Implementierung + 5 Minuten Präsentation pro Team

## Aufgaben

### 1. Verzeichnisstruktur vorbereiten
- Stelle sicher, dass `pva/pva5/` existiert
- Erstelle oder aktualisiere folgende Dateien:
  - `pva/pva5/team1_tries.md`
  - `pva/pva5/team2_kmp.md`
  - `pva/pva5/team3_boyer_moore.md`
  - `pva/pva5/team4_rabin_karp.md`
  - `pva/pva5/README.md` (Übersicht für alle Teams)

### 2. Gemeinsame Struktur für alle Team-Aufgaben

Jede Team-Datei soll folgende Struktur haben:

#### Header (Team-spezifisch)
```markdown
# PVA 5 - Team X: [Algorithmus-Name]

**Zeitrahmen:** 120 Minuten (exkl. Präsentation)
**Team-Grösse:** 3-4 Studierende
**Schwierigkeitsgrad:** [Mittel/Mittel-Hoch]
**Algorithmus-Typ:** [String-Algorithmus/Trie-Datenstruktur]

## 🎯 Lernziele
- Algorithmus aus Fachliteratur analysieren und verstehen
- Python-Implementierung mit Best Practices
- Effektive KI-Nutzung für akademische Problemlösung
- Teamarbeit und Präsentationskompetenz
```

#### Phase 1: Theoretische Grundlagen (30 Min)
- Literatur-Recherche (Häberlein-Buch, spezifisches Kapitel)
- Zu analysierende Aspekte:
  - Grundprinzip
  - Datenstrukturen (spezifisch für Algorithmus)
  - Komplexität (Best/Average/Worst Case, Speicher)
  - Stärken & Schwächen
  - Anwendungsfälle
- Deliverable: Handschriftliche Skizze, Verständnis im Team

#### Phase 2: Implementierung (60 Min)
- **Aufgabe 1:** Grundstruktur (20 Min)
  - Klassen-Skelett mit Konstruktor
  - Type-Hints, deutsche Docstrings
- **Aufgabe 2:** Kern-Algorithmus (25 Min)
  - Vollständige Implementierung (spezifische Methoden je Algorithmus)
  - Edge Cases behandeln
- **Aufgabe 3:** CLI & Testdaten (15 Min)
  - CLI-Interface für einfache Nutzung
  - Test-Szenarien mit data/strings/

#### Phase 3: Testing (15 Min)
- Basis-Test (Beispiel aus Buch)
- Edge Cases (leere Eingabe, nicht gefunden, mehrfache Vorkommen)
- Performance-Test (große Testdatei)
- Mindestens 5 Testfälle

#### Phase 4: Dokumentation (20 Min)
- Markdown-Zusammenfassung (`team_X_zusammenfassung.md`)
- Struktur:
  1. Algorithmus-Beschreibung
  2. Funktionsweise (mit Diagramm)
  3. Implementierungs-Details
  4. Performance-Analyse
  5. Anwendungsfälle
  6. **KI-Unterstützung** ⭐ **PFLICHT!**
- KI-Prompting-Strategien dokumentieren:
  - Welche Prompts verwendet?
  - Welche Patterns erfolgreich? (Chain-of-Thought, Few-Shot, etc.)
  - Welche Tools? (ChatGPT, Claude, Copilot)
  - Was hat nicht funktioniert?
  - Lessons Learned

#### Phase 5: Präsentation (10 Min Vorbereitung)
- Format: Keine Folien! Live-Demo + Code-Walkthrough
- Struktur (5 Min):
  1. Algorithmus-Überblick (1 Min)
  2. Live-Demo (2 Min)
  3. Code-Highlight (1 Min)
  4. KI & Learnings (1 Min)

#### Bewertungskriterien
- Funktionalität (35%): Algorithmus funktioniert, Tests bestehen
- Code-Qualität (20%): Sauber, dokumentiert, Best Practices
- Dokumentation (25%): Vollständig, KI-Prompting dokumentiert
- Präsentation (20%): Klar, Demo funktioniert

#### Zeitmanagement-Tabelle
| Phase | Zeit | Aktivität |
|-------|------|-----------|
| 1 | 0-30 Min | Theorie |
| 2 | 30-90 Min | Implementierung (60 Min) |
| 3 | 90-105 Min | Testing (15 Min) |
| 4 | 105-125 Min | Dokumentation (20 Min) |
| 5 | 125-135 Min | Präsentation Vorbereitung (10 Min) |

#### Ressourcen
- Häberlein-Buch (spezifisches Kapitel)
- Testdaten: `data/strings/`
- KI-Tools (ChatGPT/Claude/Copilot)

### 3. Team-spezifische Details

#### Team 1: Tries
- **Schwierigkeitsgrad:** Mittel
- **Häberlein-Kapitel:** 8.1 "Tries"
- **Datenstrukturen:** Trie-Knoten (Dictionary-basiert)
- **Komplexität:** O(m) für alle Operationen (m = Schlüssellänge)
- **Methoden:** put(), get(), delete(), keys(), keys_with_prefix(), keys_that_match(), longest_prefix_of()
- **Herausforderung:** Rekursive Traversierung
- **Highlight:** Präfix-Operationen (Autovervollständigung)
- **Testdaten:** shellsST.txt, words3.txt, tobe.txt
- **Anwendung:** Autovervollständigung, Wörterbuch, IP-Routing

#### Team 2: KMP (Knuth-Morris-Pratt)
- **Schwierigkeitsgrad:** Mittel-Hoch
- **Häberlein-Kapitel:** 7.2 "KMP-Algorithmus"
- **Datenstrukturen:** DFA (Deterministischer Finiter Automat)
- **Komplexität:** O(n) garantiert (kein Backtracking!)
- **Methoden:** __init__(pattern), search(text), search_all(text), count(text)
- **Herausforderung:** DFA-Konstruktion verstehen
- **Highlight:** Worst-Case O(n) Performance
- **Testdaten:** genomeTiny.txt, "abracadabra", "kakaokaki"
- **Anwendung:** Textsuche, DNA-Sequenzanalyse, Plagiatserkennung

#### Team 3: Boyer-Moore
- **Schwierigkeitsgrad:** Mittel-Hoch
- **Häberlein-Kapitel:** 7.3 "Boyer-Moore-Algorithmus"
- **Datenstrukturen:** Bad Character Table (Array[256])
- **Komplexität:** O(n/m) best case, O(n×m) worst case
- **Methoden:** __init__(pattern), search(text), search_all(text), count(text)
- **Herausforderung:** Bad Character Rule, Rückwärtsvergleich
- **Highlight:** Sublineare Performance bei großen Alphabeten
- **Testdaten:** tale.txt, mobydick.txt (lange Muster)
- **Anwendung:** Textsuche in Editoren, Suchmaschinen

#### Team 4: Rabin-Karp
- **Schwierigkeitsgrad:** Mittel
- **Häberlein-Kapitel:** 7.4 "Rabin-Karp-Algorithmus"
- **Datenstrukturen:** Rolling Hash (modulare Arithmetik)
- **Komplexität:** O(n+m) durchschnittlich, O(n×m) worst case
- **Methoden:** __init__(pattern), search(text), search_all(text), count(text)
- **Herausforderung:** Rolling Hash verstehen, Hash-Kollisionen behandeln
- **Highlight:** Multiple-Pattern-Suche möglich
- **Testdaten:** genomeVirus.txt, tale.txt, mobydick.txt
- **Anwendung:** Plagiatserkennung, DNA-Analyse, Multiple-Pattern-Suche

### 4. README.md erstellen

Erstelle `pva/pva5/README.md` mit:
- Übersicht über PVA 5
- Liste der 4 Teams und ihre Algorithmen
- Allgemeine Hinweise zur Bearbeitung
- Link zu Testdaten (data/strings/)
- Hinweis auf KI-Nutzung und Dokumentationspflicht
- Zeitplan

## Ausgabe

Nach der Erstellung der Dateien:
1. Zeige eine Zusammenfassung der erstellten/aktualisierten Dateien
2. Bestätige, dass alle 4 Teams vergleichbare Aufgabenstellungen haben
3. Weise auf wichtige Unterschiede zwischen den Algorithmen hin (Schwierigkeitsgrad)

## Wichtige Hinweise

- **Keine fertigen Lösungen:** Die Aufgaben sollen Leitfaden sein, KEIN Code
- **KI-Dokumentation PFLICHT:** Prompting-Strategien müssen dokumentiert werden
- **Realistische Zeitplanung:** 120 Minuten sind knapp, Prioritäten setzen!
- **Fachhochschul-Niveau:** Aufgaben sollen anspruchsvoll aber machbar sein
- **Vergleichbarkeit:** Alle Teams sollen ähnlichen Aufwand haben
