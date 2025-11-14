# Scripts für ffhs-dua

Dieses Verzeichnis enthält hilfreiche Scripts für die Entwicklung und das Testen des ffhs-dua Projekts.

## Verfügbare Scripts

### Coverage-Report Generator

Generiert Code-Coverage-Reports in verschiedenen Formaten.

#### Bash-Version

```bash
./scripts/generate_coverage.sh [--html] [--xml] [--all]
```

**Optionen:**
- `--html` - Generiere HTML-Report (interaktive Ansicht)
- `--xml` - Generiere XML-Report (für CI/CD)
- `--all` - Generiere alle Reports

**Beispiele:**

```bash
# Nur Terminal-Report mit fehlenden Zeilen
./scripts/generate_coverage.sh

# Terminal + HTML-Report
./scripts/generate_coverage.sh --html

# Alle Reports (Terminal, HTML, XML)
./scripts/generate_coverage.sh --all
```

#### Python-Version

```bash
python3 scripts/generate_coverage.py [--html] [--xml] [--all]
```

**Optionen:**
- `--html` - Generiere HTML-Report
- `--xml` - Generiere XML-Report
- `--all` - Generiere alle Reports

**Beispiele:**

```bash
# Nur Terminal-Report
python3 scripts/generate_coverage.py

# Terminal + HTML-Report
python3 scripts/generate_coverage.py --html

# Alle Reports
python3 scripts/generate_coverage.py --all
```

### Output-Formate

#### Terminal-Report

Zeigt Coverage-Statistiken direkt in der Konsole:

```
Name                                    Stmts   Miss   Cover   Missing
-----------------------------------------------------------------------
src/algs4/pva_2_sorting/shell.py           23      0 100.00%
src/algs4/pva_2_sorting/quick.py           37      0 100.00%
src/algs4/pva_3_searching/hashing.py      193     30  84.46%   424, 476-519
-----------------------------------------------------------------------
TOTAL                                   1531    106  93.08%
```

#### HTML-Report

Interaktive Ansicht mit Farbcodierung:

```bash
# Öffne den HTML-Report
open htmlcov/index.html
```

Features:
- Farbcodierung (Grün = covered, Rot = uncovered)
- Zeilenweise Ansicht
- Statistiken pro Datei
- Navigierbare Struktur

#### XML-Report

Maschinenlesbares Format für CI/CD-Integration:

```bash
# Datei: coverage.xml
# Verwendung in GitHub Actions, GitLab CI, etc.
```

## Coverage-Ziele

| Kategorie | Ziel | Aktuell |
|-----------|------|---------|
| Gesamt | ≥90% | 93.08% ✅ |
| Kritische Module | ≥95% | Variiert |
| Akzeptabel | ≥85% | Alle erfüllt ✅ |

## Häufig verwendete Befehle

### Coverage-Report mit fehlenden Zeilen anzeigen

```bash
python3 -m pytest tests/ --cov=src.algs4 --cov-report=term-missing
```

### HTML-Report generieren und öffnen

```bash
python3 scripts/generate_coverage.py --html
open htmlcov/index.html
```

### Coverage für spezifisches Modul

```bash
python3 -m pytest tests/test_sorting/ --cov=src.algs4.pva_2_sorting --cov-report=term-missing
```

### Coverage-Report mit Ausschlüssen

```bash
python3 -m pytest tests/ --cov=src.algs4 --cov-report=term-missing --cov-report=html
```

## Integration in CI/CD

### GitHub Actions

```yaml
- name: Generate Coverage Report
  run: python3 scripts/generate_coverage.py --xml

- name: Upload Coverage to Codecov
  uses: codecov/codecov-action@v3
  with:
    files: ./coverage.xml
```

### GitLab CI

```yaml
coverage:
  script:
    - python3 scripts/generate_coverage.py --xml
  coverage: '/TOTAL.*\s+(\d+%)$/'
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: coverage.xml
```

## Konfiguration

Die Coverage-Konfiguration befindet sich in `pyproject.toml`:

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

## Tipps und Tricks

### 1. Coverage-Trends verfolgen

Speichere Coverage-Reports mit Datum:

```bash
mkdir -p coverage_history
python3 scripts/generate_coverage.py --html
cp -r htmlcov coverage_history/htmlcov_$(date +%Y%m%d)
```

### 2. Nur nicht abgedeckte Zeilen anzeigen

```bash
python3 -m coverage report --skip-covered
```

### 3. Coverage-Daten löschen

```bash
rm -rf .coverage htmlcov/ coverage.xml
```

### 4. Coverage für einzelne Datei

```bash
python3 -m coverage report src/algs4/pva_2_sorting/shell.py
```

## Weitere Ressourcen

- [Coverage.py Dokumentation](https://coverage.readthedocs.io/)
- [pytest-cov Dokumentation](https://pytest-cov.readthedocs.io/)
- [docs/coverage.md](../docs/coverage.md) - Detaillierte Coverage-Dokumentation
