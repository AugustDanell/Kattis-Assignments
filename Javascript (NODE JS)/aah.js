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

jm = ""
rl.on('line', (line) => {
    if(jm == ""){
        jm = line
    }
    else{
        if(jm.length >= line.length){
            console.log("go")
        }
        else{
            console.log("no")
        }
    }
});
