/*
Ejercicio 3: Leer numeros hasta que se introduzca un cero
Para cada uno indicar si es par o impar.
Orumero lo haremos con la clase Scanner
Luego con la clase JOptionPane
 */
package Ciclos03;

import javax.swing.*;

public class Ejercicio03 {
    public static void main(String[] args) {
        int numero;

        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero:"));
        while(numero != 0){
            if(numero % 2 == 0){
                JOptionPane.showMessageDialog(null,"El numero ingresado "+numero+" es PAR");
            }
            else{
                JOptionPane.showMessageDialog(null,"El numero ingresado "+numero+" es IMPAR");
            }
            System.out.println("Digite otro numero: ");
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero:"));
        }
        JOptionPane.showMessageDialog(null,"El numero ingresado "+numero+" finaliza el prorgama");
    }
}


