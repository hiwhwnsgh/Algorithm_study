import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    static ArrayList<Integer>[] A;
    static int  M[];
    static boolean visited[];
    static int N;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        N = Integer.parseInt(br.readLine());
        A = new ArrayList[N+1];
        M = new int[N+1];
        visited = new boolean[N+1];
        for(int i = 1; i <= N; i++){
            A[i] = new ArrayList<Integer>();
        }

        for(int i=0;i<N-1;i++){
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            A[s].add(e);
            A[e].add(s);
        }
        DFS(1,1);
        for(int i = 2; i <= N; i++){
            System.out.println(M[i]);
        }
    }
    public static void DFS(int v, int parents){
        if(visited[v]){
            return;
        }
        visited[v] = true;
        M[v] = parents;
        for(int i : A[v]){
            if(!visited[i]){
                DFS(i,v);
            }
        }

    }
}
