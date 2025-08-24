import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.StringTokenizer
import java.lang.StringBuilder

private class FastScanner {
    private val br = BufferedReader(InputStreamReader(System.`in`))
    private var st: StringTokenizer? = null
    fun next(): String {
        while (st == null || !st!!.hasMoreTokens()) st = StringTokenizer(br.readLine())
        return st!!.nextToken()
    }
    fun nextInt() = next().toInt()
    fun nextLong() = next().toLong()
    fun nextLine(): String = br.readLine()
}

fun main() {
    val fs = FastScanner()
    val out = StringBuilder()

    // 예: 정수 N개 합
    val n = fs.nextInt()
    if (n == 1){
        print(fs.next())
        return
    }
    val arr = Array(n) { fs.next() }
    // 기준 문자열을 StringBuilder로 (문자 교체가 쉬움)
    val sb = StringBuilder(arr[0])
    for ( i in 1 until n){
        val cur = arr[i]
        for (j in 0 until sb.length){
            if (cur[j] != sb[j]){
                sb.setCharAt(j,'?')
            }
        }
    }
    print(sb)
}
