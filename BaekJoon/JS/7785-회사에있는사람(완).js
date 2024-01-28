const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input=[];
let dataMap = {};
let result = [];
rl.on('line', line => {
    input.push(line.split(' '));
});
rl.on("close",()=>{
    for (let i = 1; i <= Number(input[0]); i++) {
        dataMap[input[i][0]] = input[i][1];     // 마지막에 입력된 enter/leave 가 dataMap에 입력
    }
    for (let key of Object.keys(dataMap)) {
        if (dataMap[key] !== 'leave') result.push(key);
    }
    result.sort().reverse();
    console.log(result.join('\n'));
})