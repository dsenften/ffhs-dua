Analysiere und passe den Algorithmus "{{arg1}}" an die Entwicklungsrichtlinien an.

## Anweisungen

1. **Argument-Validierung:**
   - Falls kein Argument angegeben wurde ({{arg1}} ist leer), frage den Benutzer mit dem AskUserQuestion Tool nach der zu analysierenden Datei oder dem Code
   - Das Argument sollte ein Dateipfad sein (z.B. `src/algs4/pva_5_strings/rabin_karp.py`) oder eine klare Beschreibung des Algorithmus
   - Validiere, dass die Datei existiert, bevor du fortfährst

2. **Datei-Analyse:**
   - Lese die angegebene Datei vollständig mit dem Read Tool
   - Identifiziere den Typ des Algorithmus (Fundamentals, Sorting, Searching, Graphs, Strings)
   - Analysiere die aktuelle Implementierung:
     - Code-Struktur und Klassendesign
     - Docstrings und Kommentare
     - Type-Hints und Generics
     - CLI-Interface (falls vorhanden)
     - Methoden-Signaturen und Return-Types
     - Fehlerbehandlung
   - Vergleiche mit den Entwicklungsrichtlinien aus CLAUDE.md

3. **Code-Anpassung:**
   - Passe den Code an die Entwicklungsrichtlinien an:
     - **Sprache**: Deutsche Dokumentation, Kommentare und Variablennamen
     - **Type-Hints**: Für alle öffentlichen Methoden
     - **Docstrings**: Google-Style auf Deutsch mit Args/Returns/Raises
     - **Defensive Programmierung**: Assertions für interne Invarianten
     - **Generics**: `TypeVar("T")` für typensichere Container
     - **CLI-Interface**: Falls zutreffend, mit `--quiet` Flag für Performance-Tests
     - **Klassenmethoden**: `@classmethod` für stateless Algorithmen
     - **Fehlerbehandlung**: Deutsche Fehlermeldungen mit benutzerdefinierten Exceptions
   - Stelle sicher, dass die Implementierung konsistent mit anderen Algorithmen derselben Kategorie ist
   - Verwende das Edit Tool für alle Änderungen am Code

4. **Dokumentations-Aktualisierung:**
   - **CLAUDE.md aktualisieren**: Füge oder aktualisiere die Beschreibung des Algorithmus in der entsprechenden PVA-Sektion
     - Komplexität (Best/Average/Worst Case)
     - Besondere Eigenschaften
     - Anwendungsfälle
     - Methoden-Übersicht
   - **README.md aktualisieren**: Falls ein pva_X_category/README.md existiert, aktualisiere es
   - **__init__.py aktualisieren**: Stelle sicher, dass der Algorithmus in `src/algs4/pva_X_category/__init__.py` exportiert wird
   - **data/*/README.md aktualisieren**: Ergänze Beispiele für die Verwendung mit Testdaten
     - Für String-Algorithmen: `data/strings/README.md`
     - Für Sortieralgorithmen: `data/sorting/README.md`
     - Für Graph-Algorithmen: `data/graphs/README.md`
     - Etc.
   - Füge CLI-Beispiele, Python-API-Beispiele und Performance-Vergleiche hinzu

5. **Test-Validierung:**
   - Überprüfe, ob Tests für den Algorithmus existieren
   - Führe die Tests mit `python3 -m pytest tests/test_category/test_algorithm.py -v` aus
   - Falls Tests fehlen oder fehlschlagen, informiere den Benutzer
   - Stelle sicher, dass die Code-Coverage hoch bleibt (>90%)

6. **Konsistenz-Überprüfung:**
   - Vergleiche die Implementierung mit ähnlichen Algorithmen derselben Kategorie
   - Stelle sicher, dass folgende Aspekte konsistent sind:
     - Methoden-Namenskonventionen (z.B. `is_empty()`, `size()`)
     - Standard-Methoden (`__len__()`, `__iter__()`, `__repr__()`)
     - Property-Zugriff (read-only via `@property` für wichtige Attribute)
     - Error-Handling-Muster
     - CLI-Argument-Parsing
     - Timing-Utilities-Integration

## Fehlerbehandlung

- Falls die angegebene Datei nicht existiert, informiere den Benutzer und frage nach dem korrekten Pfad
- Falls der Algorithmus nicht in CLAUDE.md erwähnt wird, füge eine neue Sektion hinzu
- Falls keine Tests existieren, weise den Benutzer darauf hin, dass Tests erstellt werden sollten
- Falls die Anpassungen Breaking Changes verursachen würden, frage den Benutzer um Bestätigung

## Qualitätskriterien

Die Analyse ist vollständig, wenn:
- ✅ Der Code alle Entwicklungsrichtlinien erfüllt
- ✅ Deutsche Docstrings und Kommentare vorhanden sind
- ✅ Type-Hints für alle öffentlichen Methoden vorhanden sind
- ✅ CLAUDE.md aktualisiert wurde
- ✅ Relevante README.md-Dateien aktualisiert wurden
- ✅ __init__.py Export vorhanden ist
- ✅ CLI-Beispiele und Python-API-Beispiele in data/*/README.md dokumentiert sind
- ✅ Alle Tests bestehen
- ✅ Die Implementierung konsistent mit ähnlichen Algorithmen ist

## Beispiel-Aufruf

```bash
# Mit Dateipfad-Argument
/analyse-algorithm src/algs4/pva_5_strings/rabin_karp.py

# Ohne Argument (interaktiv)
/analyse-algorithm
```

Dies analysiert die angegebene Algorithmus-Datei, passt sie an die Entwicklungsrichtlinien an und aktualisiert alle relevanten Dokumentationsdateien.
