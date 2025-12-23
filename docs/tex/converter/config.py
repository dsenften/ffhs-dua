"""
Konfigurationsmanagement für ConTeXt-Dokumentationssystem
=========================================================

Dieses Modul verwaltet alle Konfigurationseinstellungen
für das Dokumentationssystem.
"""

import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


@dataclass
class BuildConfig:
    """
    Konfiguration für den Dokumentations-Build-Prozess.
    """

    # Verzeichnisse
    project_root: Path = Path.cwd()
    template_dir: Path = Path("docs/tex/templates")
    output_dir: Path = Path("docs/tex/output")
    assets_dir: Path = Path("docs/tex/assets")

    # Markdown-Verarbeitung
    markdown_dirs: list[Path] = field(
        default_factory=lambda: [
            Path("README.md"),
            Path("docs"),
            Path("pva"),
            Path("src"),
        ]
    )
    markdown_extensions: list[str] = field(default_factory=lambda: [".md", ".markdown"])
    exclude_patterns: list[str] = field(
        default_factory=lambda: [
            "node_modules",
            ".git",
            "__pycache__",
            "*.pyc",
            ".pytest_cache",
        ]
    )

    # ConTeXt-Einstellungen
    context_command: str = "context"
    context_args: list[str] = field(
        default_factory=lambda: ["--batchmode", "--nonstopmode"]
    )

    # PDF-Einstellungen
    pdf_output_name: str = "ffhs-dua-documentation.pdf"
    pdf_quality: str = "high"  # low, medium, high

    # Dokumentstruktur
    document_title: str = "FFHS-DUA: Datenstrukturen und Algorithmen"
    document_subtitle: str = "Praktische Vertiefungsaufgaben und Implementierungen"
    document_author: str = "Daniel Senften"
    document_institution: str = "Fernfachhochschule Schweiz (FFHS)"
    document_course: str = "Datenstrukturen und Algorithmen"
    document_version: str = "1.0"

    # Kapitel-Konfiguration
    chapters: dict[str, dict[str, Any]] = field(
        default_factory=lambda: {
            "introduction": {"title": "Einführung", "files": ["README.md"], "order": 1},
            "pva1": {
                "title": "PVA 1: Fundamentals",
                "files": ["pva/pva1/**/*.md"],
                "order": 2,
            },
            "pva2": {
                "title": "PVA 2: Sorting",
                "files": ["pva/pva2/**/*.md"],
                "order": 3,
            },
            "pva3": {
                "title": "PVA 3: Searching",
                "files": ["pva/pva3/**/*.md"],
                "order": 4,
            },
            "pva4": {
                "title": "PVA 4: Graphs",
                "files": ["pva/pva4/**/*.md"],
                "order": 5,
            },
            "pva5": {
                "title": "PVA 5: Strings",
                "files": ["pva/pva5/**/*.md"],
                "order": 6,
            },
        }
    )

    # Style-Einstellungen
    style_config: dict[str, Any] = field(
        default_factory=lambda: {
            "font_size": "11pt",
            "line_spacing": "1.2em",
            "page_margins": {
                "top": "2.5cm",
                "bottom": "2.5cm",
                "left": "2.5cm",
                "right": "2.5cm",
            },
            "colors": {
                "primary": "ffhsblue",
                "secondary": "ffhsgray",
                "accent": "ffhsred",
            },
        }
    )

    # Index-Einstellungen
    generate_index: bool = True
    index_terms: list[str] = field(
        default_factory=lambda: [
            "Algorithmus",
            "Datenstruktur",
            "Komplexität",
            "Stack",
            "Queue",
            "Tree",
            "Graph",
            "Hash",
            "Sorting",
            "Searching",
            "Python",
            "Java",
        ]
    )

    # Logging
    log_level: str = "INFO"
    log_file: Path | None = None

    def __post_init__(self):
        """Nachbearbeitung nach Initialisierung."""
        # Pfade zu absoluten Pfaden konvertieren
        self.project_root = Path(self.project_root).resolve()
        self.template_dir = self.project_root / self.template_dir
        self.output_dir = self.project_root / self.output_dir
        self.assets_dir = self.project_root / self.assets_dir

        # Markdown-Verzeichnisse zu absoluten Pfaden
        self.markdown_dirs = [self.project_root / path for path in self.markdown_dirs]


def load_config(config_path: Path | None = None) -> BuildConfig:
    """
    Lädt die Konfiguration aus einer YAML-Datei.

    Args:
        config_path: Pfad zur Konfigurationsdatei

    Returns:
        BuildConfig-Instanz
    """
    logger = logging.getLogger(__name__)

    # Standard-Konfiguration
    config = BuildConfig()

    # Konfigurationsdatei suchen
    if config_path is None:
        # Standard-Pfade durchsuchen
        possible_paths = [
            Path("docs/tex/config/build.yaml"),
            Path("docs/tex/build.yaml"),
            Path("build.yaml"),
        ]

        for path in possible_paths:
            if path.exists():
                config_path = path
                break

    # Konfigurationsdatei laden
    if config_path and config_path.exists():
        try:
            logger.info(f"Lade Konfiguration: {config_path}")

            with open(config_path, encoding="utf-8") as f:
                yaml_config = yaml.safe_load(f)

            # Konfiguration überschreiben
            _update_config_from_dict(config, yaml_config)

        except Exception as e:
            logger.warning(f"Fehler beim Laden der Konfiguration: {e}")
            logger.info("Verwende Standard-Konfiguration")
    else:
        logger.info(
            "Keine Konfigurationsdatei gefunden, verwende Standard-Konfiguration"
        )

    return config


def _update_config_from_dict(config: BuildConfig, data: dict[str, Any]):
    """
    Aktualisiert die Konfiguration mit Werten aus einem Dictionary.

    Args:
        config: BuildConfig-Instanz
        data: Dictionary mit Konfigurationswerten
    """
    for key, value in data.items():
        if hasattr(config, key):
            current_value = getattr(config, key)

            # Pfade konvertieren
            if isinstance(current_value, Path):
                setattr(config, key, Path(value))
            # Listen von Pfaden
            elif (
                isinstance(current_value, list)
                and current_value
                and isinstance(current_value[0], Path)
            ):
                setattr(config, key, [Path(p) for p in value])
            # Dictionaries mergen
            elif isinstance(current_value, dict) and isinstance(value, dict):
                current_value.update(value)
            # Direkt setzen
            else:
                setattr(config, key, value)


def save_config(config: BuildConfig, config_path: Path):
    """
    Speichert die Konfiguration in eine YAML-Datei.

    Args:
        config: BuildConfig-Instanz
        config_path: Pfad zur Ausgabedatei
    """
    logger = logging.getLogger(__name__)

    try:
        # Konfiguration zu Dictionary konvertieren
        config_dict = {}
        for field_name in config.__dataclass_fields__:
            value = getattr(config, field_name)

            # Pfade zu Strings konvertieren
            if isinstance(value, Path):
                config_dict[field_name] = str(value)
            elif isinstance(value, list) and value and isinstance(value[0], Path):
                config_dict[field_name] = [str(p) for p in value]
            else:
                config_dict[field_name] = value

        # YAML schreiben
        config_path.parent.mkdir(parents=True, exist_ok=True)
        with open(config_path, "w", encoding="utf-8") as f:
            yaml.dump(config_dict, f, default_flow_style=False, allow_unicode=True)

        logger.info(f"Konfiguration gespeichert: {config_path}")

    except Exception as e:
        logger.error(f"Fehler beim Speichern der Konfiguration: {e}")
        raise
