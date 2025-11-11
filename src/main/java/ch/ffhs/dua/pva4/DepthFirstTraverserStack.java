package ch.ffhs.dua.pva4;

/**
 * Klasse zum Traversieren eines Baumes mit Tiefensuche.
 * Diese Implementierung verwende keine Rekursion, sondern einen Stack.
 */
public abstract class DepthFirstTraverserStack<N> {

    /**
     * Traversiert einen Baum mit Tiefensuche.
     *
     * @param root Die Wurzel des zu traversierenden Baumes.
     */
    public void traverse(TreeNode<N> root) {
        // TODO
    }

    /**
     * Operation auf einem Knoten bei der Traversierung;
     * die Operation wird durchgeführt,
     * bevor die Nachkommen besucht werden.
     */
    abstract protected void visitNode(N value);

}   
