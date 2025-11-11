# Aufgaben zu Bäumen

### Aufgabe 1

Analog zu den Traversierungen in 6.2.4 aus [SG] implementiere man rekursiv eine Traversierung für beliebige (nicht nur binäre) Bäume.

Implementiere Sie dazu eine Klasse DepthFirstTraverser

```java
package ch.ffhs.dua;
public abstract class DepthfirstTraverser<N> {
    public void traverse(TreeNode<N> node) { ... }
    public abstract  void preOperation(N value) { }   
    public abstract void postOperation(N value) { }   
}
```

In konkreten Subklassen sollte mindestens eine der beiden Methoden preOperation oder postOperation überschrieben sein. Für jeden Knoten k wird einmal preOperation(k.value()) und einmal postOrder(k.value()) aufgerufen, und zwar preOperation(k.value()) bevor die Kinder von k durchlaufen werden, und postOperation(k.value()) nachdem die Kinder von k durchlaufen worden sind.

(Falls nur die Methode preOperation überschrieben wird, so entspricht das der Preorder-Traversierung bei Binärbäumen, falls nur postOperation überschrieben wird, so entspricht das der Postorder-Traversierung bei Binärbäumen.)

### Aufgabe 2

Analog zu Aufgabe 1 implementiere man einen Traverser für beliebige (nicht nur binäre) Bäume, jedoch ohne Rekursion zu verwenden. Der Einfacheit halber können Sie sich hier Pre-Order-Traversierung beschränken:

Implementiere Sie dazu eine Klasse DepthFirstPreOrderTraverser.

### Aufgabe 3

Zu einem Baum erzeuge man einen Traverser als Iterator, der das Interface `Iterator<N>` implementiere. Dieser Iterator liefere die Knotenwerte in einer Pre-Order zurück. (Die remove Methode des Iterators soll eine UnsupportedOperationException werfen.)

(Hinweis: Sie können von Code des Traversers ohne Rekursion benutzen und anpassen. (Die rekursive Version kann ebenfalls verwendet werden, das ist aber komplizierter, da man die Rekursion unterbrechen muss; das könnte man machen, indem man die Rekursion in einem eigenen Thread laufen lässt und das Erzeuger-Verbraucher Muster verwendet).)

```java
package ch.ffhs.dua;
public abstract class DepthfirstTraverser<N> {
    public void traverse(TreeNode<N> node) { ... }
    public abstract void preOperation(N value) { }   
    public void traverse(TreeNode<N>) {
        ...
    }   
}
```

### Aufgabe 4

Die bis jetzt unterssuchten Traverser verfolgen eine depth-first Strategie. Ein Baum kann jedoch auch mit der Breitensuche (oder Level-Suche) traversiert werden. Bei der Breitensuche wird zuersz die Wurzel besucht, dann alle Knoten mit Tiefe 1 (die Kinder der Wurzel), dann die Knoten mit Tiefe 2 (Enkelknoten der Wurzel) usw.

Implementieren Sie einen Traverser, der die Knoten eines Baumes mit Breitensuche traversiert.

(Hinweis: In Analogie zur Tiefensuche muss hier nicht ein Stack, sondern eine Queue verwendet werden mit zu besuchenden Knoten.

* Dieser Queue wird zu Beginn die Wurzel des Baumes hinzugefügt.
* Folgende Schritte werden wiederholt, bis die Queue leer ist:
    * Der erste Knoten k der Queue wird entfernt und besucht.
    * Alle Kinder von k werden der Queue am Ende hinzugefügt.)

Verwenden Sie dazu die Klassenrümpfe in diesem Package.
