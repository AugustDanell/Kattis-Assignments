const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

testcases = 0
rl.on('line', (line) => {
    split = line.split(" ")
    if(parseInt(split[0]) + parseInt(split[1]) == parseInt(split[2])){
        console.log("correct!")
    }
    else{
        console.log("wrong!")
    }
});
