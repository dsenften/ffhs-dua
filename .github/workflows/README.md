# GitHub Actions Workflows für ffhs-dua

Dieses Verzeichnis enthält GitHub Actions Workflows für Continuous Integration und Continuous Deployment (CI/CD).

## Verfügbare Workflows

### 1. Tests (`tests.yml`)

**Trigger:** Push und Pull Requests auf `develop` und `main`

**Was wird getestet:**
- ✅ Linting mit ruff
- ✅ Type-Checking mit mypy
- ✅ Unit-Tests mit pytest
- ✅ Code-Coverage-Reports

**Plattformen:**
- Ubuntu (Linux)
- macOS
- Windows

**Python-Version:** 3.13

**Artefakte:**
- Coverage-Reports (hochgeladen zu Codecov)

### 2. Code Quality (`code-quality.yml`)

**Trigger:** Push und Pull Requests auf `develop` und `main`

**Was wird überprüft:**
- ✅ Code-Formatierung mit ruff
- ✅ Type-Hints mit mypy
- ✅ Sicherheit mit bandit
- ✅ Print-Statements (sollten nicht in Production-Code sein)
- ✅ TODO/FIXME-Kommentare

**Plattform:** Ubuntu (Linux)

**Python-Version:** 3.13

### 3. Documentation (`documentation.yml`)

**Trigger:** Push auf `develop` und `main` (nur wenn Docs geändert)

**Was wird überprüft:**
- ✅ Dokumentations-Dateien existieren
- ✅ Markdown-Validierung
- ✅ Broken Links
- ✅ TODO/FIXME in Dokumentation

**Plattform:** Ubuntu (Linux)

### 4. Release (`release.yml`)

**Trigger:** Git Tags mit Format `v*` (z.B. `v1.0.0`)

**Was wird gemacht:**
- ✅ Version-Konsistenz überprüft
- ✅ Tests ausgeführt
- ✅ Distribution gebaut
- ✅ Release auf GitHub erstellt
- ✅ Artefakte hochgeladen

**Plattform:** Ubuntu (Linux)

**Python-Version:** 3.13

## Workflow-Status

Der Status aller Workflows wird im README angezeigt:

```markdown
![Tests](https://github.com/talent-factory/ffhs-dua/workflows/Tests/badge.svg)
![Code Quality](https://github.com/talent-factory/ffhs-dua/workflows/Code%20Quality/badge.svg)
![Documentation](https://github.com/talent-factory/ffhs-dua/workflows/Documentation/badge.svg)
```

## Verwendung

### Tests lokal ausführen

```bash
# Alle Tests
pytest tests/ -v

# Mit Coverage
pytest tests/ --cov=src.algs4 --cov-report=html

# Nur schnelle Tests
pytest tests/ -m "not slow"
```

### Code-Qualität lokal überprüfen

```bash
# Linting
ruff check src/ tests/

# Formatierung
ruff format src/ tests/

# Type-Checking
mypy src/algs4

# Sicherheit
bandit -r src/
```

### Release erstellen

```bash
# Version aktualisieren in:
# 1. pyproject.toml
# 2. src/algs4/__init__.py

# Git Tag erstellen
git tag v1.0.0
git push origin v1.0.0

# GitHub Actions wird automatisch:
# 1. Tests ausführen
# 2. Distribution bauen
# 3. Release erstellen
# 4. Artefakte hochladen
```

## Konfiguration

### Secrets

Folgende Secrets können in GitHub konfiguriert werden:

- `CODECOV_TOKEN` - Token für Codecov (optional, für private Repos)
- `GITHUB_TOKEN` - Wird automatisch bereitgestellt

### Branch Protection Rules

Empfohlene Branch Protection Rules für `main`:

1. **Require status checks to pass before merging:**
   - Tests
   - Code Quality
   - Documentation

2. **Require code reviews before merging:**
   - Mindestens 1 Review erforderlich

3. **Require branches to be up to date before merging:**
   - Aktiviert

4. **Require conversation resolution before merging:**
   - Aktiviert

## Troubleshooting

### Tests schlagen fehl

1. Überprüfe Python-Version: `python3 --version`
2. Installiere Dependencies: `pip install -e ".[dev]"`
3. Führe Tests lokal aus: `pytest tests/ -v`

### Linting-Fehler

```bash
# Automatisch beheben
ruff check --fix src/ tests/
ruff format src/ tests/
```

### Type-Checking-Fehler

```bash
# Überprüfe Type-Hints
mypy src/algs4 --show-error-codes
```

### Coverage zu niedrig

```bash
# Generiere Coverage-Report
python3 scripts/generate_coverage.py --html
open htmlcov/index.html
```

## Best Practices

### 1. Commits vor Push überprüfen

```bash
# Lokal testen
pytest tests/ -v
ruff check src/ tests/
mypy src/algs4
```

### 2. Aussagekräftige Commit-Messages

```
feat: Add new sorting algorithm
fix: Correct edge case in BST deletion
docs: Update API documentation
test: Add coverage for hashing module
```

### 3. Pull Requests

- Beschreibe die Änderungen
- Referenziere verwandte Issues
- Stelle sicher, dass alle Checks bestehen

### 4. Releases

- Aktualisiere CHANGELOG.md
- Aktualisiere Version in pyproject.toml und __init__.py
- Erstelle Git Tag
- Schreibe Release Notes

## Weitere Ressourcen

- [GitHub Actions Dokumentation](https://docs.github.com/en/actions)
- [Workflow Syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)
- [Codecov Integration](https://docs.github.com/en/actions/publishing-packages-with-github-actions)

