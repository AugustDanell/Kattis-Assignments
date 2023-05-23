const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

cases = 0
rl.on('line', (line) => {
    if (cases == 0){
        cases = parseInt(line)
    }
    else{
        x = parseInt(line)
        if (x%2 == 0){
            console.log(`${x} is even`)
        }
        else{
            console.log(`${x} is odd`)
        }
    }
});
