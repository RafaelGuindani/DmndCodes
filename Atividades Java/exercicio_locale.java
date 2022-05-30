import java.util.Locale;

public class exercicio_locale {
    public static void main (String[] args) {
        Locale.setDefault(Locale.US);
        double x;
        x = 2.3456;
        System.out.println(String.format("%.2f", x));
    }
}