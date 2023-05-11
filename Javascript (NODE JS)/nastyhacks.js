const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

size = 0

rl.on('line', (line) => {
    if(size == 0){
        size = parseInt(line)
    }
    else{
        splitted_str = line.split(" ")
        rev = parseInt(splitted_str[0])
        e = parseInt(splitted_str[1])
        c = parseInt(splitted_str[2])
        ad_rev = e-c
        if(ad_rev > rev){
            console.log("advertise")
        }
        else if(ad_rev == rev){
            console.log("does not matter")
        }
        else{
            console.log("do not advertise")
        }
    }
});
