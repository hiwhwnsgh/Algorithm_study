const readline = require('readline');
const rl = readline.createInterface({
    input : process.stdin,
    output : process.stdout,
})

let input = [];

rl.on('line',line=>{
    input.push(line.split(' '));
})
rl.on("close",()=>{
    console.log(input[1].includes(input[2]));
})
