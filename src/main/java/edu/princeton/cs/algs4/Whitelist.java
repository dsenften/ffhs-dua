package edu.princeton.cs.algs4;

/**
 * Usage:
 *   $ java Whitelist largeW.txt < largeT.txt
 *   499569
 *   984875
 *   295754
 *   207807
 *   140925
 *   161828
 *   ...
 *
 */
public class Whitelist {

    public static void main(String[] args) {

        int[] w = new In(args[0]).readAllInts();

        StaticSETofInts set = new StaticSETofInts(w);
        while (!StdIn.isEmpty()) { // Read key, print if not in whitelist.
            int key = StdIn.readInt();
            if (set.rank(key) == -1)
                StdOut.println(key);
        }
    }
}
