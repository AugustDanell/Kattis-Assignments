const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', (line) => {
    for(i = 0; i < line.length-1; i++){
        start_smile = (line.charAt(i) == ":" || line.charAt(i) == ";")
        
        if(i < line.length-2){
            if(start_smile && line.charAt(i+1) == "-" && line.charAt(i+2) == ")"){
                console.log(i)
            }
        }
        
        if(start_smile && line.charAt(i+1) == ")"){
            console.log(i)
        }
    }
});
