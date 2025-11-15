# Pre-Commit Hooks Setup

Dieses Projekt verwendet Pre-Commit Hooks zur automatischen Code-Qualitätsprüfung vor jedem Commit.

## Installation

Die Pre-Commit Hooks sind bereits in der Entwicklungsumgebung konfiguriert. Nach dem Klonen des Repositories müssen Sie die Hooks installieren:

```bash
# Hooks installieren
pre-commit install

# Hooks deinstallieren (falls nötig)
pre-commit uninstall
```

## Verfügbare Hooks

### 1. **General File Checks** (pre-commit-hooks)
- `check-merge-conflict` - Identifiziert Merge-Konflikte
- `check-yaml` - Validiert YAML-Dateien
- `check-toml` - Validiert TOML-Dateien
- `check-json` - Validiert JSON-Dateien
- `check-ast` - Überprüft Python-Syntax
- `check-added-large-files` - Verhindert grosse Dateien (>1MB)
- `trailing-whitespace` - Entfernt Leerzeichen am Zeilenende
- `end-of-file-fixer` - Stellt sicher, dass Dateien mit Newline enden
- `debug-statements` - Findet Debugger-Imports und `breakpoint()`
- `check-byte-order-marker` - Findet UTF-8 Byte-Order Marker

### 2. **Ruff** (astral-sh/ruff-pre-commit)
- `ruff` - Linting und automatische Fixes
- `ruff-format` - Code-Formatierung

### 3. **Mypy** (pre-commit/mirrors-mypy)
- Type-Checking für Python-Code
- Ausgeschlossen: `tests/`

### 4. **Bandit** (PyCQA/bandit)
- Sicherheitsprüfungen für Python-Code
- Ausgeschlossen: `tests/`

## Verwendung

### Hooks automatisch vor jedem Commit ausführen
Die Hooks werden automatisch ausgeführt, wenn Sie `git commit` ausführen. Wenn ein Hook fehlschlägt, wird der Commit blockiert.

```bash
git commit -m "Your commit message"
```

### Hooks manuell ausführen

```bash
# Alle Hooks auf allen Dateien ausführen
pre-commit run --all-files

# Nur auf geänderten Dateien ausführen
pre-commit run

# Spezifische Hook ausführen
pre-commit run ruff --all-files
pre-commit run mypy --all-files
```

### Commit ohne Hooks durchführen (nicht empfohlen)

```bash
git commit --no-verify
```

## Konfiguration

Die Konfiguration befindet sich in `.pre-commit-config.yaml`:

- **Python-Version**: 3.13
- **Fail-Fast**: Deaktiviert (alle Hooks werden ausgeführt)
- **Ausgeschlossene Pfade**: `.venv/`, `.idea/`, `__pycache__/`, etc.

## Tipps

1. **Schnellere Hooks**: Führen Sie `pre-commit run` ohne `--all-files` aus, um nur geänderte Dateien zu prüfen
2. **Automatische Fixes**: Ruff und andere Tools beheben viele Probleme automatisch
3. **Regelmässige Updates**: Aktualisieren Sie die Hooks regelmässig mit `pre-commit autoupdate`

## Fehlerbehebung

### Hooks werden nicht ausgeführt
```bash
# Hooks neu installieren
pre-commit install
```

### Spezifischer Hook schlägt fehl
```bash
# Hook mit Debugging ausführen
pre-commit run <hook-id> --all-files --verbose
```

### Umgebung zurücksetzen
```bash
# Alle Pre-Commit Umgebungen löschen
pre-commit clean
```

## Weitere Informationen

- [Pre-Commit Dokumentation](https://pre-commit.com)
- [Verfügbare Hooks](https://pre-commit.com/hooks.html)
- [Ruff Dokumentation](https://docs.astral.sh/ruff/)
- [Mypy Dokumentation](https://mypy.readthedocs.io/)
