import java.util.Locale;
import java.util.Scanner;

public class menordeTRES {
    public static void main(String[] args){
        //***
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        //***
        int a, b, c, menor;
        System.out.print("Primeiro VALOR: ");
        a = sc.nextInt();
        System.out.print("Segundo VALOR: ");
        b = sc.nextInt();
        System.out.print("Terceiro VALOR: ");
        c = sc.nextInt();
        //***
        if (a < b && a < c){
            menor = a;
        }
        else if (b < c) {
            menor = b;
        }
        else {
            menor = c;
        }
        //***
        System.out.println("MENOR = " + menor);
    }
}
