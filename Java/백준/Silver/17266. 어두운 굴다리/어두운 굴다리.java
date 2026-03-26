import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    static int n, m;
    static int[] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());

        arr = new int[m];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0; i < m; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int left = 0, right = n;
        int answer = n;

        while(left <= right) {
            int mid = (left + right) / 2;

            if(lightCheck(mid)) {
                answer = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        System.out.println(answer);
    }
    static boolean lightCheck(int mid) {
        int prev = 0;
        for (int j : arr) {
            if (j - mid <= prev) {
                prev = j + mid;
            } else {
                return false;
            }
        }
        return prev >= n;
    }
}