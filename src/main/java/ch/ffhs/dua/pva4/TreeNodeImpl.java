package ch.ffhs.dua.pva4;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * Standard-Implementierung für Tree-Nodes
 * @author urs-martin
 *
 * @param <N> Typ des Knotenwertes
 */
public class TreeNodeImpl<N> implements TreeNode<N> 
{

	private final N value;
	
	private final ArrayList<TreeNode<N>> children = new ArrayList<>();
	
	/**
	 * Erzeugt einen neuen Wurzel-Knoten.
	 */
	public TreeNodeImpl(N value)
	{
		this.value = value;
	}
	
	/**
	 * Erzeugt einen Kinder-Knoten mit gegebenem Wert
	 * @param value Der Wert des neuen Knotens.
	 * @return Gibt den neuen Knoten zurück.
	 */
	public TreeNodeImpl<N> addNode(N value)
	{
		TreeNodeImpl<N> newChild = new TreeNodeImpl<>(value);
		children.add(newChild);
		return newChild;
	}
	
	/**
	 * Liefert den Wert des Knotens.
	 */
	@Override
	public N value() 
	{
		return value;
	}

	/**
	 * Liefert eine Liste mit allen Kindern.
	 */
	@Override
	public List<TreeNode<N>> children() 
	{
		return Collections.unmodifiableList(children);
	}
	
	
}
