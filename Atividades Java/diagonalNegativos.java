import java.util.Locale;
import java.util.Scanner;

public class diagonalNegativos {
    public static void main (String[] args) {
        //***
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        //***
        int N, cont;
        System.out.print("Qual a ordem da MATRIZ ? ");
        N = sc.nextInt();
        int [][] mtz = new int[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++){
                System.out.print("Elemento [" + i + "," + j + "]: ");
                mtz[i][j] = sc.nextInt();
            }
        }
        System.out.println("DIAGONAL PRINCIPAL: ");
        for (int i = 0; i < N; i++) {
            System.out.print(mtz[i][i] + " ");
        }
        System.out.println("");
        cont = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++){
                if (mtz[i][j] < 0) {
                    cont++;
                }
            }
        }
        System.out.println("QUANTIDADE DE NEGATIVOS = " + cont);
        sc.close();
    }
}
