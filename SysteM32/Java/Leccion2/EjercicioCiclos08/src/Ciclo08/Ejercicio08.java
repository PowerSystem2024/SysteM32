package Ciclo08;

import javax.swing.JOptionPane;

public class Ejercicio08 {
    public static void main(String[] args) {
        
        String input = JOptionPane.showInputDialog("Digite un número:");
        
        int numero = Integer.parseInt(input);
        
        int i = 1;
        StringBuilder resultado = new StringBuilder();
        
        
        while(i <= numero) {
            resultado.append(i).append("\n");
            i++;
        }
        
        JOptionPane.showMessageDialog(null, resultado.toString());
    }
}

