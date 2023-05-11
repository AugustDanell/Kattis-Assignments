const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', (line) => {
    word_list = []
    found = false
    for(i = 0; i < line.length; i++){
        if (found){
            word_list.push(line[i])
        }
        else if(line[i] == "a"){
            found = true
            word_list.push(line[i])
        }
    }
    
    //console.log(word_list)
    console.log(word_list.join(""))
    
});
