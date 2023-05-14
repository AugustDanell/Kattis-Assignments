const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

x = 0
y = 0
rl.on('line', (line) => {
    if (x == 0){
        x = parseInt(line)
    }
    else{
        y = parseInt(line)
    }
    
    if(x > 0 && y > 0){
        console.log(1)
    }
    else if(x > 0 && y < 0 ){
        console.log(4)
    }
    else if(x < 0 && y > 0){
        console.log(2)
    }
    else if(y != 0){
        console.log(3)
    }
    //console.log("test", x, y)
});
