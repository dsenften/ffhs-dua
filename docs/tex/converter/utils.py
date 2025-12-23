"""
Hilfsfunktionen für ConTeXt-Dokumentationssystem
================================================

Dieses Modul enthält verschiedene Hilfsfunktionen für
die Dokumentationserstellung.
"""

import logging
import subprocess
import sys
from pathlib import Path


def setup_logging(level: int = logging.INFO, log_file: Path | None = None):
    """
    Configure the root logger with a console handler and an optional file handler.
    
    Parameters:
        level (int): Logging level applied to the root logger and created handlers.
        log_file (Path | None): Optional path to a log file; if provided, the file's parent directory will be created and a file handler will be attached.
    """
    # Formatter definieren
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Console Handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)

    # Root Logger konfigurieren
    root_logger = logging.getLogger()
    root_logger.setLevel(level)
    root_logger.addHandler(console_handler)

    # File Handler (optional)
    if log_file:
        log_file.parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        root_logger.addHandler(file_handler)


def validate_environment() -> bool:
    """
    Validate that the runtime environment meets requirements for documentation generation.
    
    Performs checks for a working ConTeXt installation and the presence of required Python modules.
    
    Returns:
        True if all validations pass, False otherwise.
    """
    logger = logging.getLogger(__name__)

    # Python-Version prüfen (3.13+ für dieses Projekt)
    logger.info(f"Python-Version: {sys.version_info.major}.{sys.version_info.minor}")

    # ConTeXt prüfen
    if not check_context_installation():
        logger.error("ConTeXt nicht gefunden oder nicht funktionsfähig")
        return False

    # Weitere Abhängigkeiten prüfen
    required_modules = ["yaml", "pathlib"]
    for module in required_modules:
        try:
            __import__(module)
        except ImportError:
            logger.error(f"Erforderliches Modul nicht gefunden: {module}")
            return False

    logger.info("Umgebungsvalidierung erfolgreich")
    return True


def check_context_installation() -> bool:
    """
    Check whether the ConTeXt `context` command is installed and executable.
    
    Attempts to run `context --version` (10-second timeout) to verify availability.
    
    Returns:
        `True` if the `context` command runs and exits with status code 0, `False` otherwise (including when the command is not found or times out).
    """
    try:
        result = subprocess.run(
            ["context", "--version"], capture_output=True, text=True, timeout=10
        )
        return result.returncode == 0
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False


def run_context(tex_file: Path, output_dir: Path | None = None) -> tuple[bool, str]:
    """
    Run ConTeXt on a given .tex file and return success status and process output.
    
    Parameters:
        tex_file (Path): Path to the .tex file to be processed.
        output_dir (Path | None): Optional directory to place ConTeXt results; if provided, passed to ConTeXt as the result directory.
    
    Returns:
        tuple[bool, str]: `True` and the process stdout if ConTeXt exits with code 0; `False` and stderr or an error message otherwise.
    """
    logger = logging.getLogger(__name__)

    try:
        # Kommando zusammenstellen
        cmd = ["context"]

        if output_dir:
            cmd.extend(["--result", str(output_dir)])

        cmd.extend(["--batchmode", "--nonstopmode", str(tex_file)])

        logger.info(f"Führe ConTeXt aus: {' '.join(cmd)}")

        # ConTeXt ausführen
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=tex_file.parent,
            timeout=300,  # 5 Minuten Timeout
        )

        if result.returncode == 0:
            logger.info("ConTeXt erfolgreich ausgeführt")
            return True, result.stdout
        else:
            logger.error(f"ConTeXt-Fehler (Code {result.returncode})")
            return False, result.stderr

    except subprocess.TimeoutExpired:
        logger.error("ConTeXt-Timeout")
        return False, "Timeout bei ConTeXt-Ausführung"
    except Exception as e:
        logger.error(f"Fehler bei ConTeXt-Ausführung: {e}")
        return False, str(e)


def find_markdown_files(
    directories: list[Path], extensions: list[str] = None
) -> list[Path]:
    """
    Locate Markdown files within the provided file system paths.
    
    Parameters:
        directories (list[Path]): Paths to files or directories to search; files are checked directly, directories are searched recursively.
        extensions (list[str], optional): File suffixes to include (example: [".md", ".markdown"]). Defaults to [".md", ".markdown"].
    
    Returns:
        list[Path]: Sorted list of unique Markdown file paths that match the given extensions.
    """
    if extensions is None:
        extensions = [".md", ".markdown"]

    markdown_files = []

    for directory in directories:
        if directory.is_file():
            # Einzelne Datei
            if directory.suffix.lower() in extensions:
                markdown_files.append(directory)
        elif directory.is_dir():
            # Verzeichnis rekursiv durchsuchen
            for ext in extensions:
                pattern = f"**/*{ext}"
                markdown_files.extend(directory.glob(pattern))

    # Duplikate entfernen und sortieren
    unique_files = list(set(markdown_files))
    unique_files.sort()

    return unique_files


