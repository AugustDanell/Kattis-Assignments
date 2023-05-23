const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

cases = 0
rl.on('line', (line) => {
    if(cases == 0){
        cases = parseInt(line)
    }
    else{
        split = line.split(" ")
        if(split.length > 1 && split[0] == "Simon" && split[1] == "says"){
            split.shift()
            split.shift()
            console.log(split.join(" "))
        }
    }
  
});
