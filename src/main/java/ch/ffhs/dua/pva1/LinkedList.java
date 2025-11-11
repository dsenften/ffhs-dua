package ch.ffhs.dua.pva1;

import java.util.Iterator;

/**
 * Diese Klasse implementiert eine doppelt verkettete Liste.
 *
 * @param <E> Der Typ der Elemente, die in dieser Liste gespeichert werden.
 *
 * @see ListBasic
 * @see java.util.List
 * @see Iterator
 *
 * @version 1.0
 *
 * @autor <a href="mailto:daniel.senften@ffhs.ch">Daniel Senften</a>
 */
@SuppressWarnings("all")
public class LinkedList<E> extends ListBasic<E> {

    @Override
    public int size() {
        // TODO
        return -1;
    }

    @Override
    public boolean isEmpty() {
        // TODO
        return false;
    }

    @Override
    public E get(int index) {
        // TODO
        return null;
    }

    @Override
    public E set(int index, E element) {
        // TODO
        return null;
    }

    @Override
    public boolean add(E element) {
        // TODO
        return true;
    }

    @Override
    public void add(int index, E element) {
        //TODO     
    }

    public boolean contains(Object o) {
        // TODO
        return false;
    }

    @Override
    public E remove(int index) {
        // TODO
        return null;
    }

    @Override
    public boolean remove(Object o) {
        // TODO
        return false;
    }

    @Override
    public void clear() {
        // TODO
    }

    @Override
    public Iterator<E> iterator() {
        return new LinkedListIterator();
    }

    // Weitere Methoden des List-Interfaces müssen nicht implementiert werden.

    private static class Node<E> {
        E element;
        Node<E> next;
        Node<E> prev;
    }

    private class LinkedListIterator implements Iterator<E> {

        @Override
        public boolean hasNext() {
            // TODO
            return false;
        }

        @Override
        public E next() {
            // TODO
            return null;
        }

        @Override
        public void remove() {
            // TODO
        }
    }

}
