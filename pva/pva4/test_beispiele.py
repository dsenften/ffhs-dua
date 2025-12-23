#!/usr/bin/env python3
"""Tests fuer die Beispieldateien der PVA 4 Gruppenarbeit.

Diese Tests stellen sicher, dass alle Beispieldateien korrekt funktionieren
und die erwarteten Ausgaben produzieren.
"""

import subprocess
import sys


class TestBeispielGruppe1:
    """Tests fuer beispiele_gruppe_1_bfs_dfs.py"""

    def test_beispiele_gruppe_1_runs_without_error(self):
        """Test: Beispiel 1 laeuft ohne Fehler."""
        result = subprocess.run(
            [sys.executable, "pva/pva4/beispiele_gruppe_1_bfs_dfs.py"],
            capture_output=True,
            text=True,
            timeout=30,
        )
        assert result.returncode == 0, f"Fehler: {result.stderr}"
        assert "ALLE BEISPIELE ABGESCHLOSSEN" in result.stdout

    def test_beispiele_gruppe_1_contains_bfs_output(self):
        """Test: Beispiel 1 enthaelt BFS-Ausgabe."""
        result = subprocess.run(
            [sys.executable, "pva/pva4/beispiele_gruppe_1_bfs_dfs.py"],
            capture_output=True,
            text=True,
            timeout=30,
        )
        assert "BREITENSUCHE (BFS)" in result.stdout
        assert "Distanz=" in result.stdout

    def test_beispiele_gruppe_1_contains_dfs_output(self):
        """Test: Beispiel 1 enthaelt DFS-Ausgabe."""
        result = subprocess.run(
            [sys.executable, "pva/pva4/beispiele_gruppe_1_bfs_dfs.py"],
            capture_output=True,
            text=True,
            timeout=30,
        )
        assert "TIEFENSUCHE (DFS)" in result.stdout
        assert "erreichbar" in result.stdout


class TestBeispielGruppe2:
    """Tests fuer beispiele_gruppe_2_kuerzeste_wege.py"""

    def test_beispiele_gruppe_2_runs_without_error(self):
        """Test: Beispiel 2 laeuft ohne Fehler."""
        result = subprocess.run(
            [sys.executable, "pva/pva4/beispiele_gruppe_2_kuerzeste_wege.py"],
            capture_output=True,
            text=True,
            timeout=30,
        )
        assert result.returncode == 0, f"Fehler: {result.stderr}"
        assert "ALLE BEISPIELE ABGESCHLOSSEN" in result.stdout

    def test_beispiele_gruppe_2_contains_dijkstra_output(self):
        """Test: Beispiel 2 enthaelt Dijkstra-Ausgabe."""
        result = subprocess.run(
            [sys.executable, "pva/pva4/beispiele_gruppe_2_kuerzeste_wege.py"],
            capture_output=True,
            text=True,
            timeout=30,
        )
        assert "DIJKSTRA" in result.stdout
        assert "Distanz=" in result.stdout


class TestBeispielGruppe3:
    """Tests fuer beispiele_gruppe_3_spannbaeume.py"""

    def test_beispiele_gruppe_3_runs_without_error(self):
        """Test: Beispiel 3 laeuft ohne Fehler."""
        result = subprocess.run(
            [sys.executable, "pva/pva4/beispiele_gruppe_3_spannbaeume.py"],
            capture_output=True,
            text=True,
            timeout=30,
        )
        assert result.returncode == 0, f"Fehler: {result.stderr}"
        assert "ALLE BEISPIELE ABGESCHLOSSEN" in result.stdout

    def test_beispiele_gruppe_3_contains_kruskal_output(self):
        """Test: Beispiel 3 enthaelt Kruskal-Ausgabe."""
        result = subprocess.run(
            [sys.executable, "pva/pva4/beispiele_gruppe_3_spannbaeume.py"],
            capture_output=True,
            text=True,
            timeout=30,
        )
        assert "KRUSKAL" in result.stdout
        assert "MST-Gewicht:" in result.stdout

    def test_beispiele_gruppe_3_contains_prim_output(self):
        """Test: Beispiel 3 enthaelt Prim-Ausgabe."""
        result = subprocess.run(
            [sys.executable, "pva/pva4/beispiele_gruppe_3_spannbaeume.py"],
            capture_output=True,
            text=True,
            timeout=30,
        )
        assert "PRIM" in result.stdout


class TestBeispielGruppe4:
    """Tests fuer beispiele_gruppe_4_union_find.py"""

    def test_beispiele_gruppe_4_runs_without_error(self):
        """Test: Beispiel 4 laeuft ohne Fehler."""
        result = subprocess.run(
            [sys.executable, "pva/pva4/beispiele_gruppe_4_union_find.py"],
            capture_output=True,
            text=True,
            timeout=30,
        )
        assert result.returncode == 0, f"Fehler: {result.stderr}"
        assert "ALLE BEISPIELE ABGESCHLOSSEN" in result.stdout

    def test_beispiele_gruppe_4_contains_union_find_output(self):
        """Test: Beispiel 4 enthaelt Union-Find-Ausgabe."""
        result = subprocess.run(
            [sys.executable, "pva/pva4/beispiele_gruppe_4_union_find.py"],
            capture_output=True,
            text=True,
            timeout=30,
        )
        assert "UNION-FIND" in result.stdout
        assert "Komponenten:" in result.stdout


if __name__ == "__main__":
    import pytest

    pytest.main([__file__, "-v"])
