package ch.ffhs.dua.pva5;

import java.util.Iterator;

/**
 * Teil-Implementierung einer HashSet Klasse.
 * Kollisionen sollen mit geketten Listen behandelt werden.
 *
 * @param <E>
 */
@SuppressWarnings("all")
public class LLHashSet<E> extends SetBasic<E> {

    @Override
    public boolean contains(Object o) {
        return false;
    }

    @Override
    public boolean add(E e) {
        return false;
    }

    @Override
    public boolean remove(Object o) {
        // TODO
        return false;
    }


    @Override
    public Iterator<E> iterator() {
        return null;
    }

    @Override
    public int size() {
        // TODO
        return 0;
    }

    @Override
    public boolean isEmpty() {
        // TODO
        return false;
    }

    @Override
    public void clear() {
        // TODO
    }
}
