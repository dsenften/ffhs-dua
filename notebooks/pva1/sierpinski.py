import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import warnings

# Unterdrücke matplotlib Warnungen
warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")


def draw_filled_triangle(x, y, size, color="black"):
    """Zeichnet ein gefülltes gleichschenkliges Dreieck"""
    height = size * np.sqrt(3) / 2

    # Dreieck-Koordinaten (Spitze oben)
    triangle_points = np.array(
        [
            [x, y + height * 2 / 3],  # Obere Spitze
            [x - size / 2, y - height / 3],  # Linke untere Ecke
            [x + size / 2, y - height / 3],  # Rechte untere Ecke
        ]
    )

    triangle = patches.Polygon(
        triangle_points, closed=True, facecolor=color, edgecolor=color
    )
    plt.gca().add_patch(triangle)


def sierpinski_iteration(triangles, iteration):
    """
    Führt eine Iteration der Sierpinski-Konstruktion durch
    triangles: Liste von (x, y, size) Tupeln
    """
    if iteration <= 1:
        return triangles

    new_triangles = []

    for x, y, size in triangles:
        # Größe der neuen kleineren Dreiecke
        new_size = size / 2
        height = size * np.sqrt(3) / 2

        # Drei neue Dreiecks-Positionen berechnen
        # Für korrekte Sierpinski-Konstruktion: Dreiecke berühren sich an den Ecken

        # Linkes unteres Dreieck
        left_x = x - new_size / 2
        left_y = y - height / 6

        # Rechtes unteres Dreieck
        right_x = x + new_size / 2
        right_y = y - height / 6

        # Oberes Dreieck
        top_x = x
        top_y = y + height / 3

        new_triangles.extend(
            [
                (left_x, left_y, new_size),
                (right_x, right_y, new_size),
                (top_x, top_y, new_size),
            ]
        )

    return sierpinski_iteration(new_triangles, iteration - 1)


def sierpinski(x, y, n, max_iterations=5):
    """
    Zeichnet das Sierpinski-Dreieck nach max_iterations Schritten
    """
    # Starte mit einem Dreieck
    initial_triangles = [(x, y, n)]

    # Führe die Iterationen durch
    final_triangles = sierpinski_iteration(initial_triangles, max_iterations)

    # Zeichne alle resultierenden Dreiecke
    for tri_x, tri_y, tri_size in final_triangles:
        draw_filled_triangle(tri_x, tri_y, tri_size)


def zeichne_sierpinski_progression():
    """
    Zeichnet die ersten 5 Iterationen des Sierpinski-Dreiecks
    """
    fig, axes = plt.subplots(1, 5, figsize=(20, 4))
    fig.suptitle("Sierpinski-Dreieck - Erste 5 Iterationen", fontsize=16)

    for i in range(5):
        plt.sca(axes[i])

        # Zeichne Sierpinski-Dreieck mit entsprechender Iteration
        sierpinski(0, 0, 3, max_iterations=i + 1)

        plt.xlim(-2, 2)
        plt.ylim(-1.5, 2)
        plt.gca().set_aspect("equal", adjustable="box")
        plt.title(f"Iteration {i + 1}")
        plt.axis("off")

    plt.tight_layout()
    plt.show()


# Alternative: Rekursive Implementierung nach dem "Kochrezept"
def sierpinski_recursive(x, y, n, level):
    """
    Rekursive Implementierung des Sierpinski-Dreiecks
    """
    # Rekursionsabbruch
    if level == 0:
        draw_filled_triangle(x, y, n)
        return

    # Rekursionsschritt: drei kleinere Dreiecke mit halber Größe
    new_size = n / 2
    height = n * np.sqrt(3) / 2

    # Positionen der drei Teildreiecke
    sierpinski_recursive(
        x - new_size / 2, y - height / 6, new_size, level - 1
    )  # Links unten
    sierpinski_recursive(
        x + new_size / 2, y - height / 6, new_size, level - 1
    )  # Rechts unten
    sierpinski_recursive(x, y + height / 3, new_size, level - 1)  # Oben


def zeichne_rekursive_version():
    """Zeigt die rekursive Version"""
    fig, axes = plt.subplots(1, 5, figsize=(20, 4))
    fig.suptitle("Sierpinski-Dreieck - Rekursive Implementierung", fontsize=16)

    for i in range(5):
        plt.sca(axes[i])

        sierpinski_recursive(0, 0, 3, i)

        plt.xlim(-2, 2)
        plt.ylim(-1.5, 2)
        plt.gca().set_aspect("equal", adjustable="box")
        plt.title(f"Rekursionstiefe {i}")
        plt.axis("off")

    plt.tight_layout()
    plt.show()


# Demonstration
if __name__ == "__main__":
    # Iterative Version (mathematisch korrekt)
    zeichne_sierpinski_progression()

    # Rekursive Version
    zeichne_rekursive_version()
