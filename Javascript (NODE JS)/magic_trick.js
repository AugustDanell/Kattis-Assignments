const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', (line) => {
    map = [];
    dup = false;
    for (let i = 0; i < line.length; i++){
        token = line.charAt(i);
        if(map.includes(token)){
            dup = true;
        }
        else{
            map.push(token);
        }
    }
    
    if(dup){
        console.log(0);
    }
    else{
        console.log(1);
    }
});
