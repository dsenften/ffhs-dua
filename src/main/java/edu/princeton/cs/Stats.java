package edu.princeton.cs;

import edu.princeton.cs.algs4.Bag;
import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;

/**
 * The class Stats illustrates a typical Bag client. The task is simply to
 * compute the average and the sample standard deviation of the double values
 * on standard input. If there are N numbers on standard input, their average
 * is computed by adding the numbers and dividing by N; their sample standard
 * deviation is computed by adding the squares of the difference between each
 * number and the average, dividing by N–1, and taking the square root.
 * <p>
 * The order in which the numbers are considered is not relevant for either
 * of these calculations, so we save them in a Bag and use the foreach
 * construct to compute each sum.
 */
public class Stats {

    public static void main(String[] args) {

        Bag<Double> numbers = new Bag<>();
        
        while (!StdIn.isEmpty())
            numbers.add(StdIn.readDouble());
        int N = numbers.size();

        double sum = 0.0;
        for (double x : numbers)
            sum += x;

        double mean = sum / N;
        sum = 0.0;

        for (double x : numbers)
            sum += (x - mean) * (x - mean);

        double std = Math.sqrt(sum / (N - 1));

        StdOut.printf("Mean: %.2f\n", mean);
        StdOut.printf("Std dev: %.2f\n", std);
    }
}
