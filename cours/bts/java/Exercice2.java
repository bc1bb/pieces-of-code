import java.util.Arrays;
import java.util.Random;

public class Exercice2 {
    public static void main(String[] args) {
        Random random = new Random();
        int[] randomArray;
        int passes = 0;

        do {
            passes++;
            int a = random.nextInt(0, 1000);
            int b = random.nextInt(0, 1000);
            int c = random.nextInt(0, 1000);

            randomArray = new int[]{a, b, c};
        } while (! checkArray(randomArray));

        System.out.println("Le tableau retenu est : " + Arrays.toString(randomArray) + ".\nIl a fallu " + passes + " essais pour trouver ce tableau.");
    }

    static boolean checkArray(int[] intArray) {
        if (intArray[0] % 2 == 0) {
            if (intArray[1] % 2 == 0) {
                if (intArray[2] % 2 != 0) {
                    return true;
                }
            }
        }

        return false;
    }
}