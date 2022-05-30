public class Mensagem_ {
    public static void obtermensagem(int hora) {

        switch (hora) {
            case 5:
            case 6:
            case 7:
            case 8:
            case 9:
            case 10:
            case 11:
            case 12:
                mensagembomdia();
                break;
            case 13:
            case 14:
            case 15:
            case 16:
            case 17:
                mensagemboatarde();
                break;
            case 18:
            case 19:
            case 20:
            case 21:
            case 22:
            case 23:
            case 0:
            case 1:
            case 2:
            case 3:
            case 4:
                mensagemboanoite();
                break;
            default:
                System.out.println("Hora inválida.");
        }
    }
    public static void mensagembomdia(){
        System.out.println("Bom Dia!");
    }
    public static void mensagemboatarde(){
        System.out.println("Boa Tarde!");
    }
    public static void mensagemboanoite(){
        System.out.println("Boa Noite!");
    }
}
