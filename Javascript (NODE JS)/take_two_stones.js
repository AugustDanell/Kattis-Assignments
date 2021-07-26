const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', (line) => {
    var nums = line.split(' ');
    var a = parseInt(nums[0]);
    
    
    
    if(a % 2 == 1){
        console.log('Alice')
    }
    else{
        console.log('Bob')
    }
    
});
