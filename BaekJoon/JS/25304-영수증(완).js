const readline = require('readline');
const rl = readline.createInterface({
    input : process.stdin,
    output : process.stdout,
})
let input = []
rl.on('line',(line)=>{
    input.push(line.split(' ').map(v=>parseInt(v)));
})
rl.on('close',()=>{
    let array = input.slice(2,input[1]+2)
    let sum = 0;
    for(i=0;i<array.length;i++){
        sum += array[i][0] * array[i][1];
        if(sum>input[0]){
            console.log("No");
            return;
        }
    }
    sum === parseInt(input[0]) ? console.log("Yes") : console.log("No");
})