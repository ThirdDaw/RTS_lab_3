import java.lang.Math;


public class Main {
    public static void main(String[] args) throws Exception {
        int[] result = factorization(33);
        System.out.println(result[0]);
        System.out.println(result[1]);
    }

    private static int[] factorization(int number) throws Exception {
        int x = (int) (Math.sqrt(number));
        if (number % 2 == 0 && isPrime((int) number / 2)) {
            return new int[]{2, (int) number / 2};
        }
        while (!isPerfectSquare(x * x - number)) {
            x += 1;
            if (x > number / 2) {
                throw new Exception();
            }
        }
        int y = (int) Math.sqrt((x * x - number));
        int a = x - y;
        int b = x + y;
        if (a == b || !isPrime(a) || !isPrime(b)) {
            throw new Exception();
        }
        return new int[]{a, b};
    }

    private static boolean isPerfectSquare(int number) {
        return Math.pow(Math.round(Math.sqrt(number)), 2) == number;
    }

    private static boolean isPrime(int number) {
        int sqrt = (int) Math.sqrt(number) + 1;
        for (int i = 2; i < sqrt; i++) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }
}
