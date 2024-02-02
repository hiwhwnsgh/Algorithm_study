const readline = require('readline')
const rl = readline.createInterface({
    input : process.stdin,
    output : process.stdout
})
let input = []

rl.on('line',line=>{
    input.push(line.split(' ').map(Number));
})
rl.on('close',()=>{
    let stack = [input[1][0]];  // 시작하는 
    let start = [[0,0]];
    let arraay = input.slice(1);
    let answer = 'Hing';
    while(stack){
        const location = start.pop();
        const move = stack.pop();
        if (!location || !move){
            break;
        }
        if(move === -1){
            answer = 'HaruHaru';
            break;
        }
        if(location[0] + move < input[0]){
            stack.push(arraay[location[0] + move][location[1]]);
            start.push([location[0]+move,location[1]]);
        }
        if(location[1] + move < input[0]){

            stack.push(arraay[location[0]][location[1]+move]);
            start.push([location[0],location[1]+move]);
        }
    }
    console.log(answer);
})