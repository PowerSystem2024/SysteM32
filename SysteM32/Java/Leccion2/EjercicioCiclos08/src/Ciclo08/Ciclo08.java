/*
Ejercicio 8: Pedir un numero N, y mostrar todos los numeros del 1 al N.
*/
package Ciclo08;

import java.util.Scanner;


public class Ciclo08 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner (System.in);
        System.out.println("Digite un numero: ");
        int numero = Integer.parseInt(entrada.nextLine());
        int i =1;
        while( i <= numero){
            System.out.println(i);
            i++;
        }
    }
}
