import java.util.Arrays;

public class MergeSort {
        public static void main(String[] args) {
            System.out.println(".-.-.-.-.-.- MERGE --.-.-.-.-");
            int[] datos = {38, 27, 43, 3, 9, 82, 10, 19, 50, 61};
            ordenarPorMezcla(datos);
            System.out.println("Arreglo ordenado: " + Arrays.toString(datos));
        }
    
        public static void ordenarPorMezcla(int[] datos) {
            if (datos.length > 1) {
                int mitad = datos.length / 2;
                int[] izquierda = Arrays.copyOfRange(datos, 0, mitad);
                int[] derecha = Arrays.copyOfRange(datos, mitad, datos.length);
    
                System.out.println(Arrays.toString(izquierda) + " --- " + Arrays.toString(derecha));
    
                ordenarPorMezcla(izquierda);
                ordenarPorMezcla(derecha);
    
                mezclar(datos, izquierda, derecha);
            }
    
            System.out.println("Regresando de recursión: " + Arrays.toString(datos));
        }
    
        private static void mezclar(int[] datos, int[] izquierda, int[] derecha) {
            int i = 0, d = 0, k = 0;
    
            while (i < izquierda.length && d < derecha.length) {
                if (izquierda[i] < derecha[d]) {
                    datos[k++] = izquierda[i++];
                } else {
                    datos[k++] = derecha[d++];
                }
            }
    
            while (i < izquierda.length) {
                datos[k++] = izquierda[i++];
            }
    
            while (d < derecha.length) {
                datos[k++] = derecha[d++];
            }
        }
    }

    //Costo computacional O(n log n)
    