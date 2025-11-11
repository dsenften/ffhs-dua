package ch.ffhs.dua.pva1;

import java.util.Collection;
import java.util.List;
import java.util.ListIterator;

/**
 * Basisimplementierung des {@link List}-Interfaces.
 * Alle Methoden werfen standardmässig eine {@link UnsupportedOperationException}.
 * Diese Klasse kann als Ausgangspunkt für eine teilweise Implementierung des List-Interfaces
 * verwendet werden.
 *
 * <p>Vererbende Klassen sollen die Methoden überschreiben, die tatsächlich benötigt werden,
 * während die nicht benötigten Methoden weiterhin die Standardausnahme werfen können.
 *
 * @param <E> Der Typ der Elemente, die in der Liste gespeichert werden sollen.
 *
 * @author <a href="mailto:daniel.senften@ffhs.ch">Daniel Senften</a>
 * @version 1.0
 */
public abstract class ListBasic<E> implements List<E> {

    @Override
    public boolean containsAll(Collection<?> c) {
        throw new UnsupportedOperationException();
    }

    @Override
    public boolean addAll(Collection<? extends E> c) {
        throw new UnsupportedOperationException();
    }

    @Override
    public boolean addAll(int index, Collection<? extends E> c) {
        throw new UnsupportedOperationException();
    }

    @Override
    public boolean removeAll(Collection<?> c) {
        throw new UnsupportedOperationException();
    }

    @Override
    public boolean retainAll(Collection<?> c) {
        throw new UnsupportedOperationException();
    }

    @Override
    public int lastIndexOf(Object o) {
        throw new UnsupportedOperationException();
    }

    @Override
    public ListIterator<E> listIterator() {
        throw new UnsupportedOperationException();
    }

    @Override
    public ListIterator<E> listIterator(int index) {
        throw new UnsupportedOperationException();
    }

    @Override
    public Object[] toArray() {
        throw new UnsupportedOperationException();
    }

    @Override
    public <T> T[] toArray(T[] a) {
        throw new UnsupportedOperationException();
    }

    @Override
    public List<E> subList(int fromIndex, int toIndex) {
        throw new UnsupportedOperationException();
    }

    @Override
    public int indexOf(Object o) {
        throw new UnsupportedOperationException();
    }

}
