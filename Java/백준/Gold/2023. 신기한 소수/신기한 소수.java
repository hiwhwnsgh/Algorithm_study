import java.util.Scanner;

public class Main {
    static int N;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();

        DFS(1,2);
        DFS(1,3);
        DFS(1,5);
        DFS(1,7);
    }
    public static void DFS(int depth, int num){
        if(depth == N){
            System.out.println(num);
            return;
        }
        for(int i=1; i<=9; i++){
            if( i % 2 == 0) continue; // 짝수는 소수가 될 수 없음
            int newNum = num * 10 + i;
            if(isPrime(newNum)) {
                DFS(depth + 1, newNum);
            }
        }
    }
    public static boolean isPrime(int num){
        if(num < 2) return false;
        for(int i=2; i<=Math.sqrt(num); i++){
            if(num % i == 0) return false;
        }
        return true;
    }
}
