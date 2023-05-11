const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
counter =  0
rl.on('line', (line) => {
    for(i = 0; i < line.length; i++){
        if (vowels.includes(line[i])){
            counter ++
        }
    }
    console.log(counter)
});
