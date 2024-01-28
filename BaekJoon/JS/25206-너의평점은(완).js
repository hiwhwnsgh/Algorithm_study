/*
인하대학교 컴퓨터공학과를 졸업하기 위해서는, 전공평점이 3.3 이상이거나 졸업고사를 통과해야 한다. 
그런데 아뿔싸, 치훈이는 깜빡하고 졸업고사를 응시하지 않았다는 사실을 깨달았다!
치훈이의 전공평점을 계산해주는 프로그램을 작성해보자.
전공평점은 전공과목별 (학점 × 과목평점)의 합을 학점의 총합으로 나눈 값이다.
*/

const readline = require('readline');
const rl = readline.createInterface({
    input : process.stdin,
    output : process.stdout,
})
const grades = {
    "A+" : 4.5,
    "A0" : 4.0,
    "B+" : 3.5,
    "B0" : 3.0,
    "C+" : 2.5,
    "C0" : 2.0,
    "D+" : 1.5,
    "D0" : 1.0,
    "F" : 0.0,
    "P" : 0.0,
}
let input=[]
let result = 0;
let total = 0;
rl.on("line",line=>{
    input.push(line.split(' '))
})
rl.on("close",()=>{
    for(i=0;i<input.length;i++){
        const [subject, score, grade] = input[i];
        if(grade === 'P') continue;
        const num = Number(score) * grades[grade];
        result += num;
        total += Number(score);
    }
    console.log((result / total).toFixed(6));
})
