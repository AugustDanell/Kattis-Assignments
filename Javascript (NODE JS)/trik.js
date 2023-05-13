const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
cups = [1, 0, 0]
rl.on('line', (line) => {
    for(i = 0; i < line.length; i++){
        if(line[i] == "A"){
            temp = cups[0]
            cups[0] = cups[1]
            cups[1] = temp
        }
        else if(line[i] == "B"){
            temp = cups[1]
            cups[1] = cups[2]
            cups[2] = temp
        }
        else{
            temp = cups[0]
            cups[0] = cups[2]
            cups[2] = temp
        }
    }
    
    for(i = 0; i < cups.length; i++){
        if(cups[i] == 1){
            console.log(i+1)
            break
        }
    }
});
