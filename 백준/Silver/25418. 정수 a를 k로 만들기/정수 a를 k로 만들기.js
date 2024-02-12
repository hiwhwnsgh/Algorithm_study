function minOperationsToK(A, K) {
  let count = 0;
  
  while (true) {
      // K가 홀수이면 1을 빼고, 짝수이면 2로 나눈다
      if(K===A){
        console.log(count)
        break
      }
      if(K % 2 === 0 && K>=A*2){
        K /= 2
      }
      else{
        K -=1
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
    // let queue = [[A,0]];
    // let visited = new Set([A]);
    // while(queue.length > 0){
    //     const [current,count] = queue.shift();
    //     if(current==K){
    //       console.log(count);
    //       break;
    //     }
    //     // 현재 값이 K보다 크면, 더 이상 더블링하지 않고 바로 다음 단계로 넘어감
    //     if (current < K && !visited.has(current * 2)) {
    //       queue.push([current * 2, count + 1]);
    //       visited.add(current * 2);
    //     }

    //     if (!visited.has(current + 1)) {
    //         queue.push([current + 1, count + 1]);
    //         visited.add(current + 1);
    //     }
        
    // }
    minOperationsToK(A,K)
});
