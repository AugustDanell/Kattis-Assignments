const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rows = 0
sum = 0
counter = -1
rl.on('line', (line) => {
    flag = true
    l = []
    for(i = 0; i < line.length; i++){
        if(line[i] == "-"){
            flag = true
        }
        else if(flag){
            l.push(line[i])
            flag = false
        }
    }
    console.log(l.join(""))
});
