function minOperationsToK(A, K) {
  let count = 0;
  
  while (true) {
    if(K === A) {
      // A와 K가 같아지면 반복을 종료하고 현재까지의 연산 횟수를 반환한다.
      return count;
    }
    if(K % 2 === 0 && K >= A * 2) {
      K /= 2;
    } else {
      K -= 1;
    }
    count++;
  }
}
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let input = [];

rl.on("line", (line) => {
  input = line.split(" ").map(Number);
});

rl.on("close", () => {
    const A = input[0];
    const K = input[1];
    console.log(minOperationsToK(A, K)); // 출력: 151 또는 문제에 따라 다른 최소 연산 횟수
});
