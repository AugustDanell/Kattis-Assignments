const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

testcases = 0
rl.on('line', (line) => {
    splitted = line.split(" ")
    a = parseInt(splitted[0])
    b = parseInt(splitted[1])
    if(a >= b){
        console.log(b, a)
    }
    else{
        console.log(a, b)
    }
});
