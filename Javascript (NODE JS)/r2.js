const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rows = 0
sum = 0
counter = -1
rl.on('line', (line) => {
    split = line.split(" ")
    R_1 = parseInt(split[0])
    s = parseInt(split[1])
    R_2 = 2*s - R_1
    console.log(R_2)
});
