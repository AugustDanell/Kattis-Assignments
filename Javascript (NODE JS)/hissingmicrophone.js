const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

testcases = 0
rl.on('line', (line) => {
    found = false
    for(i = 0; i < line.length-1; i++){
        if(line[i] == "s" && line[i+1] == "s"){
            found = true
            break
        }
    }
    if(found){
        console.log("hiss")
    }
    else{
        console.log("no hiss")
    }
});
