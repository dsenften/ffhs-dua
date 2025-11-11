package ch.ffhs.dua.pva5;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Arrays;

/**
 * This class provides a simple example of calculating the absolute value
 * of an integer using the Math.abs() method. The main() method demonstrates
 * this functionality by outputting the absolute value of -2147483648,
 * which in this case is still -2147483648.
 *
 * @see <a href="https://math.oxford.emory.edu/site/cs171/usingTheHashCodeMethod/">Using the hashCode() Method, </a>
 */
@SuppressWarnings("all")
public class HashValue {

    MessageDigest sha1 = MessageDigest.getInstance("SHA1");

    public HashValue() throws NoSuchAlgorithmException {
        String string = "Daniel Senften, wohnhaft in Kirchberg.";
        System.out.println("String: " + string);
        System.out.println("Hash: " + Arrays.toString(sha1.digest(string.getBytes())));
    }

    public static void main(String[] args) throws NoSuchAlgorithmException {

        HashValue hash = new HashValue();
        // prints -2147483648
        System.out.println(Math.abs(-2147483648));
    }
}
