import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.StringTokenizer
import java.io.PrintWriter
import java.util.HashMap

private class FastReader {
    private val br = BufferedReader(InputStreamReader(System.`in`))
    private var st: StringTokenizer? = null

    fun next(): String {
        while (st == null || !st!!.hasMoreElements()) {
            val line = br.readLine() ?: return ""
            st = StringTokenizer(line)
        }
        return st!!.nextToken()
    }
    fun nextInt(): Int = next().toInt()
    fun nextLong(): Long = next().toLong()
    fun nextDouble(): Double = next().toDouble()

    fun nextLine(): String = br.readLine() ?: ""
    fun intArray(n: Int): IntArray = IntArray(n) { nextInt() }
    fun longArray(n: Int): LongArray = LongArray(n) { nextLong() }
}

fun main() {
    val fr = FastReader()
    val out = PrintWriter(System.out)

    // 예시: N, M 읽고 합/출력

    val hashMap = HashMap<Int,Boolean>()
    for ( i in 1..30){
        hashMap[i] = false
    }
    for(i in 0 until 28){
        val n = fr.nextInt()
        hashMap[n] = true
    }
    for (i in 1..30){
        if (hashMap[i] == false){
            println(i)
        }
    }

    out.flush()
}
