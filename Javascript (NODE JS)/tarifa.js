const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

megabytes = -1
size = -1
s = 0
rl.on('line', (line) => {
    if (megabytes == -1){
        megabytes = parseInt(line)
    }
    else if(size == -1){
        size = parseInt(line)
    }
    else{
        subtraction = parseInt(line)
        s += megabytes - subtraction
        size --
    }
    
    if(size == 0){
        console.log(megabytes + s)
    }
});
