const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

testcases = 0
rl.on('line', (line) => {
    if(testcases == 0){
        testcases = parseInt(line)
    }
    else{
        substrings = line.split(" ")
        substrings.shift()
        size = substrings.length
        sum = substrings.map(Number).reduce((acc, curr) => acc + curr, 0);
        console.log(sum - (size-1))
    }
});
