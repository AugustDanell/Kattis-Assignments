function maximal(S, s1, s2, s3, s4){
    return Math.sqrt((S-s1) * (S-s2) * (S-s3) * (S-s4))
}


const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

cases = 0
rl.on('line', (line) => {
    split = line.split(" ")
    a = parseInt(split[0])
    b = parseInt(split[1])
    c = parseInt(split[2])
    d = parseInt(split[3])
    console.log(maximal((a+b+c+d)/2, a, b,c,d))
});
