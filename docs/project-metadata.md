# Projekt-Metadaten für ffhs-dua

Dieses Dokument beschreibt die Projekt-Metadaten und deren Konfiguration in `pyproject.toml`.

## Überblick

Die `pyproject.toml` Datei enthält alle wichtigen Metadaten des Projekts:
- Projekt-Name und Version
- Beschreibung und Dokumentation
- Autor und Maintainer
- Abhängigkeiten und optionale Dependencies
- Build-System-Konfiguration
- Tool-Konfigurationen (pytest, coverage, ruff, mypy, etc.)

## Projekt-Informationen

### Basis-Metadaten

```toml
[project]
name = "ffhs-dua"
version = "1.0.0"
description = "Umfassende Python-Implementierung grundlegender Algorithmen und Datenstrukturen für den akademischen Gebrauch an der Fernfachhochschule Schweiz (FFHS)"
readme = "README.md"
requires-python = ">=3.13.1"
license = {text = "MIT"}
```

**Erklärung:**
- **name**: Eindeutiger Paket-Name (wird auf PyPI verwendet)
- **version**: Semantische Versionierung (MAJOR.MINOR.PATCH)
- **description**: Kurze Beschreibung des Projekts
- **readme**: Pfad zur README-Datei
- **requires-python**: Minimale Python-Version
- **license**: Lizenz des Projekts

### Autor und Maintainer

```toml
authors = [
    {name = "Daniel Senften", email = "daniel.senften@ffhs.ch"}
]
maintainers = [
    {name = "Daniel Senften", email = "daniel.senften@ffhs.ch"}
]
```

### Keywords

```toml
keywords = [
    "algorithms",
    "data-structures",
    "education",
    "ffhs",
    "sorting",
    "searching",
    "union-find",
    "binary-search-tree",
    "avl-tree",
    "red-black-tree"
]
```

Diese Keywords helfen bei der Auffindbarkeit auf PyPI.

### Klassifizierer

```toml
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Education",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: German",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.13",
    "Topic :: Education",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Scientific/Engineering"
]
```

**Klassifizierer-Kategorien:**
- **Development Status**: Reife des Projekts (Alpha, Beta, Production/Stable)
- **Intended Audience**: Zielgruppe
- **License**: Lizenz-Typ
- **Natural Language**: Sprache der Dokumentation
- **Operating System**: Unterstützte Betriebssysteme
- **Programming Language**: Programmiersprache und Version
- **Topic**: Thematische Kategorien

### Projekt-URLs

```toml
[project.urls]
Homepage = "https://gitlab.com/talent-factory/ffhs/dua"
Documentation = "https://gitlab.com/talent-factory/ffhs/dua/-/blob/develop/docs/index.adoc"
Repository = "https://gitlab.com/talent-factory/ffhs/dua.git"
Issues = "https://gitlab.com/talent-factory/ffhs/dua/-/issues"
Changelog = "https://gitlab.com/talent-factory/ffhs/dua/-/blob/develop/CHANGELOG.md"
```

Diese URLs werden auf PyPI angezeigt und helfen Benutzern, das Projekt zu finden.

## Abhängigkeiten

### Haupt-Abhängigkeiten

```toml
dependencies = [
    "matplotlib>=3.10.5",
]
```

Nur matplotlib ist erforderlich für die Visualisierungen.

### Entwicklungs-Abhängigkeiten

```toml
[project.optional-dependencies]
dev = [
    "pytest>=8.4.1",
    "pytest-cov>=4.0",
    "pytest-benchmark>=4.0",
    "ruff>=0.12.10",
    "mypy>=1.0",
    "pre-commit>=3.0",
    "jupyter>=1.1.1",
]
```

Installation:
```bash
pip install ffhs-dua[dev]
```

### Dokumentations-Abhängigkeiten

```toml
docs = [
    "sphinx>=7.0",
    "sphinx-rtd-theme>=1.3",
]
```

Installation:
```bash
pip install ffhs-dua[docs]
```

## Version-Management

### Versionierung

Das Projekt folgt der **Semantischen Versionierung** (SemVer):

- **MAJOR** (1.0.0): Inkompatible API-Änderungen
- **MINOR** (1.1.0): Neue Features, abwärtskompatibel
- **PATCH** (1.0.1): Bug-Fixes, abwärtskompatibel

### Version aktualisieren

Die Version muss an zwei Stellen aktualisiert werden:

1. **pyproject.toml**:
```toml
[project]
version = "1.0.0"
```

2. **src/algs4/__init__.py**:
```python
__version__ = "1.0.0"
```

## Build-System

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src"]
```

Das Projekt verwendet **hatchling** als Build-Backend.

### Paket bauen

```bash
# Wheel bauen
python3 -m build

# Oder mit hatchling direkt
python3 -m hatchling build
```

## Konsistenz überprüfen

### pyproject.toml validieren

```bash
# Mit pip
pip install build
python3 -m build --sdist

# Oder mit hatchling
python3 -m hatchling build
```

### Metadaten überprüfen

```bash
# Mit twine
pip install twine
twine check dist/*
```

## Best Practices

### 1. Version konsistent halten

Stelle sicher, dass die Version in `pyproject.toml` und `src/algs4/__init__.py` identisch ist.

### 2. Aussagekräftige Beschreibung

Die Beschreibung sollte:
- Kurz und prägnant sein
- Das Hauptziel des Projekts erklären
- Zielgruppe identifizieren

### 3. Korrekte Klassifizierer

Verwende nur offizielle Klassifizierer von PyPI:
- [PyPI Classifiers](https://pypi.org/pypi?%3Aaction=list_classifiers)

### 4. Abhängigkeiten minimal halten

- Nur notwendige Abhängigkeiten in `dependencies`
- Entwicklungs-Tools in `dev` optional-dependencies
- Dokumentations-Tools in `docs` optional-dependencies

### 5. URLs aktuell halten

Stelle sicher, dass alle URLs in `[project.urls]` gültig sind.

## Weitere Ressourcen

- [PEP 621 - Project metadata](https://peps.python.org/pep-0621/)
- [PyPI Classifiers](https://pypi.org/pypi?%3Aaction=list_classifiers)
- [Semantic Versioning](https://semver.org/)
- [Hatchling Documentation](https://hatch.pypa.io/)

