function is_duplicate(L, index, word){
    for (let i = 0; i < L.length; i++){
        if(i === index){
            continue;
        }
        else{
            if(L[i] === word){
                return true
            }            
        }
    }

    return false
}

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', (line) => {
    var L = line.split(' ')
    var length = L.length
    var dup = false
    for (let i = 0; i < length; i++){
        if(is_duplicate(L, i, L[i])){
            dup = true;
            break;
        }
    }
    
    if(dup){
        console.log('no');
    }
    else{
        console.log('yes');
    }
});
