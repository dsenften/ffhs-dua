# Aufgaben zu Sortierverfahren

1. Implementieren Sie "Sortieren durch Einfügen" für int-Arrays.
2. Implementieren Sie Quicksort für `int`-Arrays.
3. Testen Sie, für welche Grössen der zu sortierenden Arrays 
 `Sortieren durch Einfügen` bzw. Quicksort schneller ist.
4. Modifizieren Sie Quicksort so, dass bei den rekursiven Aufrufen bei kleinen 
  Argumenten `Sortieren duch Einfügen` aufgerufen wird. (Entscheiden Sie aufgrund der Überlegungen aus der vorherigen Aufgabe, wann der Wechsel auf `Sortieren duch Einfügen` erfolgen soll.)
5. Testen und beschreiben Sie, wie gross die Verbesserung aus Teilaufgabe 4
  gegnüber des reinen Quicksorts ist.
  <br>
  Quicksort ist eines der schnellsten Sortierverfahren, aber nur im Mittel. 
  Das Worstcase-Verhalten von Quicksort ist hingegen schlecht: <i>O</i>(n<sup>2</sup>).
  Im Gegensatz dazu ist Heapsort im Mittel etwas langsamer als Quicksort, aber 
  das Worstcase-Verhalten von Heapsort ist besser, nämlich <i>O</i>(n * log<sub>2</sub>(n)).
  <br>Introsort ist eine Kombination dieser beiden Verfahren: Man beginnt ein Array mit
  Quicksort zu sortieren (oder mit der Variante aus der vorhergehenden Aufgabe); 
  wird die Rekursionstiefe jedoch zu gross, dann ruft man nicht mehr Quicksort auf,
  sondern Heapsort. Eine Möglichkeit für einen Schwellwert zum Wechseln auf 
  Heapsort ist eine Rekursionstiefe von 2*log<sub>2</sub>(n).</br>
6. Implementieren Sie Heapsort, um ein Teilstück eines Arrays zu Sortieren.
7. Passen Sie Quicksort so an, dass die Rekursionstiefe als Parameter übergeben wird.
8. Kombinieren Sie diese beiden obigen Teilaufgaben, um Introsort zu 
  implementieren (mit dem Schwellwert von 2n*log<sub>2</sub>(n) für die Rekursionstiefe).

Verwenden Sie die Klassenrümpfe aus diesem Package.
