const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
counter =  0
rl.on('line', (line) => {
    if (line[0] == "5" && line[1] == "5" && line[2] == "5"){
        console.log(1)
    }
    else{
        console.log(0)
    }
});
