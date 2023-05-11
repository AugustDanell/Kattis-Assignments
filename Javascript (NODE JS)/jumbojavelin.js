const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rows = 0
sum = 0
counter = -1
rl.on('line', (line) => {
    if(counter == -1){
        counter = parseInt(line)
        rows = counter
    }
    else{
        sum += parseInt(line)
        counter --;
    }

    if (counter == 0){
        res = sum - (rows-1)
        console.log(res)
    }
});
