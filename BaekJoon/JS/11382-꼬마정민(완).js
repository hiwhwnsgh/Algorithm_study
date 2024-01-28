const readline = require('readline');
const rl = readline.createInterface({
    input : process.stdin,
    output : process.stdout,
})
let input = []
rl.on('line',(line)=>{
    input = line.split(' ').map(v=>parseInt(v));
})
rl.on('close',()=>{
    const result = input.reduce((acc,value)=>{
        acc+= value
        return acc;
    },0)
    console.log(result);
})