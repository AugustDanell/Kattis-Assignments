import java.util.Scanner;
class digitswap {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        System.out.print(a%10);
        System.out.print((int)a/10);
    }
}
