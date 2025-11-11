package ch.ffhs.dua.pva3;

@SuppressWarnings("all")
public class HeapSort {
    /**
     * Sortiert ein Array mit Heapsort.
     *
     * @param array Zu sortierender Array
     */
    public static void sort(int[] array) {
        sort(array, 0, array.length - 1);
    }

    /**
     * Sortiert ein Teilstück eines Array s mit Heapsort.
     *
     * @param array Zu sortierender Array
     * @param start Index des ersten Elementes des zu sortierenden Teils.
     * @param end   Index des letzten Elementes des zu sortierenden Teils.
     */
    public static void sort(int[] array, int start, int end) {
        // TODO
    }

    /**
     * Erzeugt aus einem angegebenen Teilstück einen Heap.
     *
     * @param array Zu sortierender Array
     * @param start Index des ersten Elementes, aus dem ein Heap erzeugt werden sollte.
     *              Das ist auch der Index der Wurzel des Heaps; die Kinder der Wurzel
     *              liegen dann an den Position start+1 und start+2.
     * @param end   Index des letzten Elementes des Stücks, aus dem ein Heap erzeugt werden sollte.
     */
    public static void makeHeap(int[] array, int start, int end) {
        // TODO
    }

    /**
     * Hilfsmethode für Heapsort:
     * Aus einem Teilstück eines Arrays mit den Grenzen start und end
     * sollte ein Heap erzeugt werden. Für Indices grösser als index
     * sei die Heap-Eigenschaft bereits erfüllt.
     * Die Methode ordnet das Stück zwischen index und end so um,
     * dass die Heap-Eigenschaft für alle Elemente erfüllt ist.
     */
    static void sink(int[] array, int start, int end, int index) {
        // TODO	(Implementieren Sie diese Methode, wenn Sie sie für die Sort-Methoden brauchen.
    }

    /**
     * Entfernt das Wurzel-Element eines Heaps, baut den Heap um,
     * sodass er nach dem Entfernen wieder ein Heap ist (mit einem Element weniger),
     * und setzt das ehemalige Wurzel-Element an die vormals letzte Stelle im Heap
     * (die nun nicht mehr zum Heap gehört).
     *
     * @param array Ein Array, das als Teilstück einen heap enthält.
     * @param start Indes der Wurzel des heaps
     * @param end   Index des letzten Heap-Elements.
     */
    public static void removeHeapRoot(int[] array, int start, int end) {
        // TODO	(Implementieren Sie diese Methode, wenn Sie sie für die Sort-Methoden brauchen.
    }

    /**
     * Berechnet den Index des linken Kind-Elementes in einem Heap.
     *
     * @param parentIndex Index des Elternschlüssels
     * @param offset      Offset für Heap-Eigenschaft: entspricht
     *                    dem Index der Heap-Wurzel - 1
     * @return Index des linken Kindes
     */
    static int leftChild(int parentIndex, int offset) {
        return 2 * parentIndex - offset;
    }

    /**
     * Berechnet den Index des rechten Kind-Elementes in einem Heap.
     *
     * @param parentIndex Index des Elternschlüssels
     * @param offset      Offset für Heap-Eigenschaft: entspricht
     *                    dem Index der Heap-Wurzel - 1
     * @return Index des rechten Kindes
     */
    static int rightChild(int parentIndex, int offset) {
        return leftChild(parentIndex, offset) + 1;
    }


}
