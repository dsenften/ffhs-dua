package ch.ffhs.dua.pva5.kmp;

import javax.swing.*;
import javax.swing.table.TableModel;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class KMPFrame extends JFrame implements ActionListener {

    private final JTextField text;
    private final JTextField pattern;
    private final JButton start;
    private final JButton weiter;
    private final JTextArea jta;
    private final JTextArea randJta;
    private JTable table;
    private TableModel model;
    private JScrollPane scroll;
    private int position = 0;
    private KMPAlgorithm kmpAlgo;
    private int stepCounter;


    public KMPFrame() {

        super("Knuth-Morris-Pratt-Algorithmus - https://www.oliver-lazar.de/");

        JPanel p1 = new JPanel();
        p1.setLayout(new GridLayout(2, 1));
        JPanel p2 = new JPanel(new FlowLayout(FlowLayout.LEFT));
        p2.add(new JLabel("Zeichenkette: "));
        text = new JTextField(50);
        text.setText("XXXKOKOFXXXKOKOSNUSSXXXKOKOKOXXX");

        p2.add(text);
        p2.add(new JLabel("Muster: "));
        pattern = new JTextField(10);
        pattern.setText("KOKOS");
        //muster.setText("ababa");
        p2.add(pattern);
        p1.add(p2);

        JPanel p3 = new JPanel(new FlowLayout(FlowLayout.LEFT));
        start = new JButton("Start");
        start.addActionListener(this);
        p3.add(start);
        weiter = new JButton("weiter");
        weiter.addActionListener(this);
        weiter.setEnabled(false);
        p3.add(weiter);
        p1.add(p3);


        add(p1, BorderLayout.NORTH);

        JPanel southPanel = new JPanel(new BorderLayout());

        jta = new JTextArea(16, 50);
        jta.setEditable(false);
        JScrollPane scroll = new JScrollPane();
        scroll.getViewport().add(jta);
        southPanel.add(scroll, BorderLayout.CENTER);

        randJta = new JTextArea(10, 12);
        randJta.setEditable(false);
        randJta.setBackground(Color.LIGHT_GRAY);
        JScrollPane scroll2 = new JScrollPane();
        scroll2.getViewport().add(randJta);
        southPanel.add(scroll2, BorderLayout.EAST);

        add(southPanel, BorderLayout.SOUTH);

        setSize(1280, 720);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setVisible(true);
    }

    public static void main(String[] args) {
        new KMPFrame();
    }

    private void erzeugeTabelle() {

        if (table != null) {
            remove(scroll);
            table = null;
            scroll = null;
        }

        // Bestimme Anzahl Zeilen und Spalten
        int spalten = text.getText().length();

        String[] spaltenNamen = new String[text.getText().length()];
        for (int i = 0; i < text.getText().length(); i++) {
            spaltenNamen[i] = i + "";
        }

        Object[][] zeichen = new Object[3][spalten];
        char[] zArray = text.getText().toCharArray();
        for (int i = 0; i < zArray.length; i++) {
            zeichen[0][i] = zArray[i] + "";
        }
        char[] mArray = pattern.getText().toCharArray();
        for (int i = 0; i < mArray.length; i++) {
            zeichen[1][i] = mArray[i] + "";
            zeichen[2][i] = i + "";
        }

        table = new JTable(zeichen, spaltenNamen);
        Font font = new Font("Arial", Font.PLAIN, 28);
        table.setFont(font);
        table.setRowHeight(30);
        table.setDefaultRenderer(Object.class, new MyTableCellRenderer(kmpAlgo));

        scroll = new JScrollPane(table);
        scroll.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_AS_NEEDED);
        scroll.setHorizontalScrollBarPolicy(JScrollPane.HORIZONTAL_SCROLLBAR_AS_NEEDED);

        table.setRowSelectionAllowed(false);
        table.setColumnSelectionAllowed(false);
        table.setCellSelectionEnabled(false);
        model = table.getModel();


        add(scroll, BorderLayout.CENTER);
        int width = getWidth();
        int height = getHeight();
        pack();
        setSize(width, height);


    }

    private void verschiebeMuster() {

        position += kmpAlgo.getDeltaS();
        char[] mArray = pattern.getText().toCharArray();

        if ((position + mArray.length) > text.getText().length()) {
            JOptionPane.showMessageDialog(this, "Der Text wurde vollstaendig durchsucht!", "Fertig", JOptionPane.INFORMATION_MESSAGE);
            weiter.setEnabled(false);
            return;
        }

        for (int i = 0; i < text.getText().length(); i++) {
            if (i == position) {
                for (int j = 0; j < mArray.length; j++) {
                    model.setValueAt(mArray[j] + "", 1, i);
                    model.setValueAt(j + "", 2, i);
                    i++;
                }
                i--;
            } else {
                model.setValueAt("", 1, i);
                model.setValueAt("", 2, i);
            }

        }

    }

    @Override
    public void actionPerformed(ActionEvent e) {

        if (e.getSource() == start) {
            if (text.getText().length() < 10) {
                JOptionPane.showMessageDialog(this, "Bitte gib mindestens 10 Zeichen ein!", "Zu kurze Zeichenkette", JOptionPane.ERROR_MESSAGE);
            } else if (pattern.getText().length() < 2) {
                JOptionPane.showMessageDialog(this, "Bitte gib mindestens 2 Zeichen ein!", "Zu kurze Zeichenkette", JOptionPane.ERROR_MESSAGE);
            } else {
                if (kmpAlgo != null) {
                    kmpAlgo.reset(text.getText(), pattern.getText());
                    position = 0;
                } else {
                    kmpAlgo = new KMPAlgorithm(text.getText(), pattern.getText(), jta, randJta);
                }
                erzeugeTabelle();
                scroll.getViewport().setViewPosition(new Point(0, (int) jta.getSize().getHeight()));
                stepCounter = 0;
                weiter.setEnabled(true);
                jta.setText("");

            }
        } else if (e.getSource() == weiter) {

            if (stepCounter % 2 == 0) {
                jta.append("--------------------------------------------------------\n");
                if (kmpAlgo.kmpSchritt()) {
                    stepCounter++;
                }
            } else {

                verschiebeMuster();
            }

            scroll.getViewport().setViewPosition(new Point(0, (int) jta.getSize().getHeight()));
            stepCounter++;

        }

    }

}

