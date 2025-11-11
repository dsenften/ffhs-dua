package ch.ffhs.dua.pva2;

import org.junit.jupiter.api.Test;

import java.math.BigInteger;

import static org.junit.jupiter.api.Assertions.assertEquals;

class ParkettierungTest {

    @Test
    void fibonacciTest() {
        BigInteger[] fibs = fibonacciZahlen(12);
        for (int n = 0; n < fibs.length; n++) {
            assertEquals(fibs[n], Parkettierung.anzahlParkettierungen(2, n));
            assertEquals(fibs[n], Parkettierung.anzahlParkettierungen(n, 2));
        }
    }

    @SuppressWarnings("SameParameterValue")
    private BigInteger[] fibonacciZahlen(int n) {
        BigInteger[] fibs = new BigInteger[n];
        fibs[0] = fibs[1] = BigInteger.ONE;
        for (int i = 2; i < n; i++) {
            fibs[i] = fibs[i - 1].add(fibs[i - 2]);
        }
        return fibs;
    }

    @Test
    void andereArgumente() {
        assertEquals(BigInteger.valueOf(6728L), Parkettierung.anzahlParkettierungen(6, 6));
        assertEquals(BigInteger.valueOf(12988816L), Parkettierung.anzahlParkettierungen(8, 8));
        assertEquals(BigInteger.valueOf(108435745L), Parkettierung.anzahlParkettierungen(8, 9));
        assertEquals(BigInteger.valueOf(108435745L), Parkettierung.anzahlParkettierungen(9, 8));
        assertEquals(BigInteger.valueOf(258584046368L), Parkettierung.anzahlParkettierungen(10, 10));
        assertEquals(new BigInteger("2444888770250892795802079170816"), Parkettierung.anzahlParkettierungen(16, 16));
    }

}
