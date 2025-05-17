public class Burbuja {
        public static void main(String[] args) {
        int[] numeros = {5, 2, 9, 1, 3,10,100,30,22,4,5,67,323,45,500,432};
        int[] ordenados = Burbuja(numeros);

        for (int num : ordenados) {
            System.out.print(num + " ");   
        }
    }

    public static int[] Burbuja(int[] Lista) {
        for (int i = 0; i < Lista.length - 1; i++) {
            for (int j = 0; j < Lista.length - 1 - i; j++) {
                if (Lista[j] > Lista[j + 1]) {
                    int aux = Lista[j];
                    Lista[j] = Lista[j + 1];
                    Lista[j + 1] = aux;
                }
            }
        }
        return Lista;
    }
}

//Costo computacional n^2