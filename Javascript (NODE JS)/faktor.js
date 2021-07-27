const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', (line) => {
    var nums = line.split(' ');
    var a = parseInt(nums[0]);
    var b = parseInt(nums[1]);
    
    
    console.log((a)*(b-1)+1)
    
});
