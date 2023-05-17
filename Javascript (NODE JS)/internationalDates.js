const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});


rl.on('line', (line) => {
    split = line.split("/")
    date = []
    for(i = 0; i < split.length; i++){
        date.push(parseInt(split[i]))
    }
    if(date[0] > 12){
        console.log("EU")
    }
    else if(date[1] > 12){
        console.log("US")
    }
    else{
        console.log("either")
    }
});
