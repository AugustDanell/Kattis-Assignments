const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

testcases = 0
rl.on('line', (line) => {
    split = line.split(" ")
    kings =   (1 - parseInt(split[0]))
    queens =  (1 - parseInt(split[1]))
    rooks =   (2 - parseInt(split[2]))
    bishops = (2 - parseInt(split[3]))
    knights = (2 - parseInt(split[4]))
    pawns =   (8 - parseInt(split[5]))
    console.log(kings, queens, rooks, bishops, knights, pawns)
});
