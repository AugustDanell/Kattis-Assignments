const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', (line) => {
    var echo = line
    var response = echo
    
    for (let i = 0; i < 2; i++){
        response += " " + echo
    }
    
    console.log(response)
});
