#!/bin/bash

# Script zum Generieren von Coverage-Reports für ffhs-dua
# Verwendung: ./scripts/generate_coverage.sh [--html] [--xml] [--all]

set -e

# Farben für Output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Standard-Optionen
GENERATE_TERM=true
GENERATE_HTML=false
GENERATE_XML=false

# Parse Argumente
while [[ $# -gt 0 ]]; do
    case $1 in
        --html)
            GENERATE_HTML=true
            shift
            ;;
        --xml)
            GENERATE_XML=true
            shift
            ;;
        --all)
            GENERATE_HTML=true
            GENERATE_XML=true
            shift
            ;;
        *)
            echo "Unbekannte Option: $1"
            echo "Verwendung: $0 [--html] [--xml] [--all]"
            exit 1
            ;;
    esac
done

echo -e "${BLUE}============================================================${NC}"
echo -e "${BLUE}Coverage-Report Generator für ffhs-dua${NC}"
echo -e "${BLUE}============================================================${NC}"
echo ""

# Stelle sicher, dass wir im Projekt-Root sind
if [ ! -f "pyproject.toml" ]; then
    echo -e "${YELLOW}Fehler: pyproject.toml nicht gefunden!${NC}"
    echo "Bitte führe dieses Script aus dem Projekt-Root aus."
    exit 1
fi

# Installiere Dependencies falls nötig
echo -e "${BLUE}Überprüfe Dependencies...${NC}"
python3 -m pip install -q pytest pytest-cov coverage 2>/dev/null || true

# Generiere Coverage-Reports
echo -e "${BLUE}Generiere Coverage-Reports...${NC}"
echo ""

PYTEST_ARGS="tests/ --cov=src.algs4 --cov-report=term-missing"

if [ "$GENERATE_HTML" = true ]; then
    PYTEST_ARGS="$PYTEST_ARGS --cov-report=html"
fi

if [ "$GENERATE_XML" = true ]; then
    PYTEST_ARGS="$PYTEST_ARGS --cov-report=xml"
fi

python3 -m pytest $PYTEST_ARGS -q

echo ""
echo -e "${GREEN}✅ Coverage-Reports erfolgreich generiert!${NC}"
echo ""

# Zeige Pfade zu den generierten Reports
if [ "$GENERATE_HTML" = true ]; then
    echo -e "${BLUE}HTML-Report:${NC}"
    echo "  Pfad: htmlcov/index.html"
    echo "  Öffnen mit: open htmlcov/index.html"
    echo ""
fi

if [ "$GENERATE_XML" = true ]; then
    echo -e "${BLUE}XML-Report:${NC}"
    echo "  Pfad: coverage.xml"
    echo ""
fi

echo -e "${BLUE}Terminal-Report:${NC}"
echo "  Siehe oben für detaillierte Statistiken"
echo ""

# Zeige Coverage-Zusammenfassung
echo -e "${BLUE}============================================================${NC}"
echo -e "${BLUE}Coverage-Zusammenfassung${NC}"
echo -e "${BLUE}============================================================${NC}"
python3 -m coverage report --skip-covered 2>/dev/null || true

echo ""
echo -e "${GREEN}✅ Fertig!${NC}"
