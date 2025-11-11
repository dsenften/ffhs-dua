package ch.ffhs.dua.pva4;

/**
 * Traverser-Klasse für Breitensuche. Ein Traverser besucht zuerst die Wurzel,
 * dann die Kinder der Wurzel, dann die Enkel usw.
 * <p>
 * Diese Suche ist auch unter dem Begriff LevelOrder bekannt.
 *
 * @param <N>
 */
public abstract class BreadthFirstTraverser<N> 
{
	/**
	 * Methode zum Traversieren eines Baumes.
	 * @param node Wurzelknoten des Baumes.
	 */
	public void traverse(TreeNode<N> node) 
	{
		//TODO
	}
	
	/**
	 * Diese Methode gibt an, was beim travsersieren gemacht werden sollte.
	 */
	protected abstract void visitNode(N value);   
    
}   
