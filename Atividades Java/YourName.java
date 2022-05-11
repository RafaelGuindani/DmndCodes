import java.util.Scanner;

public class YourName {
    public static void main(String[] args) {
        String seunome = "";
        Scanner digitarnome = new Scanner(System.in);

        System.out.println("Por gentileza, Informe seu nome:\n>: ");
        seunome = digitarnome.nextLine();
        System.out.println("Olá "+seunome);/*Inserir nome*/
        Scanner sc = new Scanner(System.in);
        System.out.println("Informe por gentileza o ano que nasceu\n>:");/*Inserir idade*/
        int a = sc.nextInt();
        int b = 2022;
        int year = b - a;
        System.out.println("Você tem "+ year + " Anos");

    }}
