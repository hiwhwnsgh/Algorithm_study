function solution(players, callings) {
    var answer = [];
    for(i=0;i<callings.length;i++){
        for(j=0;j<players.length;j++){
            if(players[j]===callings[i]){
                var temp = players[j-1];
                players[j-1] = players[j];
                players[j] = temp
                
            }
        }
    }
    //console.log(players)
    return answer;
}

solution(["mumu", "soe", "poe", "kai", "mine"],["mumu", "soe", "poe", "kai", "mine"])