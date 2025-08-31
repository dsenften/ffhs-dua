#!/usr/bin/env python3
"""
Validierung der Testdaten-Migration
"""

import os
from pathlib import Path

def validate_migration():
    """Validiert die Migration der Testdaten."""
    
    # Teste Zugriff auf verschiedene Testdaten-Kategorien
    test_files = [
        'data/sorting/1Kints.txt',
        'data/graphs/tinyG.txt', 
        'data/strings/mobydick.txt',
        'data/fundamentals/tinyUF.txt',
        'data/compression/4runs.bin'
    ]

    print('Validierung der migrierten Testdaten:')
    print('=' * 40)

    success_count = 0
    for file_path in test_files:
        path = Path(file_path)
        if path.exists():
            size = path.stat().st_size
            print(f'✅ {file_path} ({size:,} bytes)')
            success_count += 1
        else:
            print(f'❌ {file_path} - NICHT GEFUNDEN')

    # Gesamtstatistik
    txt_files = len(list(Path("data").rglob("*.txt")))
    csv_files = len(list(Path("data").rglob("*.csv")))
    bin_files = len(list(Path("data").rglob("*.bin")))
    total_files = txt_files + csv_files + bin_files
    
    print(f'\nGesamtstatistik:')
    print(f'  TXT-Dateien: {txt_files}')
    print(f'  CSV-Dateien: {csv_files}')
    print(f'  BIN-Dateien: {bin_files}')
    print(f'  Gesamt: {total_files}')
    
    print(f'\nValidierung: {success_count}/{len(test_files)} Testdateien erfolgreich')
    
    # Prüfe ob algs4/data noch existiert
    old_path = Path("algs4/data")
    if old_path.exists():
        print(f'⚠️  Altes Verzeichnis {old_path} existiert noch!')
        return False
    else:
        print(f'✅ Altes Verzeichnis algs4/data erfolgreich entfernt')
    
    return success_count == len(test_files)

if __name__ == "__main__":
    success = validate_migration()
    if success:
        print(f'\n🎉 Migration erfolgreich validiert!')
    else:
        print(f'\n⚠️  Migration unvollständig!')
