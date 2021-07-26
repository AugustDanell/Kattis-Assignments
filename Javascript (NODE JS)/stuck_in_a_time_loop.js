const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', (line) => {
    var nums = line.split(' ');
    var n = parseInt(nums[0]);
    
    for (let i = 1; i <= n; i++){
            console.log(i + ' Abracadabra')
    }
    
});
