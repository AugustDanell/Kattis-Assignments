const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', (line) => {
    split = line.split(" ")
    if((split[0] == "OCT" && split[1] == "31") || split[0] == "DEC" && split[1] == "25"){
        console.log("yup")
    }
    else{
        console.log("nope")
    }
});
