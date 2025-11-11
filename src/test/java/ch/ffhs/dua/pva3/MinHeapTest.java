package ch.ffhs.dua.pva3;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class MinHeapTest {

    private MinHeap heap;

    @BeforeEach
    void setUp() {
        heap = new MinHeap(15);
        heap.insert(5);
        heap.insert(3);
        heap.insert(17);
        heap.insert(10);
        heap.insert(9);
    }

    @Test
    @DisplayName("insert(5)")
    void insert() {
        assertEquals(3, heap.remove());
        assertEquals(5, heap.remove());
        assertEquals(9, heap.remove());
    }

    @Test
    @DisplayName("toString()")
    void print() {
        String expected = """
                 PARENT : 3 LEFT CHILD : 5 RIGHT CHILD :17
                 PARENT : 5 LEFT CHILD : 10 RIGHT CHILD :9
                """;
        assertEquals(expected, heap.toString());
    }
}
