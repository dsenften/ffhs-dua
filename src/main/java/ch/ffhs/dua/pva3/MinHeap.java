package ch.ffhs.dua.pva3;

/**
 * Java Program to Implement Heaps by Illustrating Min Heap
 *
 * @see <a href="https://www.geeksforgeeks.org/min-heap-in-java/">Min Heap in Java</a>
 */
class MinHeap {

    // Initializing front as static with unity
    private static final int FRONT = 1;

    // Member variables of this class
    private final int[] Heap;
    private final int maxsize;
    private int size;

    /**
     * Construct a MinHeap with {@code maxsize} elements.
     *
     * @param maxsize elements for this heap
     */
    public MinHeap(int maxsize) {

        this.maxsize = maxsize;
        this.size = 0;

        Heap = new int[this.maxsize + 1];
        Heap[0] = Integer.MIN_VALUE;
    }

    public static void main(String[] arg) {

        // Display message
        System.out.println("The Min Heap is ");

        // Creating object of class in main() method
        MinHeap minHeap = new MinHeap(15);

        // Inserting element to minHeap
        minHeap.insert(5);
        minHeap.insert(3);
        minHeap.insert(17);
        minHeap.insert(10);
        minHeap.insert(84);
        minHeap.insert(19);
        minHeap.insert(6);
        minHeap.insert(22);
        minHeap.insert(9);

        // Print all elements of the heap
      

        // Removing minimum value from above heap and printing it
        System.out.println("The Min val is " + minHeap.remove());
    }

    // Returning the position of the parent for the node currently at pos

    /**
     * Returning the position of the parent for the node currently at {@code position}.
     *
     * @param position to start with
     * @return parent position of thos node
     */
    private int parent(int position) {
        return position / 2;
    }

    /**
     * Returning the position of the left child for the node currently at
     * {@code position}.
     *
     * @param position to start with
     * @return left child of current node
     */
    private int leftChild(int position) {
        return (2 * position);
    }

    // Returning the position of the right child for the node currently at pos

    /**
     * Returning the position of the right child for the node currently at
     * {@code position}.
     *
     * @param position to start with
     * @return right child of current node
     */
    private int rightChild(int position) {
        return (2 * position) + 1;
    }

    /**
     * Returning {@code true} if the passed node is a leaf node.
     *
     * @param position to look at
     * @return {@code true} if the passed node is a leaf node
     */
    private boolean isLeaf(int position) {
        return position > (size / 2) && position <= size;
    }

    /**
     * To swap two nodes of the heap.
     *
     * @param first  node position
     * @param second node position
     */
    private void swap(int first, int second) {
        int tmp;
        tmp = Heap[first];

        Heap[first] = Heap[second];
        Heap[second] = tmp;
    }

    /**
     * To heapify the node at position.
     *
     * @param position to start with
     */
    private void minHeapify(int position) {

        // If the node is a non-leaf node and greater than any of its child
        if (!isLeaf(position)) {
            if (Heap[position] > Heap[leftChild(position)]
                    || Heap[position] > Heap[rightChild(position)]) {

                // Swap with the left child and heapify the left child
                if (Heap[leftChild(position)]
                        < Heap[rightChild(position)]) {
                    swap(position, leftChild(position));
                    minHeapify(leftChild(position));
                }

                // Swap with the right child and heapify the right child
                else {
                    swap(position, rightChild(position));
                    minHeapify(rightChild(position));
                }
            }
        }
    }

    /**
     * To insert a node into the heap.
     *
     * @param element to be inserted
     */
    public void insert(int element) {

        if (size >= maxsize) {
            return;
        }

        Heap[++size] = element;
        int current = size;

        while (Heap[current] < Heap[parent(current)]) {
            swap(current, parent(current));
            current = parent(current);
        }
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= size / 2; i++) {
            sb.append(" PARENT : ").append(Heap[i])
                    .append(" LEFT CHILD : ").append(Heap[2 * i])
                    .append(" RIGHT CHILD :").append(Heap[2 * i + 1])
                    .append("\n");
        }
        return sb.toString();
    }

    /**
     * To remove and return the minimum element from the heap.
     *
     * @return minimum element from the heap
     */
    public int remove() {

        int popped = Heap[FRONT];
        Heap[FRONT] = Heap[size--];
        minHeapify(FRONT);

        return popped;
    }
}
