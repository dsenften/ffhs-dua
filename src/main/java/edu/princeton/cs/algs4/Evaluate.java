package edu.princeton.cs.algs4;

/**
 * This Stack client uses two stacks to evaluate arithmetic expressions,
 * illustrating an essential computational process: interpreting a string
 * as a program and executing that program to compute the desired result.
 * With generics, we can use the code in a single Stack implementation to
 * implement one stack of String values and another stack of Double values.
 * For simplicity, this code assumes that the expression is fully parenthesized,
 * with numbers and characters separated by whitespace.
 */
@SuppressWarnings({"IfCanBeSwitch", "StatementWithEmptyBody"})
public class Evaluate {

    public static void main(String[] args) {

        Stack<String> ops = new Stack<>();
        Stack<Double> vals = new Stack<>();

        while (!StdIn.isEmpty()) { // Read token, push if operator.

            String s = StdIn.readString();

            if (s.equals("(")) ;
            else if (s.equals("+")) ops.push(s);
            else if (s.equals("-")) ops.push(s);
            else if (s.equals("*")) ops.push(s);
            else if (s.equals("/")) ops.push(s);
            else if (s.equals("sqrt")) ops.push(s);
            else if (s.equals(")")) { // Pop, evaluate, and push result if token is ")".

                String op = ops.pop();
                double v = vals.pop();

                if      (op.equals("+")) v = vals.pop() + v;
                else if (op.equals("-")) v = vals.pop() - v;
                else if (op.equals("*")) v = vals.pop() * v;
                else if (op.equals("/")) v = vals.pop() / v;
                else if (op.equals("sqrt")) v = Math.sqrt(v);

                vals.push(v);
            } // Token not operator or paren: push double value. else vals.push(Double.parseDouble(s));

        }
        StdOut.println(vals.pop());

    }
}
