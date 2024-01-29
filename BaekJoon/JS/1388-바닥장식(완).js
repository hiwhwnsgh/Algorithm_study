/*
형택이는 건축가이다. 지금 막 형택이는 형택이의 남자 친구 기훈이의 집을 막 완성시켰다.
형택이는 기훈이 방의 바닥 장식을 디자인했고, 
이제 몇 개의 나무 판자가 필요한지 궁금해졌다. 나무 판자는 크기 1의 너비를 가졌고, 양수의 길이를 가지고 있다. 
기훈이 방은 직사각형 모양이고, 방 안에는 벽과 평행한 모양의 정사각형으로 나누어져 있다.
이제 ‘-’와 ‘|’로 이루어진 바닥 장식 모양이 주어진다. 
만약 두 개의 ‘-’가 인접해 있고, 같은 행에 있다면, 두 개는 같은 나무 판자이고, 
두 개의 ‘|’가 인접해 있고, 같은 열에 있다면, 두 개는 같은 나무 판자이다.

input
6 9
-||--||--
--||--||-
|--||--||
||--||--|
-||--||--
--||--||-

output
31
*/
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
// 행에 대한 재귀함수
const rowRecusion = (strArray,array,i,j,count) =>{
    if(j>=array[i].length || strArray[i][j] === '|') return;
    array[i][j] = count;
    if(j+1>=array[i].length) return;
    if(array[i][j+1] === 0){
        rowRecusion(strArray,array,i,j+1,count);
    } else return;
}
// 열에 대한 재귀함수
const columnRecusion = (strArray,array,i,j,count) => {
    if(i>=array.length || strArray[i][j] === '-') return;
    array[i][j] = count;
    if(i+1>=array.length) return;
    if(array[i+1][j] === 0){
        columnRecusion(strArray,array,i+1,j,count);
    }
}
let input = []
rl.on('line',line=>{
    input.push(line);
})
rl.on('close',()=>{
    let [width,height] = input[0].split(' ').map(v=> parseInt(v)); // 첫 줄 가로,세로 길이 추출
    let array = Array.from({length : width}, ()=> Array(height).fill(0));   // 0으로 채워진 width,height 2차원 배열 초기화
    let strArray = input.slice(1);  // 첫 줄 삭제
    strArray = strArray.map(row=>row.split('')); // 판자(문자열)를(을) 2차원배열 초기화
    let count = 1;
    for(let i=0;i<array.length;i++){
        for(let j=0;j<array[0].length;j++){
            if(array[i][j]===0){
                if(strArray[i][j] === '-'){
                    rowRecusion(strArray,array,i,j,count);
                }
                else if(strArray[i][j] === '|'){
                    columnRecusion(strArray,array,i,j,count);
                }
                count +=1;
            }
        }
    }
    console.log(count-1);
})