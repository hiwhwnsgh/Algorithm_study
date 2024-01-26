/*
얀에서는 매년 달리기 경주가 열립니다. 해설진들은 선수들이 자기 바로 앞의 선수를 추월할 때 추월한 선수의 이름을 부릅니다. 
예를 들어 1등부터 3등까지 "mumu", "soe", "poe" 선수들이 순서대로 달리고 있을 때, 
해설진이 "soe"선수를 불렀다면 2등인 "soe" 선수가 1등인 "mumu" 선수를 추월했다는 것입니다. 즉 "soe" 선수가 1등, "mumu" 선수가 2등으로 바뀝니다.
선수들의 이름이 1등부터 현재 등수 순서대로 담긴 문자열 배열 players와 해설진이 부른 이름을 담은 문자열 배열 callings가 매개변수로 주어질 때, 
경주가 끝났을 때 선수들의 이름을 1등부터 등수 순서대로 배열에 담아 return 하는 solution 함수를 완성해주세요.
*/
function solution(players, callings) {
    var dataMap = {};
    // 키와 값을 가진 map으로 구성 { name : idx }
    players.forEach((value,index)=>{
        dataMap[value] = index;
    })

    callings.forEach((value)=>{
        let currentPlayer = dataMap[value]; //불린 선수의 인덱스 
        let prevPlayer = dataMap[players[currentPlayer-1]]; // 불린 선수의 바로 앞 선수의 인덱스
        let temp = players[currentPlayer];  // 불린 선수의 값을 저장
        dataMap[temp] -= 1; // 불린 선수의 순위 하나 추월
        dataMap[players[prevPlayer]] +=1; // 불린 선수의 앞 선수의 순위 하나 강등
        players[currentPlayer] = players[prevPlayer];   // 불린선수의 인덱스에 강등된 선수의 값을 저장
        players[prevPlayer]= temp;  // 불린 선수의 추월한 인덱스에 값을 저장
    })
    return players;
}

const players = ["mumu", "soe", "poe", "kai", "mine"];
const callings = ["kai", "kai", "mine", "mine"]
console.log(solution(players,callings))