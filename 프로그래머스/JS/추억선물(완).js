function solution(name, yearning, photo) {
    var answer = [];
    let dataMap = {};
    for(i=0;i<name.length;i++){
        dataMap[name[i]] = yearning[i]
    }
    for(i=0;i<photo.length;i++){
        let result = 0;
        for(j=0;j<photo[i].length;j++){
            if(photo[i][j] in dataMap){
                result += dataMap[photo[i][j]];
            }
        }
        answer.push(result);
    }
    return answer;
}