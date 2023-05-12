const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

N = 0
carrots = 0
rl.on('line', (line) => {
    if(carrots == 0){
        split = line.split(" ")
        N = parseInt(split[0])
        carrots = parseInt(split[1])
    }
    else{
        N --;
    }
    
    if(N == 0){
        console.log(carrots)
    }
});
