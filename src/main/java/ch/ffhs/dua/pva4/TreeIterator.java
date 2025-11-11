package ch.ffhs.dua.pva4;

import java.util.Iterator;

/**
 * Ein Iterator, der in <a href="https://de.wikipedia.org/wiki/Tiefensuche">Depth-First</a> Reihenfolge alle Werte
 * der Knoten eines Baumes ausgibt.
 *
 * @param <N> Typ des Knotenwertes.
 */
public class TreeIterator<N> implements Iterator<N>
{
	/** 
	 * Erzeugt einen neuen Baum-Knoten-Iterator
	 * @param node Die Wurzel des zu traversierenden Baumes.
	 */
	public TreeIterator(TreeNode<N> node)
	{
		// TODO
	}

	@Override
	public boolean hasNext() 
	{
		// TODO
		return false;
	}

	@Override
	public N next() {
		// TODO
		return null;
	}
	
	// remove() muss nicht implementiert werden.
}
