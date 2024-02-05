const readline = require('readline');

const rl = readline.createInterface({
    input : process.stdin,
    output : process.stdout
})

let input = []

rl.on('line', line=>{
    input.push(line.split(' ').map(Number));
})

const dfs = (v,visited,graph) => {
    //console.log(`현재 정점 : ${v}, 방문 여부 : ${visited}, 그래프 ${graph}`);
    visited[v] = true;
    const next_value = graph[v];
    if(!visited[next_value]){
        dfs(next_value,visited,graph);
    }
}

rl.on('close',()=>{
    
    const T = input.shift();
    for(i=0;i<T;i++){
        const len = input.shift();
        let graph = input.shift();
        graph.unshift(0);
        let visited = new Array(len+1).fill(false);
        let cycles = 0;
        for(j=1;j<=len;j++){
            if(!visited[j]){
                dfs(j,visited,graph)
                cycles += 1;
            }
        }
        console.log(cycles);
    }
})