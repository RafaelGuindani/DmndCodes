import java.util.Locale;

public class exercicio_double_to_int {
    public static void main (String[] args){
        //***
        Locale.setDefault(Locale.US);
        //***
        double a, b;
        int c;
        a = 6.3;
        b = 5.9;
        c = (int)a * (int)b;
        //***
        System.out.println(c);
    }
}
