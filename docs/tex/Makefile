# Makefile für FFHS-DUA ConTeXt-Dokumentation
# ============================================
#
# Verwendung:
#   make          - Kompiliert das Dokument
#   make pdf      - Kompiliert das Dokument (alias)
#   make clean    - Entfernt temporäre Dateien
#   make distclean - Entfernt alle generierten Dateien
#   make view     - Öffnet das PDF
#   make watch    - Überwacht Änderungen und kompiliert automatisch

# Konfiguration
DOCUMENT = dua-dokumentation
CONTEXT = context

# Hauptquelldateien - rekursiv alle .tex-Dateien finden
SOURCES = $(DOCUMENT).tex \
          $(shell find content/chapters -name "*.tex" 2>/dev/null) \
          $(shell find templates/styles -name "*.tex" 2>/dev/null)

# Standard-Ziel
.PHONY: all
all: pdf

# PDF erstellen mit context (MkIV - empfohlen)
.PHONY: pdf
pdf: $(DOCUMENT).pdf

$(DOCUMENT).pdf: $(SOURCES)
	@echo "==> Kompiliere $(DOCUMENT).tex mit context (MkIV)..."
	$(CONTEXT) $(DOCUMENT).tex
	@echo "==> Fertig: $(DOCUMENT).pdf"

# Temporäre Dateien entfernen
.PHONY: clean
clean:
	@echo "==> Entferne temporäre Dateien..."
	rm -f $(DOCUMENT).log $(DOCUMENT).tuc $(DOCUMENT).tuo
	rm -f $(DOCUMENT).aux $(DOCUMENT).toc $(DOCUMENT).idx
	rm -f $(DOCUMENT).tmp $(DOCUMENT).top $(DOCUMENT).tui $(DOCUMENT)*.mp
	rm -f $(DOCUMENT).synctex.gz $(DOCUMENT).fls $(DOCUMENT).fdb_latexmk
	rm -f *.log *.tuc *.tuo *.aux
	rm -f $(DOCUMENT)-temp-*.vimout
	rm -rf texexec-*.tmp
	@echo "==> Aufgeräumt."

# Alle generierten Dateien entfernen
.PHONY: distclean
distclean: clean
	@echo "==> Entferne PDF..."
	rm -f $(DOCUMENT).pdf
	@echo "==> Vollständig aufgeräumt."

# PDF anzeigen (macOS)
.PHONY: view
view: pdf
	@echo "==> Öffne $(DOCUMENT).pdf..."
	open $(DOCUMENT).pdf

# Überwachungsmodus (benötigt fswatch)
.PHONY: watch
watch:
	@echo "==> Überwache Änderungen..."
	@echo "    (Drücke Ctrl+C zum Beenden)"
	fswatch -o $(SOURCES) | xargs -n1 -I{} make pdf

# Hilfe
.PHONY: help
help:
	@echo "FFHS-DUA ConTeXt Dokumentation - Makefile"
	@echo ""
	@echo "Verfügbare Ziele:"
	@echo "  make          - Kompiliert das Dokument mit context (MkIV)"
	@echo "  make pdf      - Kompiliert das Dokument (alias)"
	@echo "  make clean    - Entfernt temporäre Dateien"
	@echo "  make distclean- Entfernt alle generierten Dateien"
	@echo "  make view     - Öffnet das PDF"
	@echo "  make watch    - Überwacht Änderungen (benötigt fswatch)"
	@echo "  make help     - Zeigt diese Hilfe"
