const friends = [
    ["muzi", "ryan", "frodo", "neo"],
    ["joy", "brad", "alessandro", "conan", "david"],
    ["a", "b", "c"]
]
const gifts = [
    ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"],
    ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"],
    ["a b", "b a", "c a", "a c", "a c", "c a"]
]

var names = {};
const idx = 0
for (let i = 0; i < friends[idx].length; i++) {
    const name = friends[idx][i];
    names[name] = {};
    for (let j = 0; j < friends[idx].length; j++) {
      const innerName = friends[idx][j];
      if (i !== j) {
        names[name][innerName] = 0;
      }
    }
}

for(i=0;i<gifts[idx].length;i++){
    const value = gifts[idx][i].split(' ');
    names[value[0]][value[1]] += 1   
}
console.log(names['muzi']['ryan'])
