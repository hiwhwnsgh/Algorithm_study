const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', line => {
    input.push(Number(line));
});

rl.on('close', () => {
    let result = [];
    for(i=1;i<=input[0];i++){
        let num = input[i];
        let array = []
        let share
        if(num>=25){
            share = parseInt(num / 25);
            array.push(share);
            num -= 25 * share;
        }
        else{
            array.push(0);
        }
        if(num >= 10){
            share = parseInt(num / 10);
            array.push(share); 
            num -= 10 * share;
        }
        else{
            array.push(0);
        }
        if(num>=5){
            share = parseInt(num / 5);
            array.push(share); 
            num -= 5 * share;
        }
        else{
            array.push(0);
        }
        array.push(num);
        result.push(array);
    }
    result.forEach(el=>{
        console.log(`${el[0]} ${el[1]} ${el[2]} ${el[3]}`);
    })
});