def clean_output_directory(output_dir: Path, keep_patterns: list[str] = None):
    """
    Clean the contents of an output directory while preserving specified patterns.
    
    Deletes common temporary and auxiliary files (e.g., logs, aux, toc, tmp, fls, fdb_latexmk) from output_dir, leaving files that match any pattern in keep_patterns. If keep_patterns is not provided, files matching "*.pdf" are preserved.
    
    Parameters:
        output_dir (Path): Directory whose contents will be cleaned. If the directory does not exist, the function returns without action.
        keep_patterns (list[str] | None): Glob-style filename patterns to preserve (e.g., ["*.pdf", "important_*"]). Defaults to ["*.pdf"] when None.
    """
    logger = logging.getLogger(__name__)

    if not output_dir.exists():
        return

    if keep_patterns is None:
        keep_patterns = ["*.pdf"]  # PDFs standardmäßig behalten

    logger.info(f"Bereinige Ausgabeverzeichnis: {output_dir}")

    # Temporäre Dateien löschen
    temp_patterns = [
        "*.log",
        "*.aux",
        "*.toc",
        "*.tui",
        "*.tuo",
        "*.tmp",
        "*.fls",
        "*.fdb_latexmk",
    ]

    for pattern in temp_patterns:
        for file in output_dir.glob(pattern):
            try:
                file.unlink()
                logger.debug(f"Gelöscht: {file}")
            except Exception as e:
                logger.warning(f"Konnte nicht löschen {file}: {e}")


def copy_assets(source_dir: Path, target_dir: Path):
    """
    Copy common asset files (images, fonts, PDFs, etc.) from a source directory into a target directory while preserving the source's subdirectory structure.
    
    If the source directory does not exist, the function logs a warning and returns without raising. The function creates any necessary target subdirectories and copies matching asset file types (e.g., PNG, JPG, SVG, PDF, EPS, TTF, WOFF) using metadata-preserving copy operations.
    
    Parameters:
        source_dir (Path): Directory to search recursively for asset files.
        target_dir (Path): Destination directory where assets will be copied, preserving relative paths.
    """
    import shutil

    logger = logging.getLogger(__name__)

    if not source_dir.exists():
        logger.warning(f"Asset-Verzeichnis nicht gefunden: {source_dir}")
        return

    logger.info(f"Kopiere Assets: {source_dir} -> {target_dir}")

    # Asset-Dateitypen
    asset_patterns = [
        "*.png",
        "*.jpg",
        "*.jpeg",
        "*.gif",
        "*.svg",
        "*.pdf",
        "*.eps",
        "*.ps",
        "*.ttf",
        "*.otf",
        "*.woff",
        "*.woff2",
    ]

    target_dir.mkdir(parents=True, exist_ok=True)

    for pattern in asset_patterns:
        for asset_file in source_dir.rglob(pattern):
            # Relativer Pfad beibehalten
            rel_path = asset_file.relative_to(source_dir)
            target_file = target_dir / rel_path

            # Zielverzeichnis erstellen
            target_file.parent.mkdir(parents=True, exist_ok=True)

            # Datei kopieren
            try:
                shutil.copy2(asset_file, target_file)
                logger.debug(f"Kopiert: {asset_file} -> {target_file}")
            except Exception as e:
                logger.warning(f"Konnte nicht kopieren {asset_file}: {e}")


def generate_file_hash(file_path: Path) -> str:
    """
    Compute the SHA-256 hash of a file's contents.
    
    Parameters:
        file_path (Path): Path to the file to hash.
    
    Returns:
        str: SHA-256 hex digest of the file contents.
    """
    import hashlib

    hash_sha256 = hashlib.sha256()

    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)

    return hash_sha256.hexdigest()


def format_file_size(size_bytes: int) -> str:
    """
    Convert a size in bytes into a human-readable string using 1024-based units.
    
    Parameters:
        size_bytes (int): Size in bytes.
    
    Returns:
        str: Formatted size string using units B, KB, MB, GB, or TB (e.g., "1.5 MB").
    """
    if size_bytes == 0:
        return "0 B"

    size_names = ["B", "KB", "MB", "GB", "TB"]
    i = 0
    size = float(size_bytes)

    while size >= 1024.0 and i < len(size_names) - 1:
        size /= 1024.0
        i += 1

    return f"{size:.1f} {size_names[i]}"