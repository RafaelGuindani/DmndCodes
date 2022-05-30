public class Main {

    public static void main(String[] args) {
        // CALCULADORA ***
        System.out.println("\nExercicio Calculadora\n");
        Calculadora.soma(3,6);
        Calculadora.subtracao(9, 1.8);
        Calculadora.multiplicacao(7,8);
        Calculadora.divisao(5,2.5);
        // MENSAGEM ***
        System.out.println("\nExercício mensagem\n");
        Mensagem_.obtermensagem(9);
        Mensagem_.obtermensagem(14);
        Mensagem_.obtermensagem(1);
        // EMPRESTIMO ***
        System.out.println("\nExercicio de Empréstimo\n");
        Emprestimo.calcular(1000, Emprestimo.getDuasParcelas());
        Emprestimo.calcular(1000, Emprestimo.getTresParcelas());
        Emprestimo.calcular(1000,5);
    }
}
