const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', (line) => {
    var nums = line.split(' ');
    var greeting = nums[0];
    counter = (greeting.length-2)*2
    response = "h"
    for (let i = 0; i < counter; i++){
        response += "e"
    }
    response += "y"
    
    console.log(response)
});
