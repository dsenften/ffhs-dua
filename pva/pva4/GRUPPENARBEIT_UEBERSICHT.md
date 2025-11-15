# PVA 4: Gruppenarbeit Übersicht

## Agenda für die Präsenzveranstaltung

| Zeit | Dauer | Aktivität |
|------|-------|-----------|
| 12:45 | 10' | Begrüssung, Rückblick, Agenda |
| 12:55 | 15' | Graphen & Repräsentation (Schnelldurchlauf) |
| 13:10 | 15' | Kurze Intro zu allen 4 Themen |
| 13:25 | 60' | **Gruppenarbeit** (mit Betreuer-Rotation) |
| 14:25 | 15' | **PAUSE** |
| 14:40 | 45' | **Präsentationen** (ca. 10-12' pro Gruppe) |
| 15:25 | 15' | Diskussion & Vergleiche |
| 15:40 | 20' | Feedback & Fragen |
| 16:00 | - | Ende |

## Gruppen und Themen

### Gruppe 1: Breiten- und Tiefensuche (BFS & DFS)

**Dokumentation:** `gruppe_1_bfs_dfs.adoc`

**Themen:**
- Breitensuche (BFS)
- Tiefensuche (DFS)
- Topologische Sortierung

**Implementierungen:**
- `src/algs4/pva_4_graphs/bfs.py`
- `src/algs4/pva_4_graphs/dfs_paths.py`
- `src/algs4/pva_4_graphs/topological.py`

**Testdaten:**
- `data/graphs/tinyEWG.txt` (8 Knoten, 16 Kanten)
- `data/graphs/tinyDAG.txt` (13 Knoten, 22 Kanten)
- `data/graphs/mediumEWG.txt` (250 Knoten)

---

### Gruppe 2: Kürzeste Wege (Shortest Paths)

**Dokumentation:** `gruppe_2_kuerzeste_wege.adoc`

**Themen:**
- Dijkstra's Algorithmus
- Pfadrekonstruktion
- Anwendungen

**Implementierungen:**
- `src/algs4/pva_4_graphs/dijkstra_sp.py`

**Testdaten:**
- `data/graphs/tinyEWD.txt` (8 Knoten, 15 Kanten)
- `data/graphs/mediumEWD.txt` (250 Knoten)
- `data/graphs/largeEWD.txt` (1000+ Knoten)

---

### Gruppe 3: Spannbäume (Minimum Spanning Trees)

**Dokumentation:** `gruppe_3_spannbaeume.adoc`

**Themen:**
- Kruskal's Algorithmus
- Prim's Algorithmus
- Vergleich und Trade-offs

**Implementierungen:**
- `src/algs4/pva_4_graphs/kruskal_mst.py`
- `src/algs4/pva_4_graphs/prim_mst.py`

**Testdaten:**
- `data/graphs/tinyEWG.txt` (8 Knoten, 16 Kanten)
- `data/graphs/mediumEWG.txt` (250 Knoten)
- `data/graphs/largeEWG.txt` (1000+ Knoten)

---

### Gruppe 4: Union-Find (Disjoint Set Union)

**Dokumentation:** `gruppe_4_union_find.adoc`

**Themen:**

- Union-Find Datenstruktur
- Optimierungen (Path Compression, Union by Rank)
- Anwendungen (Zyklenerkennung, Kruskal)

**Implementierungen:**

- `src/algs4/pva_1_fundamentals/uf.py`

**Testdaten:**

- `data/graphs/tinyEWG.txt`
- `data/graphs/mediumEWG.txt`
- `data/graphs/largeEWG.txt`

## Vorbereitung für Gruppen

### Für jede Gruppe

1. **Dokumentation lesen**
   - Öffne `gruppe_X_THEMA.adoc`
   - Verstehe die Algorithmen
   - Studiere die Pseudocodes

2. **Code studieren**
   - Schaue dir die Implementierungen an
   - Verstehe die Datenstrukturen
   - Lese die Tests

3. **Übungen durcharbeiten**
   - Führe die Übungen durch
   - Experimentiere mit Testdaten
   - Dokumentiere Ergebnisse

4. **Präsentation vorbereiten**
   - Nutze `praesentations_template.adoc`
   - Bereite Live-Demo vor
   - Übe die Präsentation

### Ressourcen für alle

- **Buch:** Praktische Algorithmik mit Python, Tobias Häberlein
- **Code:** `src/algs4/pva_4_graphs/` und `src/algs4/pva_1_fundamentals/`
- **Tests:** `tests/test_graphs/` und `tests/test_fundamentals/`
- **Testdaten:** `data/graphs/`

## Präsentations-Ablauf

### Zeitplan

| Gruppe | Thema | Zeit |
|--------|-------|------|
| 1 | BFS & DFS | 14:40 - 14:52 |
| 2 | Kürzeste Wege | 14:52 - 15:04 |
| 3 | Spannbäume | 15:04 - 15:16 |
| 4 | Union-Find | 15:16 - 15:28 |

### Bewertung

Jede Präsentation wird bewertet nach:
- Verständnis des Algorithmus (30%)
- Code-Qualität & Demo (25%)
- Präsentation & Kommunikation (25%)
- Fragen & Diskussion (20%)

## Tipps für erfolgreiche Gruppenarbeit

- [ ] Teilt die Aufgaben auf
- [ ] Kommuniziert regelmäßig
- [ ] Testet alles vorher
- [ ] Habt einen Plan B
- [ ] Seid enthusiastisch!
- [ ] Helft euch gegenseitig
- [ ] Stellt Fragen wenn etwas unklar ist

## Häufig gestellte Fragen

**F: Wie lange sollte die Präsentation sein?**
A: 10-12 Minuten. Nutze das Zeitbudget: 2-3 Min Erklärung, 3-4 Min Demo, 2-3 Min Ergebnisse, 1-2 Min Fragen.

**F: Was wenn der Code nicht funktioniert?**
A: Habe Screenshots oder eine Backup-Demo vorbereitet. Erkläre trotzdem den Algorithmus.

**F: Können wir den Code live schreiben?**
A: Besser nicht. Zeige vorbereiteten Code und erkläre ihn.

**F: Wie viele Personen sollten präsentieren?**
A: Mindestens 2 Personen pro Gruppe. Teilt die Präsentation auf.

**F: Können wir Folien verwenden?**
A: Ja, aber nicht zu viele. Fokus auf Live-Demo und Code.

## Kontakt & Support

- **Fragen zur Dokumentation:** Siehe `gruppe_X_THEMA.adoc`
- **Fragen zum Code:** Siehe Tests und Docstrings
- **Fragen zur Präsentation:** Siehe `praesentations_template.adoc`
- **Technische Probleme:** Kontaktiere den Betreuer

## Viel Erfolg! 🚀

Wir freuen uns auf eure Präsentationen!
