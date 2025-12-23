Erstelle eine umfassende Zusammenfassung zum Thema "{{arg1}}".

## Anweisungen

1. **Thema-Validierung:**
   - Falls kein Thema angegeben wurde ({{arg1}} ist leer), frage den Benutzer mit dem AskUserQuestion Tool nach dem gewünschten Thema
   - Das Thema sollte spezifisch und klar definiert sein

2. **Quellen-Recherche:**
   - Durchsuche AUSSCHLIESSLICH das Verzeichnis 'docs/refs/' nach relevanten Unterlagen
   - Verwende Glob und Grep Tools, um passende Dateien zum Thema zu finden
   - Lese alle relevanten Dateien vollständig mit dem Read Tool

3. **Zusammenfassungs-Erstellung:**
   - Erstelle eine strukturierte Markdown-Zusammenfassung basierend NUR auf den gefundenen Materialien
   - Die Zusammenfassung sollte enthalten:
     - Überschrift mit dem Thema
     - Einleitung
     - Hauptinhalt in logisch strukturierten Abschnitten
     - Wichtige Konzepte, Definitionen und Beispiele
     - Fazit oder Schlussfolgerung
   - Verwende deutsche Sprache
   - Nutze Markdown-Formatierung: Überschriften, Listen, Code-Blöcke, Hervorhebungen
   - Zitiere oder referenziere die Quelldateien, wo relevant

4. **Datei-Speicherung:**
   - Speichere die Zusammenfassung in 'docs/summaries/' als Markdown-Datei
   - Dateiname: `{thema-in-kebab-case}.md` (z.B. "dijkstra-algorithmus.md")
   - Verwende das Write Tool zum Erstellen der Datei

5. **Formatierung:**
   - NACH der Erstellung der Markdown-Datei MUSS der Task Tool mit subagent_type='markdown-syntax-formatter' aufgerufen werden
   - Übergib den Pfad zur erstellten Datei an den Formatter
   - Der Formatter korrigiert Markdown-Syntax-Probleme und stellt konsistente Formatierung sicher

## Fehlerbehandlung

- Falls keine relevanten Unterlagen in 'docs/refs/' gefunden werden, informiere den Benutzer
- Falls das Thema zu allgemein ist, bitte um Präzisierung
- Überprüfe, dass die Zusammenfassung tatsächlich nur auf vorhandenen Materialien basiert

## Beispiel-Aufruf

```bash
/create-summary Dijkstra Algorithmus
```

Dies erstellt eine Zusammenfassung zum Dijkstra-Algorithmus basierend auf Materialien in 'docs/refs/' und speichert sie in 'data/summaries/dijkstra-algorithmus.md'.
