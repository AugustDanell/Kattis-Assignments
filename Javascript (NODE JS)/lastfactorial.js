function fac(x){
    if(x == 1 || x == 0){
        return 1
    }
    return fac(x-1)*x
}

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

N = 0
carrots = 0
rl.on('line', (line) => {
    if(N == 0){
        N = parseInt(line)
    }
    else{
        x = parseInt(line)
        console.log(fac(x)%10)
    }
});
