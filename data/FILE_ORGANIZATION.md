# Testdaten-Organisation

## ✅ Migration abgeschlossen

Alle Testdaten wurden erfolgreich von `algs4/data/` nach `/data/*` migriert und thematisch organisiert.

## Finale Struktur

### Thematische Kategorien

- **`data/fundamentals/`** - Union-Find, Stacks, Queues, Priority Queues
- **`data/sorting/`** - Sortieralgorithmen und Integer-Arrays
- **`data/graphs/`** - Graph-Algorithmen (gerichtet/ungerichtet/gewichtet)
- **`data/strings/`** - String-Algorithmen, Texte, Kompression
- **`data/compression/`** - Binäre Dateien und Kompressionsalgorithmen
- **`data/misc/`** - CSV-Dateien und sonstige Anwendungsdaten

### Größenkategorien (Fallback)

- **`data/small/`** - Dateien < 100KB
- **`data/medium/`** - Dateien 100KB - 10MB  
- **`data/large/`** - Dateien > 10MB

## Migration Statistik

- **Dateien migriert:** 82
- **Gesamtgröße:** 1.040,4 MB
- **Fehler:** 0
- **Ursprungsverzeichnis:** `algs4/data/` ✅ gelöscht

## Zugriff auf Testdaten

```python
# Beispiele für neue Pfade:
data_path = Path("data/sorting/1Kints.txt")
graph_data = Path("data/graphs/tinyG.txt") 
text_data = Path("data/strings/mobydick.txt")
```
