const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', (line) => {
    c = 0
    for(i = 0; i < line.length; i++){
        c+= line.charCodeAt(i)
    }
    console.log(String.fromCharCode(Math.floor(c/line.length)))
});
