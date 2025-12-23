# Tourverschmelzung beim TSP und Clarke-Wright-Savings-Algorithmus

## Zusammenhang zwischen Tourverschmelzung und Clarke-Wright

Ja, die Tourverschmelzung hat **direkten Zusammenhang** mit dem Clarke-Wright-Savings-Algorithmus.
Beide Verfahren basieren auf dem gleichen Grundprinzip:

1. **Ausgangssituation**: Mehrere separate (Teil-)Touren
2. **Verschmelzung**: Systematisches Zusammenführen dieser Touren
3. **Optimierungskriterium**: Maximale Einsparung (Savings) bei der Verschmelzung

## Der Clarke-Wright-Savings-Algorithmus in einfachen Schritten

### Schritt 1: Initialzustand - Sternkonfiguration

**Was passiert:**

- Wir starten mit einem zentralen Depot (oft Knoten 0)
- Jeder Kunde wird einzeln vom Depot aus besucht und wieder zurück
- Wir haben also n separate "Touren" der Form: Depot → Kunde i → Depot

**Beispiel:**

```text
Depot (0) → Kunde 1 → Depot (0)
Depot (0) → Kunde 2 → Depot (0)
Depot (0) → Kunde 3 → Depot (0)
Depot (0) → Kunde 4 → Depot (0)
```

### Schritt 2: Savings-Berechnung

**Was passiert:**

- Für jedes Kundenpaar (i, j) berechnen wir die potenzielle Einsparung
- Die Savings-Formel lautet: **s(i,j) = d(0,i) + d(0,j) - d(i,j)**

**Bedeutung:**

- d(0,i) = Distanz vom Depot zu Kunde i
- d(0,j) = Distanz vom Depot zu Kunde j
- d(i,j) = Direkte Distanz zwischen Kunde i und j
- s(i,j) = Eingesparte Distanz bei Verbindung von i und j

**Intuition:**
Statt zwei separate Touren zu fahren (0→i→0 und 0→j→0), fahren wir eine kombinierte Tour (0→i→j→0).
Die Einsparung ist: (0→i→0) + (0→j→0) - (0→i→j→0)

### Schritt 3: Sortierung der Savings

**Was passiert:**

- Alle berechneten Savings-Werte werden in **absteigender Reihenfolge** sortiert
- Wir erstellen eine Savings-Liste: s(i,j) ≥ s(k,l) ≥ s(m,n) ≥ ...

**Beispiel:**

```text
s(1,3) = 25  (höchste Einsparung)
s(2,4) = 18
s(1,2) = 12
s(3,4) = 8
s(2,3) = 5   (niedrigste Einsparung)
```

### Schritt 4: Tourverschmelzung (iterativ)

**Was passiert:**

- Wir gehen die sortierte Savings-Liste von oben nach unten durch
- Für jedes Kundenpaar (i,j) prüfen wir: Können wir die Touren verschmelzen?

**Verschmelzungsbedingungen:**

1. Kunde i ist **Endpunkt** einer Tour (nicht in der Mitte)
2. Kunde j ist **Endpunkt** einer anderen Tour (nicht in der Mitte)
3. Beide Kunden sind in **verschiedenen** Touren
4. Die Kapazitätsbeschränkung wird nicht verletzt (falls vorhanden)

**Wenn alle Bedingungen erfüllt sind:**
→ Verbinde die beiden Touren über die Kante (i,j)

### Schritt 5: Terminierung

**Was passiert:**

- Der Algorithmus endet, wenn alle Savings abgearbeitet sind
- Resultat: Eine oder mehrere Touren (je nach Kapazitätsbeschränkungen)

## Detailliertes Beispiel mit Visualisierung

### Ausgangssituation

Gegeben: 4 Kunden (1,2,3,4) und 1 Depot (0)

**Distanzmatrix:**

```text
     0    1    2    3    4
0    0   10   15   20   25
1   10    0   35   30   20
2   15   35    0   15   30
3   20   30   15    0   15
4   25   20   30   15    0
```

### Schritt-für-Schritt Durchführung

#### 1. Initialzustand (Sternkonfiguration)

```text
Tour 1: 0 → 1 → 0  (Länge: 20)
Tour 2: 0 → 2 → 0  (Länge: 30)
Tour 3: 0 → 3 → 0  (Länge: 40)
Tour 4: 0 → 4 → 0  (Länge: 50)

Gesamtlänge: 140
```

#### 2. Savings berechnen

Für alle Paare (i,j):

```text
s(1,2) = d(0,1) + d(0,2) - d(1,2) = 10 + 15 - 35 = -10 (negativ!)
s(1,3) = d(0,1) + d(0,3) - d(1,3) = 10 + 20 - 30 = 0
s(1,4) = d(0,1) + d(0,4) - d(1,4) = 10 + 25 - 20 = 15  ✓
s(2,3) = d(0,2) + d(0,3) - d(2,3) = 15 + 20 - 15 = 20  ✓
s(2,4) = d(0,2) + d(0,4) - d(2,4) = 15 + 25 - 30 = 10  ✓
s(3,4) = d(0,3) + d(0,4) - d(3,4) = 20 + 25 - 15 = 30  ✓ (max!)
```

#### 3. Sortierte Savings-Liste

```text
1. s(3,4) = 30
2. s(2,3) = 20
3. s(1,4) = 15
4. s(2,4) = 10
5. s(1,3) = 0
6. s(1,2) = -10
```

#### 4. Verschmelzung durchführen

