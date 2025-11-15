# Coverage-Reports für ffhs-dua

Dieses Dokument beschreibt die Code-Coverage-Messung und -Berichterstattung für das ffhs-dua Projekt.

## Überblick

Das Projekt verwendet `pytest-cov` zur Messung der Code-Coverage. Die Coverage-Konfiguration ist in `pyproject.toml` definiert und wird automatisch bei jedem Test-Lauf gemessen.

**Aktuelle Coverage: 93.14%** ✅

## Coverage-Konfiguration

### pyproject.toml

```toml
[tool.coverage.run]
source = ["src/algs4"]
omit = [
    "*/tests/*",
    "*/test_*.py",
    "*/__pycache__/*",
]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "def __str__",
    "raise AssertionError",
    "raise NotImplementedError",
    "if __name__ == .__main__.:",
]
```

## Coverage-Reports generieren

### Terminal-Report mit fehlenden Zeilen

```bash
python3 -m pytest tests/ --cov=src.algs4 --cov-report=term-missing
```

### HTML-Report generieren

```bash
python3 -m pytest tests/ --cov=src.algs4 --cov-report=html
```

Der HTML-Report wird im Verzeichnis `htmlcov/` generiert und kann mit einem Browser geöffnet werden:

```bash
open htmlcov/index.html
```

### Beide Reports gleichzeitig

```bash
python3 -m pytest tests/ --cov=src.algs4 --cov-report=term-missing --cov-report=html
```

## Aktuelle Coverage-Statistiken

### Gesamt-Coverage: 93.14%

| Modul | Statements | Missed | Coverage | Status |
|-------|-----------|--------|----------|--------|
| `__init__.py` | 7 | 0 | 100.00% | ✅ |
| `errors/__init__.py` | 2 | 0 | 100.00% | ✅ |
| `errors/errors.py` | 8 | 0 | 100.00% | ✅ |
| `pva_1_fundamentals/__init__.py` | 5 | 0 | 100.00% | ✅ |
| `pva_1_fundamentals/bag.py` | 84 | 10 | 88.10% | ⚠️ |
| `pva_1_fundamentals/queue.py` | 47 | 0 | 100.00% | ✅ |
| `pva_1_fundamentals/stack.py` | 99 | 8 | 91.92% | ✅ |
| `pva_1_fundamentals/uf.py` | 124 | 13 | 89.52% | ✅ |
| `pva_2_sorting/__init__.py` | 5 | 0 | 100.00% | ✅ |
| `pva_2_sorting/heap.py` | 32 | 0 | 100.00% | ✅ |
| `pva_2_sorting/merge.py` | 41 | 0 | 100.00% | ✅ |
| `pva_2_sorting/quick.py` | 37 | 0 | 100.00% | ✅ |
| `pva_2_sorting/shell.py` | 23 | 0 | 100.00% | ✅ |
| `pva_3_searching/__init__.py` | 5 | 0 | 100.00% | ✅ |
| `pva_3_searching/avl.py` | 272 | 15 | 94.49% | ✅ |
| `pva_3_searching/bst.py` | 232 | 11 | 95.26% | ✅ |
| `pva_3_searching/hashing.py` | 193 | 29 | 84.97% | ⚠️ |
| `pva_3_searching/red_black_bst.py` | 315 | 19 | 93.97% | ✅ |

### Fehlende Coverage-Bereiche

#### `pva_1_fundamentals/bag.py` (88.10%)
- Zeilen 121-129: Spezielle Bag-Varianten
- Zeile 140: Edge-Case Handling
- Zeile 159: Fehlerbehandlung

#### `pva_1_fundamentals/stack.py` (91.92%)
- Zeile 147: ResizingArrayStack Spezialfall
- Zeile 194: FixedCapacityStack Grenzfall
- Zeilen 236-241: Fehlerbehandlung

#### `pva_1_fundamentals/uf.py` (89.52%)
- Zeilen 62, 155, 163, 191, 199, 214: Verschiedene UF-Varianten
- Zeilen 286, 295, 390, 398, 420, 440-441: Spezielle Fälle

#### `pva_3_searching/avl.py` (94.49%)
- Zeilen 432, 534, 578, 640, 663, 710, 712: Rotations-Edge-Cases
- Zeilen 813, 815, 819-826: Balancierungs-Spezialfälle

#### `pva_3_searching/bst.py` (95.26%)
- Zeilen 225, 253, 271, 296, 381, 425, 452, 487, 510, 557, 559: Verschiedene Lösch-Szenarien

#### `pva_3_searching/hashing.py` (84.97%)
- Zeilen 476-519: Resize-Operationen und Kollisionsbehandlung

#### `pva_3_searching/red_black_bst.py` (93.97%)
- Zeilen 403, 418, 442, 522, 594, 637, 698, 721, 768, 770: Rotations-Edge-Cases
- Zeilen 872, 874, 878-886: Balancierungs-Spezialfälle

## HTML-Report

Der HTML-Report bietet eine detaillierte, interaktive Ansicht der Coverage:

- **Farbcodierung**: Grün (covered), Rot (uncovered), Gelb (partial)
- **Zeilenweise Ansicht**: Jede Zeile zeigt, ob sie getestet wurde
- **Statistiken**: Zusammenfassung pro Datei und Modul
- **Trends**: Historische Coverage-Daten (wenn konfiguriert)

### HTML-Report öffnen

```bash
# macOS
open htmlcov/index.html

# Linux
xdg-open htmlcov/index.html

# Windows
start htmlcov/index.html
```

## Best Practices

### 1. Coverage-Ziele

- **Ziel**: Mindestens 90% Coverage
- **Kritische Module**: 95%+ Coverage angestrebt
- **Akzeptabel**: 85%+ Coverage für komplexe Module

### 2. Coverage-Ausschlüsse

Verwende `# pragma: no cover` für Code, der nicht getestet werden sollte:

```python
def __repr__(self):  # pragma: no cover
    return f"MyClass({self.value})"
```

### 3. Coverage in CI/CD

Coverage-Reports sollten in CI/CD-Pipelines generiert werden:

```bash
# GitHub Actions Beispiel
- name: Generate Coverage Report
  run: |
    python3 -m pytest tests/ --cov=src.algs4 --cov-report=xml

- name: Upload Coverage to Codecov
  uses: codecov/codecov-action@v3
  with:
    files: ./coverage.xml
```

### 4. Coverage-Trends verfolgen

Speichere Coverage-Reports über Zeit, um Trends zu verfolgen:

```bash
# Coverage-Report mit Datum speichern
python3 -m pytest tests/ --cov=src.algs4 --cov-report=html:htmlcov_$(date +%Y%m%d)
```

## Verbesserungsmöglichkeiten

### Hashing-Modul (84.97%)

Das Hashing-Modul hat die niedrigste Coverage. Mögliche Verbesserungen:

1. Tests für Resize-Operationen hinzufügen
2. Kollisionsbehandlung umfassender testen
3. Edge-Cases bei Load-Factor-Änderungen testen

### Bag-Modul (88.10%)

Das Bag-Modul könnte mit zusätzlichen Tests verbessert werden:

1. Spezielle Bag-Varianten testen
2. Edge-Cases bei leeren Bags testen
3. Fehlerbehandlung umfassender testen

## Weitere Ressourcen

- [Coverage.py Dokumentation](https://coverage.readthedocs.io/)
- [pytest-cov Dokumentation](https://pytest-cov.readthedocs.io/)
- [Code Coverage Best Practices](https://martinfowler.com/bliki/TestCoverage.html)
