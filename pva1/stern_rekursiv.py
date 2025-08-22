#!/usr/bin/env python3
"""
Aufgabe 1.9: Rekursive Sternzeichnung mit matplotlib

Zeichnet einen Stern durch eine rekursiv definierte Python-Funktion unter Verwendung 
der matplotlib-Bibliothek.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches


def zeichne_stern(ax, x, y, groesse, tiefe):
    """
    Zeichnet einen Stern rekursiv.
    
    Args:
        ax: Matplotlib Axes-Objekt
        x, y: Zentrumskoordinaten
        groesse: Größe des Sterns
        tiefe: Rekursionstiefe (0 = nur Grundform)
    """
    if tiefe < 0:
        return
    
    # Zeichne das Kreuz (Grundform des Sterns)
    arm_laenge = groesse / 3
    arm_breite = groesse / 15
    
    # Horizontaler Balken
    rect_h = patches.Rectangle(
        (x - arm_laenge/2, y - arm_breite/2), 
        arm_laenge, arm_breite, 
        facecolor='black'
    )
    ax.add_patch(rect_h)
    
    # Vertikaler Balken
    rect_v = patches.Rectangle(
        (x - arm_breite/2, y - arm_laenge/2), 
        arm_breite, arm_laenge, 
        facecolor='black'
    )
    ax.add_patch(rect_v)
    
    # Rekursive Aufrufe an den vier Enden des Kreuzes
    if tiefe > 0:
        neue_groesse = groesse / 3
        offset = arm_laenge / 2
        
        # Oben
        zeichne_stern(ax, x, y + offset, neue_groesse, tiefe - 1)
        # Unten  
        zeichne_stern(ax, x, y - offset, neue_groesse, tiefe - 1)
        # Links
        zeichne_stern(ax, x - offset, y, neue_groesse, tiefe - 1)
        # Rechts
        zeichne_stern(ax, x + offset, y, neue_groesse, tiefe - 1)


def main():
    """Hauptfunktion zum Zeichnen des rekursiven Sterns."""
    fig, ax = plt.subplots(1, 1, figsize=(10, 10))
    
    # Koordinatensystem konfigurieren
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal')
    ax.axis('off')  # Achsen ausblenden
    
    # Titel setzen
    ax.set_title('Ein Stern', fontsize=16, pad=20)
    
    # Stern zeichnen (Tiefe 2 für 3 Rekursionsebenen wie im Bild)
    zeichne_stern(ax, 0, 0, 3, 2)
    
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()