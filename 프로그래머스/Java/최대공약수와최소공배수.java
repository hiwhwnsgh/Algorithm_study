public class 최대공약수와최소공배수 {
    class Solution {
        public int[] solution(int n, int m) {
            
            int GCD = findGCD(n,m);
            int LCM = findLCM(n,m);
            int[] answer = {GCD,LCM};
            return answer;
        }
        public static int findGCD(int a,int b){
            while(b!=0){
                int temp = b;
                b = a % b;
                a = temp;
            }
            return a;
        }
        public static int findLCM(int a, int b){
            return a*b/findGCD(a,b);
        }
    }
}
