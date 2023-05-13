const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', (line) => {
    upper = 0
    lower = 0
    whites = 0
    symbols = 0
    
    for(i = 0; i < line.length; i++){
        if(line[i] == "_"){
            whites ++;
        }
        else if(line.charCodeAt(i) >= 123){
            symbols ++;
        }
        else if(line.charCodeAt(i) >= 97){
            lower ++;
        }
        else if(line.charCodeAt(i) >= 91){
            symbols ++;
        }
        else if(line.charCodeAt(i) >= 65){
            upper ++;
        }
        else{
            symbols ++;
        }
    }
    total = line.length
    console.log(whites  / total)
    console.log(lower   / total)
    console.log(upper   / total)
    console.log(symbols / total)
});
