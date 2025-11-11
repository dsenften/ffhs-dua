package ch.ffhs.dua.pva5.kmp;

import javax.swing.*;
import javax.swing.table.DefaultTableCellRenderer;
import java.awt.*;

class MyTableCellRenderer extends DefaultTableCellRenderer {

    private final KMPAlgorithm kmpAlgo;

    public MyTableCellRenderer(KMPAlgorithm kmpAlgo) {
        this.kmpAlgo = kmpAlgo;
        setHorizontalAlignment(SwingConstants.CENTER);
    }

    public Component getTableCellRendererComponent(JTable table, Object value, boolean isSelected, boolean hasFocus, int row, int column) {

        Component cell = super.getTableCellRendererComponent(table, value, isSelected, hasFocus, row, column);

        if (row == 2)
            setBackground(SystemColor.window);
        else {
            setBackground(Color.WHITE);
        }

        // current cell
        if ((row == 0 || row == 1) && column == kmpAlgo.getTableI()) {
            setBackground(Color.GREEN);
        }

        return cell;
    }
}
