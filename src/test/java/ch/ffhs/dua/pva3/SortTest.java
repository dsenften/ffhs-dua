package ch.ffhs.dua.pva3;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.function.Consumer;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

import static org.junit.jupiter.api.Assertions.*;

class SortTest {
    private ArrayList<int[]> arrays;

    private static List<Integer> toList(int[] array) {
        return IntStream.of(array).boxed().collect(Collectors.toList());
    }

    /**
     * Hilfsmethode; testet, ob ein Array ein Heap ist.
     */
    static boolean isHeap(int[] array) {
        return isHeap(array, 0, array.length - 1);
    }

    /**
     * Hilfsmethode; testet, ob ein Teilstück eines Arrays ein Heap ist.
     */
    static boolean isHeap(int[] array, int start, int end) {
        int offset = start - 1;
        int length = end - start + 1;
        for (int index = length; index > 1; index--) {
            if (array[offset + index] > array[offset + index / 2]) return false;
        }
        return true;
    }

    @BeforeEach
    public void init() {
        arrays = new ArrayList<>();
        arrays.add(new int[]{});
        arrays.add(new int[]{1});
        arrays.add(new int[]{2, 1});
        arrays.add(new int[]{1, 1, 2, 2, 3});
        arrays.add(new int[]{1, 1, 2, 2, 1});
        arrays.add(new int[]{2, 1});
        arrays.add(new int[]{1, 2, 3, 4, 5, 6, 7, 8, 9, 10});
        arrays.add(new int[]{10, 9, 8, 7, 6, 5, 4, 3, 2, 1});
        arrays.add(new int[]{10, 3, 5, 3, 6, 3, 2, 8, 7, 2, 2});
        arrays.add(new int[10]);
    }

    private void testSort(Consumer<int[]> sorter) {
        for (int[] array : arrays) {
            int[] arrS = array.clone();
            Arrays.sort(arrS);
            sorter.accept(array);
            assertEquals(toList(arrS), toList(array));
        }
    }

    @Test
    void testInsertSort() {
        testSort(InsertSort::sort);
    }

    @Test
    void testQuickSort() {
        testSort(QuickSort::sort);
    }

    @Test
    void testQuickSortPlus() {
        int oldThr = QuickSort.THRESHOLD;
        try {
            QuickSort.THRESHOLD = 4;
            testSort(QuickSort::sortPlus);
        } finally {
            QuickSort.THRESHOLD = oldThr;
        }
    }

    /**
     * Tests für log2 Methode
     */
    @Test
    void testLog2() {
        assertSame(0, IntroSort.log2(1));
        assertSame(1, IntroSort.log2(2));
        assertSame(1, IntroSort.log2(3));
        assertSame(2, IntroSort.log2(4));
        assertSame(2, IntroSort.log2(5));
        assertSame(2, IntroSort.log2(7));
        assertSame(3, IntroSort.log2(8));
        assertSame(3, IntroSort.log2(9));
        assertSame(0, IntroSort.log2(0));
    }

    /**
     * Test makeHeap Methode
     */
    @Test
    void testHeap() {
        for (int[] array : arrays) {
            int[] arrayC = array.clone();
            HeapSort.makeHeap(array, 0, array.length - 1);
            assertTrue(isHeap(array));
            Arrays.sort(array);
            Arrays.sort(arrayC);
            assertArrayEquals(arrayC, array);
        }

        int[] array;
        array = new int[]{1, 2, 3, 4, 5, 6, 7};
        HeapSort.makeHeap(array, 0, array.length - 1);
        assertTrue(isHeap(array));

        array = new int[]{1, 2, 3, 4, 5, 6, 7};
        HeapSort.makeHeap(array, 1, array.length - 2);
        assertTrue(isHeap(array, 1, array.length - 2));
        assertSame(1, array[0]);
        assertSame(7, array[6]);

        array = new int[]{1, 2, 3, 4, 5, 6, 7, 8};
        HeapSort.makeHeap(array, 0, array.length - 1);
        assertTrue(isHeap(array));


        array = new int[]{1, 2, 3, 4, 5, 6, 7, 8};
        HeapSort.makeHeap(array, 1, array.length - 2);
        assertTrue(isHeap(array, 1, array.length - 2));
        assertSame(1, array[0]);
        assertSame(8, array[7]);
    }

    @Test
    void testRemoveHeapRoot() {
        for (int[] array : arrays) {
            if (array.length == 0) continue;
            int[] arrayClone = array.clone();
            Arrays.sort(arrayClone);
            HeapSort.makeHeap(array, 0, array.length - 1);
            assertTrue(isHeap(array));
            HeapSort.removeHeapRoot(array, 0, array.length - 1);
            assertTrue(isHeap(array, 0, array.length - 2));
            Arrays.sort(array);
            assertSame(arrayClone[array.length - 1], array[array.length - 1]);
            assertArrayEquals(array, arrayClone);
        }

        int[] array;
        int[] arrayClone;
        array = new int[]{8, 7, 6, 5, 4, 4, 3, 3, 2, 1};
        arrayClone = array.clone();
        assertTrue(isHeap(array));
        HeapSort.removeHeapRoot(array, 0, array.length - 1);
        assertTrue(isHeap(array, 0, array.length - 2));
        assertSame(arrayClone[0], array[array.length - 1]);
        Arrays.sort(array);
        Arrays.sort(arrayClone);
        assertArrayEquals(array, arrayClone);
    }

    @Test
    void testHeapSort() {
        testSort(HeapSort::sort);
    }

    @Test
    void testIntroSort() {
        testSort(IntroSort::sort);
    }

}