##### Iteration 1: s(3,4) = 30

- Kunde 3 ist Endpunkt von Tour 3: 0→3→0 ✓
- Kunde 4 ist Endpunkt von Tour 4: 0→4→0 ✓
- Verschiedene Touren ✓
- **Verschmelzung möglich!**

```text
Neue Tour: 0 → 3 → 4 → 0  (Länge: 20 + 15 + 25 = 60)
Vorher: (0→3→0) + (0→4→0) = 40 + 50 = 90
Ersparnis: 90 - 60 = 30 ✓

Aktuelle Touren:
Tour 1: 0 → 1 → 0  (20)
Tour 2: 0 → 2 → 0  (30)
Tour 3/4: 0 → 3 → 4 → 0  (60)
Gesamtlänge: 110 (Ersparnis: 30)
```

##### Iteration 2: s(2,3) = 20

- Kunde 2 ist Endpunkt von Tour 2: 0→2→0 ✓
- Kunde 3 ist Endpunkt von Tour 3/4: 0→3→4→0 ✓
- Verschiedene Touren ✓
- **Verschmelzung möglich!**

```text
Neue Tour: 0 → 2 → 3 → 4 → 0  (Länge: 15 + 15 + 15 + 25 = 70)
Vorher: (0→2→0) + (0→3→4→0) = 30 + 60 = 90
Ersparnis: 90 - 70 = 20 ✓

Aktuelle Touren:
Tour 1: 0 → 1 → 0  (20)
Tour 2/3/4: 0 → 2 → 3 → 4 → 0  (70)
Gesamtlänge: 90 (Ersparnis: 50)
```

##### Iteration 3: s(1,4) = 15

- Kunde 1 ist Endpunkt von Tour 1: 0→1→0 ✓
- Kunde 4 ist Endpunkt von Tour 2/3/4: 0→2→3→4→0 ✓
- Verschiedene Touren ✓
- **Verschmelzung möglich!**

```text
Neue Tour: 0 → 1 → 4 → 3 → 2 → 0
(wir müssen die Richtung von Tour 2/3/4 umdrehen)
Länge: 10 + 20 + 15 + 15 + 15 = 75

Oder: 0 → 2 → 3 → 4 → 1 → 0
Länge: 15 + 15 + 15 + 20 + 10 = 75

Aktuelle Touren:
Tour gesamt: 0 → 2 → 3 → 4 → 1 → 0  (75)
Gesamtlänge: 75 (Ersparnis: 65)
```

### Endergebnis

**Optimierte Tour:** 0 → 2 → 3 → 4 → 1 → 0
**Länge:** 75
**Ersparnis gegenüber Initialzustand:** 140 - 75 = 65 (46% Reduktion!)

## Wichtige Hinweise für die Lehre

### 1. Negative Savings

- Wenn s(i,j) < 0: Die Verschmelzung würde die Tour **verlängern**
- Solche Paare werden **nicht** verschmolzen
- Beispiel: s(1,2) = -10 bedeutet, es ist besser, separate Touren zu behalten

### 2. Reihenfolge ist wichtig

- Wir bearbeiten Savings in **absteigender** Reihenfolge
- Grund: Maximale Einsparungen zuerst realisieren
- Greedy-Ansatz: Lokale Optima führen zu guten (nicht optimalen) Lösungen

### 3. Endpunkt-Bedingung

- Nur Endpunkte können verschmolzen werden
- Warum? Sonst entstehen ungültige Touren (kein Hamiltonscher Kreis)
- Beispiel: In 0→2→3→0 ist Kunde 3 ein Endpunkt, Kunde 2 nicht

### 4. Kapazitätsbeschränkungen (CVRP)

- Bei Vehicle Routing Problems mit Kapazität
- Zusätzliche Bedingung: Gesamtbedarf der Tour ≤ Fahrzeugkapazität
- Falls verletzt: Verschmelzung ablehnen

## Pädagogische Tipps

1. **Visualisierung**: Zeichnen Sie jeden Schritt auf der Tafel/Folien
2. **Hands-On**: Lassen Sie Studierende ein kleines Beispiel selbst durchrechnen
3. **Intuition**: Betonen Sie die Savings-Intuition (Wegfall von 2× Depot-Kanten)
4. **Komplexität**: O(n²) für Savings-Berechnung, O(n² log n) für Sortierung
5. **Qualität**: Typischerweise 5-15% über optimaler Lösung (sehr gut für Heuristik!)

## Vergleich zu anderen Heuristiken

| Heuristik | Konstruktionsart | Qualität | Komplexität |
|-----------|------------------|----------|-------------|
| Clarke-Wright | Verschmelzung | Gut (5-15%) | O(n² log n) |
| Nearest Neighbor | Einfügung | Mittel (20-30%) | O(n²) |
| 2-Opt | Verbesserung | Sehr gut | O(n²) pro Iteration |

## Zusammenfassung

Der Clarke-Wright-Savings-Algorithmus ist eine **konstruktive Heuristik**,
die durch systematische **Tourverschmelzung** arbeitet:

1. Start: Sternkonfiguration (n einzelne Touren)
2. Berechne alle möglichen Einsparungen (Savings)
3. Sortiere Savings absteigend
4. Verschmelze Touren greedily nach Savings-Wert
5. Beachte: Nur Endpunkte, verschiedene Touren, Kapazität

**Kernidee der Tourverschmelzung:**
Zwei Depot-Kanten fallen weg, eine Kunden-Kante kommt hinzu → Netto-Einsparung!
