const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', (line) => {
    var nums = line.split(' ');
    var x = parseInt(nums[0]);
    var y = parseInt(nums[1]);
    var n = parseInt(nums[2]);
    
    for (let i = 1; i <= n; i++){
        if(i % x === 0 && i % y === 0){
            console.log('Fizzbuzz')
        }
        else if(i % x === 0){
            console.log('Fizz')
        }
        else if(i % y === 0){
            console.log('Buzz')
        }
        else{
            console.log(i)
        }
    }
    
});
