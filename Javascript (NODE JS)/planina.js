const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', (line) => {
    var nums = line.split(' ');
    var a = parseInt(nums[0]);
    b = Math.pow(2,a)   
    b += 1
    c = b*b
    console.log(c)
    
});

