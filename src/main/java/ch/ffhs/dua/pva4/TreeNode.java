package ch.ffhs.dua.pva4;

import java.util.List;

/**
 * Knoteninterface für Bäume, die traversiert werden müssen.
 * @author urs-martin
 */
public interface TreeNode<N> 
{
    /** 
     * @return Liefert den Wert des Knotens.
     */
	N value();
    
	/**
	 * @return Gibt eine Liste mit allen Kinderknoten zurück.
	 */
    List<TreeNode<N>> children();
}
