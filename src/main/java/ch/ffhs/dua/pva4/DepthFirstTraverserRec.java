package ch.ffhs.dua.pva4;

/**
 * Klasse zum Traversieren eines Baumes mit Tiefensuche.
 * Am einfachsten kann die Tiefensuche rekursiv programmiert werden.
 */
public abstract class DepthFirstTraverserRec<N> 
{
	/**
	 * Traversiert einen Baum mit DepthFirst Strategie.
	 * @param node Die Wurzel des zu traversierenden Baumes.
	 */
	public void traverse(TreeNode<N> node) 
	{
		// TODO
	}
	
	/**
	 * Operation auf einem Knoten, bevor die Nachkommen besucht wurden.
	 */
	abstract protected void preOperation(N value);   
    
	/**
	 * Operation auf einem Knoten, nachdem die Nachkommen besucht wurden.
	 */
	abstract protected void postOperation(N value);  

}   
