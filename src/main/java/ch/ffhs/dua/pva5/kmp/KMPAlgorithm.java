package ch.ffhs.dua.pva5.kmp;

import javax.swing.*;

public class KMPAlgorithm {

    private final JTextArea jta;
    private final JTextArea randJta;
    private int i;
    private int j;
    private int tableI;
    private int tableJ;
    private char[] textChars;
    private char[] musterChars;
    private int[] randTabelle;
    private int matches;
    private int deltaS;
    private int rand;


    public KMPAlgorithm(String text, String muster, JTextArea jta, JTextArea randJta) {

        this.textChars = text.toCharArray();
        this.musterChars = muster.toCharArray();
        this.jta = jta;
        this.randJta = randJta;
        i = 0;
        j = 0;
        matches = 0;
        erzeugeRandTabelle(muster);

    }

    public void reset(String text, String muster) {
        this.textChars = text.toCharArray();
        this.musterChars = muster.toCharArray();
        i = 0;
        j = 0;
        tableI = 0;
        tableJ = 0;
        matches = 0;
        erzeugeRandTabelle(muster);
    }

    public boolean kmpSchritt() {

        jta.append(textChars[i] + " == " + musterChars[j] + " bei Index i=" + i + " und j=" + j + "\n");
        tableI = i;
        tableJ = j;
        boolean match = false;

        if (textChars[i] == musterChars[j]) {
            // match
            jta.append("match: i und j inkrementieren.\n");
            j++;
            i++;
            deltaS = 0;
            match = true;

        } else {
            // mismatch
            jta.append("mismatch:\n");
            if (j == 0) {
                deltaS = 1;
                i++;
                j = 0;
                jta.append("Delta s = " + deltaS + "\n");

            } else if (j == 1) {
                deltaS = 1;
                j = 0;
                jta.append("Delta s = " + deltaS + "\n");

            } else {
                rand = randTabelle[j - 1];
                jta.append("Rand = " + rand + "\n");
                deltaS = j - rand;
                jta.append("Delta s = (j - Rand) = " + j + " - " + rand + " = " + deltaS + "\n");
                j = rand;
            }


            jta.append("i_neu = " + i + " und j_neu = " + j + "\n");

        }

        if (j >= musterChars.length) {
            rand = randTabelle[j - 1];
            jta.append("Patternmatch\n");
            jta.append("Für die Berechnung von j_neu und Delta S geht man so vor, als h�tte man ein Mismatch hinter dem Pattern.\n");
            jta.append("Rand = " + rand + "\n");

            deltaS = j - rand;
            jta.append("Delta s = (j - Rand) = " + j + " - " + rand + " = " + deltaS + "\n");

            j = rand;
            jta.append("i_neu = " + i + " und j_neu = " + j + "\n");
            match = false;
        }

        return match;
    }


    /**
     * Bestimmt den Rand eines (Teil-)Wortes.
     *
     * @param s Zu ueberpruefende Zeichenkette
     * @return Groesse des Randes
     */
    public int bestimmeRand(String s) {
        int rand = 0;

        for (int i = 1; i < s.length(); i++) {

            //System.out.println(s.substring(0, i)+" == "+s.substring(s.length()-i));

            if (s.substring(0, i).equals(s.substring(s.length() - i))) {
                rand = i;
            }

        }
        return rand;
    }


    public void erzeugeRandTabelle(String s) {

        randTabelle = new int[s.length()];
        randJta.setText("");
        randJta.append("Randtabelle:\n");
        for (int i = 0; i < s.length() - 1; i++) {

            randTabelle[i] = bestimmeRand(s.substring(0, i + 1));
            //System.out.println(s.substring(0,i+1)+" / Rand("+i+"): "+randTabelle[i]);
            randJta.append(s.substring(0, i + 1) + " / Rand: " + randTabelle[i] + "\n");
        }
        randTabelle[s.length() - 1] = bestimmeRand(s);
        //System.out.println(s+" / Rand("+i+"): "+randTabelle[s.length()-1]);
        randJta.append(s + " / Rand: " + randTabelle[s.length() - 1] + "\n");

    }

    public int getI() {
        return i;
    }

    public int getJ() {
        return j;
    }

    public int getTableI() {
        return tableI;
    }

    public int getTableJ() {
        return tableJ;
    }

    public int[] getRandTabelle() {
        return randTabelle;
    }

    public int getMatches() {
        return matches;
    }

    public int getDeltaS() {
        return deltaS;
    }

    public int getRand() {
        return rand;
    }


}
