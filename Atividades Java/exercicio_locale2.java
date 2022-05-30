import java.util.Locale;

public class exercicio_locale2 {
    public static void main(String[] args){
        Locale.setDefault(Locale.US);
        //***
        int idade;
        double salario;
        String nome;
        char sexo;
        //***
        idade = 32;
        salario = 4560.9;
        nome = "Rafael Guindani";
        sexo = 'M';
        //***
        System.out.println("O Funcionário " + nome + ", sexo " + sexo + ", ganha " +
                String.format("%.2f", salario) + " e tem " + idade + " anos.");
    }
}
