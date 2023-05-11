const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

size = 0
l = []
rl.on('line', (line) => {
    if(size == 0){
        size = parseInt(line)
    }
    else{
        l = line.split(" ")
        for(i = 0; i < line.length; i++){
            l[i] = parseInt(l[i])
        }
        
        counter = 0
        for(i = 0; i < l.length; i++){
            if(l[i] < 0){
                counter ++;
            }
        }
        console.log(counter)
        
    }
});
