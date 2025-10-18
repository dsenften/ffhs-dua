# CI/CD mit GitHub Actions

Dieses Dokument beschreibt die Continuous Integration und Continuous Deployment (CI/CD) Infrastruktur für ffhs-dua.

## Überblick

Das Projekt verwendet GitHub Actions für automatisierte Tests, Code-Qualitätsprüfungen und Releases.

**Workflows:**
1. **Tests** - Automatisierte Tests auf mehreren Plattformen
2. **Code Quality** - Linting, Type-Checking, Sicherheitsprüfungen
3. **Documentation** - Dokumentations-Validierung
4. **Release** - Automatisierte Release-Erstellung

## Workflow: Tests

### Trigger

- Push auf `develop` oder `main`
- Pull Requests zu `develop` oder `main`

### Schritte

1. **Checkout** - Repository klonen
2. **Python Setup** - Python 3.13 installieren
3. **Dependencies** - Abhängigkeiten installieren
4. **Ruff Linting** - Code-Formatierung überprüfen
5. **Mypy Type-Check** - Type-Hints überprüfen
6. **Pytest** - Unit-Tests ausführen
7. **Coverage** - Code-Coverage messen
8. **Codecov Upload** - Coverage-Reports hochladen

### Plattformen

- Ubuntu (Linux)
- macOS
- Windows

### Beispiel-Output

```
✓ Ruff check passed
✓ Ruff format check passed
✓ Mypy type check passed
✓ 362 tests passed
✓ Coverage: 93.08%
✓ Coverage uploaded to Codecov
```

## Workflow: Code Quality

### Trigger

- Push auf `develop` oder `main`
- Pull Requests zu `develop` oder `main`

### Schritte

1. **Ruff Check** - Linting und Formatierung
2. **Mypy** - Type-Checking
3. **Bandit** - Sicherheitsprüfungen
4. **Common Issues** - Print-Statements, TODO/FIXME

### Beispiel-Output

```
=== Ruff Check ===
✓ All checks passed

=== Ruff Format Check ===
✓ All files properly formatted

=== Mypy Type Check ===
✓ No type errors

=== Bandit Security Check ===
✓ No security issues found

=== Checking for print statements ===
✓ No print statements found

=== Checking for TODO comments ===
No TODO/FIXME found
```

## Workflow: Documentation

### Trigger

- Push auf `develop` oder `main` (nur wenn Docs geändert)
- Pull Requests zu `develop` oder `main` (nur wenn Docs geändert)

### Schritte

1. **Checkout** - Repository klonen
2. **Python Setup** - Python 3.13 installieren
3. **Dependencies** - Sphinx installieren
4. **File Check** - Dokumentations-Dateien überprüfen
5. **Markdown Validation** - Markdown validieren
6. **Link Check** - Broken Links überprüfen

## Workflow: Release

### Trigger

- Git Tag mit Format `v*` (z.B. `v1.0.0`)

### Schritte

1. **Checkout** - Repository klonen
2. **Python Setup** - Python 3.13 installieren
3. **Build Dependencies** - Build-Tools installieren
4. **Version Extraction** - Version aus Tag extrahieren
5. **Version Verification** - Version-Konsistenz überprüfen
6. **Tests** - Unit-Tests ausführen
7. **Build** - Distribution bauen
8. **Check** - Distribution validieren
9. **Release** - GitHub Release erstellen
10. **Upload** - Artefakte hochladen

### Release erstellen

```bash
# 1. Version aktualisieren
# pyproject.toml: version = "1.0.0"
# src/algs4/__init__.py: __version__ = "1.0.0"

# 2. Commit und Push
git add pyproject.toml src/algs4/__init__.py
git commit -m "chore: bump version to 1.0.0"
git push origin develop

# 3. Tag erstellen
git tag v1.0.0
git push origin v1.0.0

# 4. GitHub Actions wird automatisch:
# - Tests ausführen
# - Distribution bauen
# - Release erstellen
# - Artefakte hochladen
```

## Status Badges

Füge diese Badges zur README hinzu:

```markdown
![Tests](https://github.com/talent-factory/ffhs-dua/workflows/Tests/badge.svg)
![Code Quality](https://github.com/talent-factory/ffhs-dua/workflows/Code%20Quality/badge.svg)
![Documentation](https://github.com/talent-factory/ffhs-dua/workflows/Documentation/badge.svg)
```

## Branch Protection Rules

Empfohlene Konfiguration für `main` Branch:

1. **Require status checks to pass before merging**
   - Tests
   - Code Quality
   - Documentation

2. **Require code reviews before merging**
   - Mindestens 1 Review

3. **Require branches to be up to date before merging**
   - Aktiviert

4. **Require conversation resolution before merging**
   - Aktiviert

## Secrets und Umgebungsvariablen

### Automatisch verfügbar

- `GITHUB_TOKEN` - GitHub API Token (automatisch)

### Optional konfigurierbar

- `CODECOV_TOKEN` - Codecov Token (für private Repos)

### Konfiguration

1. Gehe zu Repository Settings
2. Wähle "Secrets and variables" → "Actions"
3. Klicke "New repository secret"
4. Gib Name und Wert ein

## Troubleshooting

### Workflow schlägt fehl

1. Überprüfe Workflow-Logs in GitHub Actions
2. Führe Tests lokal aus
3. Überprüfe Python-Version
4. Überprüfe Dependencies

### Tests schlagen fehl

```bash
# Lokal reproduzieren
python3 -m pytest tests/ -v

# Mit Coverage
python3 -m pytest tests/ --cov=src.algs4 --cov-report=html
```

### Linting-Fehler

```bash
# Automatisch beheben
ruff check --fix src/ tests/
ruff format src/ tests/
```

### Release schlägt fehl

1. Überprüfe Version-Konsistenz
2. Überprüfe, dass alle Tests bestehen
3. Überprüfe Tag-Format (v1.0.0)
4. Überprüfe CHANGELOG.md

## Best Practices

### 1. Commits vor Push überprüfen

```bash
pytest tests/ -v
ruff check src/ tests/
mypy src/algs4
```

### 2. Aussagekräftige Commit-Messages

```
feat: Add new feature
fix: Fix bug
docs: Update documentation
test: Add tests
chore: Update dependencies
```

### 3. Pull Requests

- Beschreibe Änderungen
- Referenziere Issues
- Stelle sicher, dass Checks bestehen

### 4. Releases

- Aktualisiere CHANGELOG.md
- Aktualisiere Version
- Erstelle Git Tag
- Schreibe Release Notes

## Weitere Ressourcen

- [GitHub Actions Dokumentation](https://docs.github.com/en/actions)
- [Workflow Syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)
- [Codecov Integration](https://docs.github.com/en/actions/publishing-packages-with-github-actions)
- [.github/workflows/README.md](.github/workflows/README.md) - Detaillierte Workflow-Dokumentation

