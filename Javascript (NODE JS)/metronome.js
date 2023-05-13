const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

testcases = 0
rl.on('line', (line) => {
    console.log(parseInt(line)/4)
});
