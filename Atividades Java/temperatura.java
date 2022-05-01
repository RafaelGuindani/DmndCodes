/* Escreva um programa que, com base em uma temperatura em graus celsius, 
converta e exiba em Kelvin (K), Réaumur (Re), Rankine (Ra) e Fahrenheit (F),
seguindo as fórmulas: F = C * 1.8 + 32;
K = C + 273.15;
Re = C * 0.8;
Ra = C * 1.8 + 32 + 459.67 */

public class temperatura {
    public static void main(String[] args) {
        double C, K, Re, Ra, F;
        C = 21; /*celsius*/

        F = C * 1.8 + 32;  /*Fahrenheit*/       
        K = C + 273.15;  /*Kelvin*/
        Re = C * 0.8;  /*Réaumur*/
        Ra = C * 1.8 + 32 + 459.67;  /*Rankine*/

        System.out.println("A temperatura em Fahrenheit é:" + F);
        System.out.println("A temperatura em Kelvin é:" + K);
        System.out.println("A temperatura em Réaumur é:" + Re);
        System.out.println("A temperatura em Rankine é:" + Ra);

    }}