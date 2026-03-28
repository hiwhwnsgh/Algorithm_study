import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        PriorityQueue<Integer> qp = new PriorityQueue<>();
        for(int i=0;i<N;i++){
            int data = sc.nextInt();
            qp.add(data);
        }
        int sum = 0;
        while(qp.size() != 1){
            int data1 = qp.remove();
            int data2 = qp.remove();
            sum += data1 + data2;
            qp.add(data1 + data2);
        }
        System.out.println(sum);

    }
}
