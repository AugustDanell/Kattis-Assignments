const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', (line) => {
    var undead = false
    var alive = false
    for(var i = 0; i < line.length-1; i++){
        if(line[i] == ":"){
            if (line[i+1] == ")"){
                alive = true
            }
            else if(line[i+1] == "("){
                undead = true
            }
        }
    }
    
    if(alive && !undead){
        console.log("alive")
    }
    else if(!alive && undead){
        console.log("undead")
    }
    else if(!alive && !undead){
        console.log("machine")
    }
    else{
        console.log("double agent")
    }
});
