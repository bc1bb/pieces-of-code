import java.util.Random;
import java.util.Scanner;

public class Exercice3 {
    public static void main(String[] args) {
        long start = System.nanoTime();
        Random random = new Random();
        int userGuess = -1;
        String buffer;
        Scanner sc;

        int randomInt = random.nextInt(0, 1000);

        while(userGuess != randomInt) {
            System.out.print("Devinez le nombre: ");
            sc = new Scanner(System.in);
            buffer = sc.nextLine();
            userGuess = Integer.parseInt(buffer);

            if (userGuess > randomInt) {
                System.out.println("C'est moins!");
            } else if (userGuess < randomInt) {
                System.out.println("C'est plus!");
            }
        }

        long end = System.nanoTime();
        long time = end - start;

        System.out.println("Bravo, le nombre était bien " + randomInt + ", il vous a fallu " + formatTime(time));
    }

    public static String formatTime(long time) {
        long seconds = time / 1000000000;

        if (seconds > 60) {
            int minutes = (int) (seconds / 60);
            long reste = seconds - (minutes * 60L);

            if (minutes == 1) {
                return minutes + " min et " + reste + " secs";
            } else {
                return minutes + " mins et " + reste + " secs";
            }
        } else {
            return seconds + " secs";
        }
    }
}