import java.util.Scanner;

public class YourName {
    public static void main(String[] args) {
        String seunome = "";
        Scanner digitarnome = new Scanner(System.in);

        System.out.println("Por gentileza, Informe seu nome:\n>: ");
        seunome = digitarnome.nextLine();
        System.out.println("Olá "+seunome);
    }}
